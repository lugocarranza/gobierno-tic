from __future__ import annotations

import argparse
import re
from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Inches, Mm, Pt


TABLE_STYLE = "Table Grid"
HEADING_STYLES = tuple(f"Heading {level}" for level in range(1, 5))


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "cp1252"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def strip_front_matter(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                return "\n".join(lines[index + 1 :]).lstrip()
    return text


def clean_inline(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r"Imagen: \1 (\2)", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"_([^_]+)_", r"\1", text)
    return text.strip()


def has_style(document: Document, name: str) -> bool:
    try:
        document.styles[name]
    except KeyError:
        return False
    return True


def ensure_heading_styles(document: Document) -> None:
    default_document = Document()
    for name in HEADING_STYLES:
        if not has_style(document, name):
            document.styles.element.append(
                deepcopy(default_document.styles[name]._element)
            )


def is_separator_row(line: str) -> bool:
    cells = split_table_row(line)
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def is_table_start(lines: list[str], index: int) -> bool:
    if index + 1 >= len(lines):
        return False
    return "|" in lines[index] and is_separator_row(lines[index + 1])


def split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [clean_inline(cell.strip()) for cell in line.split("|")]


def collect_table(lines: list[str], index: int) -> tuple[list[list[str]], int]:
    rows = [split_table_row(lines[index])]
    index += 2
    while index < len(lines):
        line = lines[index]
        if not line.strip() or "|" not in line:
            break
        rows.append(split_table_row(line))
        index += 1
    return rows, index


def add_table(document: Document, rows: list[list[str]]) -> None:
    if not rows:
        return
    column_count = max(len(row) for row in rows)
    table = document.add_table(rows=0, cols=column_count)
    table.style = TABLE_STYLE
    for row_index, row_values in enumerate(rows):
        row = table.add_row()
        for column_index in range(column_count):
            value = row_values[column_index] if column_index < len(row_values) else ""
            cell = row.cells[column_index]
            cell.text = value
            if row_index == 0:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.bold = True


def add_code_block(document: Document, code_lines: list[str]) -> None:
    if not code_lines:
        return
    paragraph = document.add_paragraph()
    run = paragraph.add_run("\n".join(code_lines))
    run.font.name = "Consolas"
    run.font.size = Pt(9)


def add_markdown_line(document: Document, line: str) -> None:
    stripped = line.strip()
    if not stripped:
        return

    if re.fullmatch(r"[-*_]{3,}", stripped):
        return

    heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
    if heading:
        level = min(len(heading.group(1)), 4)
        document.add_heading(clean_inline(heading.group(2)), level=level)
        return

    unordered = re.match(r"^\s*[-*+]\s+(.+)$", line)
    if unordered:
        value = clean_inline(unordered.group(1))
        if has_style(document, "List Bullet"):
            document.add_paragraph(value, style="List Bullet")
        else:
            document.add_paragraph(f"• {value}", style="List Paragraph")
        return

    ordered = re.match(r"^\s*(\d+)\.\s+(.+)$", line)
    if ordered:
        value = clean_inline(ordered.group(2))
        if has_style(document, "List Number"):
            document.add_paragraph(value, style="List Number")
        else:
            document.add_paragraph(
                f"{ordered.group(1)}. {value}",
                style="List Paragraph",
            )
        return

    quote = re.match(r"^>\s*(.+)$", stripped)
    if quote:
        paragraph = document.add_paragraph()
        run = paragraph.add_run(clean_inline(quote.group(1)))
        run.italic = True
        return

    document.add_paragraph(clean_inline(stripped))


def create_document(template: Path | None) -> Document:
    if template is None:
        document = Document()
        section = document.sections[0]
        section.page_width = Mm(210)
        section.page_height = Mm(297)
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        return document

    document = Document(template)
    body = document._element.body
    for child in list(body):
        if child.tag != qn("w:sectPr"):
            body.remove(child)
    return document


def convert_markdown_to_docx(
    source: Path,
    output: Path,
    title_prefix: str,
    template: Path | None,
) -> None:
    text = strip_front_matter(read_text(source))
    lines = text.splitlines()

    document = create_document(template)
    ensure_heading_styles(document)

    document.core_properties.title = title_prefix

    index = 0
    in_code_block = False
    code_lines: list[str] = []

    while index < len(lines):
        line = lines[index]
        if line.strip().startswith("```"):
            if in_code_block:
                add_code_block(document, code_lines)
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            index += 1
            continue

        if in_code_block:
            code_lines.append(line)
            index += 1
            continue

        if is_table_start(lines, index):
            rows, index = collect_table(lines, index)
            add_table(document, rows)
            continue

        add_markdown_line(document, line)
        index += 1

    if code_lines:
        add_code_block(document, code_lines)

    output.parent.mkdir(parents=True, exist_ok=True)
    document.save(output)


def iter_markdown_files(source: Path, include_agents: bool) -> list[Path]:
    files = sorted(source.rglob("*.md"))
    if include_agents:
        return files
    return [path for path in files if path.name.lower() != "agents.md"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Export Markdown files to Word documents.")
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--template", type=Path)
    parser.add_argument("--include-agents", action="store_true")
    args = parser.parse_args()

    source_root = args.source.resolve()
    output_root = args.output.resolve()
    template = args.template.resolve() if args.template else None

    if not source_root.exists():
        raise SystemExit(f"No existe la carpeta fuente: {source_root}")
    if template is not None and not template.exists():
        raise SystemExit(f"No existe la plantilla: {template}")

    exported = 0
    for markdown_path in iter_markdown_files(source_root, args.include_agents):
        relative = markdown_path.relative_to(source_root)
        output_path = output_root / source_root.name / relative.with_suffix(".docx")
        convert_markdown_to_docx(
            markdown_path,
            output_path,
            str(relative.with_suffix("")),
            template,
        )
        print(f"Exportado: {relative} -> {output_path.relative_to(output_root)}")
        exported += 1

    print("")
    print(f"Documentos exportados: {exported}")
    print(f"Carpeta de salida: {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

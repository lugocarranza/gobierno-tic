param(
    [switch]$IncludeAgents
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir
$SourceDir = Join-Path $RepoRoot "GobiernoTI"
$OutputDir = Join-Path $RepoRoot "target\word"
$Converter = Join-Path $ScriptDir "md_to_docx.py"
$Template = Join-Path $ScriptDir "plantilla.docx"

if (-not (Test-Path $SourceDir)) {
    throw "No se encontro la carpeta fuente: $SourceDir"
}

if (-not (Test-Path $Converter)) {
    throw "No se encontro el conversor: $Converter"
}

$RuntimePython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

if (Test-Path $RuntimePython) {
    $Python = $RuntimePython
} else {
    $PythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if (-not $PythonCommand) {
        throw "No se encontro Python. Instale Python o ejecute desde Codex con el runtime disponible."
    }
    $Python = $PythonCommand.Source
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

$ArgsList = @(
    $Converter,
    "--source", $SourceDir,
    "--output", $OutputDir
)

if (Test-Path $Template) {
    $ArgsList += @("--template", $Template)
}

if ($IncludeAgents) {
    $ArgsList += "--include-agents"
}

Write-Host "Fuente : $SourceDir"
Write-Host "Salida : $OutputDir"
Write-Host "Python : $Python"
if (Test-Path $Template) {
    Write-Host "Plantilla: $Template"
} else {
    Write-Host "Plantilla: no encontrada; se utilizara el formato base"
}
Write-Host ""

& $Python @ArgsList

if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

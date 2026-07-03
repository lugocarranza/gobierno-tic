# AGENTS.md

## Lectura Inicial Obligatoria

Antes de analizar, revisar o modificar cualquier documento se deberá leer:

1. README.md
2. MAPA-DOCUMENTAL.md
3. El documento objetivo
4. Los documentos relacionados identificados en el mapa documental

Las modificaciones deben mantener consistencia entre todo el marco documental.

---

## Propósito del Proyecto

Este proyecto contiene la documentación normativa de Tecnologías de Información (TI) del Fondo de Inclusión Social Energético (FISE).

El objetivo es mantener un marco documental consistente, práctico y auditable para la gestión de TI, utilizando GitHub Flavored Markdown (GFM) como formato estándar.

La documentación busca ser aplicable a la realidad operativa del FISE y servir como base para procesos de gobierno, operación, desarrollo, seguridad y soporte tecnológico.

---

## Contexto del Proyecto

El FISE es una entidad pública del Perú con una estructura tecnológica pequeña.

El área de TI cuenta con recursos limitados y un equipo reducido, por lo que los documentos deben ser:

* Prácticos.
* Simples.
* Auditables.
* Sostenibles.
* Aplicables a una operación real.

Las propuestas, mejoras o recomendaciones deben priorizar:

* Simplicidad operativa.
* Trazabilidad.
* Seguridad razonable.
* Cumplimiento normativo.
* Mantenibilidad.
* Uso eficiente de recursos.

Evitar proponer estructuras, procesos o controles excesivamente complejos que resulten desproporcionados para el tamaño de la organización.

---

## Contexto Organizacional de TI

Como referencia organizacional considerar:

* Coordinador TIC o responsable designado de TIC.
* Dos desarrolladores de software.
* Responsable de Base de Datos.
* Especialista GIS.
* Mesa de Servicios o soporte.
* Proveedores externos cuando corresponda.

La misma persona puede asumir múltiples responsabilidades dependiendo de la necesidad operativa.

No asumir la existencia de:

* PMO.
* Arquitecto Empresarial.
* Oficina de Seguridad especializada.
* Comité de Arquitectura.
* Comité de Riesgos TI.
* CAB complejos o multinivel.
* Estructuras ITIL completas.

Las recomendaciones deben adaptarse a una organización pequeña.

---

## Estructura Documental

### Directivas

* DIR-GOB-TI
* DIR-GST-TI
* DIR-SEG-TI

### Procedimientos

* PRO-ACC-TI
* PRO-CAM-TI
* PRO-DES-TI
* PRO-INC-MAY-TI
* PRO-RES-TI

### Estándares

* EST-BD-TI
* EST-DES-TI

### Catálogos

* CAT-SER-TI

---

## Dependencias Documentales

Antes de modificar cualquier documento revisar:

```text
MAPA-DOCUMENTAL.md
```

para identificar:

* Dependencias.
* Impactos.
* Referencias cruzadas.
* Consistencia documental.

Cuando se modifique un documento deberá evaluarse si existen impactos sobre otros documentos relacionados.

No introducir cambios que generen contradicciones entre directivas, procedimientos, estándares o catálogos.

---

## Convenciones de Formato

Utilizar siempre GitHub Flavored Markdown (GFM).

Todos los documentos normativos deberán iniciar con Front Matter YAML.

Ejemplo:

```yaml
---
codigo: DIR-GOB-TI
titulo: Directiva de Gobierno de Tecnologías de Información
version: 1.0
tipo: Directiva
responsable: Coordinación de Tecnologías de Información
estado: Vigente
---
```

Utilizar:

* Encabezados Markdown.
* Tablas GFM.
* Listas simples.
* Bloques de código cuando corresponda.

Evitar formatos propietarios o dependientes de herramientas específicas.

---

## Convenciones de Redacción

Utilizar lenguaje institucional claro y directo.

Preferir expresiones como:

* deberá;
* podrá;
* cuando corresponda;
* según la criticidad;
* de manera razonable;
* conforme a la disponibilidad operativa.

Evitar:

* lenguaje excesivamente académico;
* marcos teóricos extensos;
* obligaciones difíciles de implementar;
* burocracia innecesaria.

Las disposiciones deben ser razonablemente aplicables y auditables.

---

## Criterios Normativos

Mantener alineamiento general con:

* Gobierno Digital.
* Seguridad de la Información.
* Protección de Datos Personales.
* Gestión de Servicios TI.
* Control Interno.
* Gestión de Cambios.
* Auditoría.

Las referencias a:

* ITIL
* COBIT
* ISO/IEC 27001
* ISO/IEC 20000
* ISO/IEC 38500

deben considerarse únicamente como buenas prácticas de referencia y no como una adopción integral obligatoria.

---

## Desarrollo de Software

Tecnologías preferentes para nuevos desarrollos:

### Backend

* Java.
* Spring Boot.

### Frontend

* Angular.
* React.

### Integración

* API REST.
* HTTPS.

### Seguridad

* Autenticación.
* Autorización basada en roles.
* Auditoría.
* Protección de datos sensibles.

Los sistemas legados pueden mantener sus tecnologías originales.

Las mejoras deberán alinearse progresivamente a los estándares institucionales cuando resulte técnica, operativa y económicamente viable.

---

## Base de Datos

El estándar de base de datos es neutral respecto al motor utilizado.

No asumir Oracle, PostgreSQL, SQL Server u otro motor salvo que el documento lo indique expresamente.

Conservar y respetar:

* Nomenclaturas.
* Prefijos.
* Campos de auditoría.
* Metadata.
* Integridad referencial.
* Constraints.
* Índices.
* Vistas.
* Procedimientos.
* Funciones.
* Triggers.
* Secuencias.

No eliminar reglas de nomenclatura ni tablas de prefijos sin justificación técnica.

---

## Estándares Técnicos

Los documentos EST-BD-TI y EST-DES-TI contienen lineamientos técnicos institucionales.

Al modificarlos:

* Conservar nomenclaturas y convenciones institucionales.
* No eliminar tablas de referencia sin justificación técnica.
* No simplificar estándares técnicos eliminando contenido útil.
* Mantener neutralidad tecnológica cuando corresponda.
* Evitar dependencias innecesarias a productos o fabricantes específicos.

Los estándares deben privilegiar principios de diseño y buenas prácticas por encima de herramientas particulares.

---

## Jira y Trazabilidad

La organización utiliza o busca utilizar Jira para:

* Backlog.
* Requerimientos.
* Incidencias.
* Cambios.
* Evidencias.
* Seguimiento.

No asumir que todos los usuarios registran directamente en Jira.

Los requerimientos pueden originarse mediante:

* Correo electrónico.
* Memorando.
* Ticket.
* Acta.
* Documento interno.
* Comunicación formal de un área usuaria.

Jira constituye un mecanismo de trazabilidad y seguimiento.

---

## Creación de Nuevos Documentos

No proponer nuevos documentos normativos salvo que exista una necesidad clara identificada.

Antes de crear una nueva directiva, procedimiento, estándar o catálogo, verificar si el tema puede incorporarse razonablemente en un documento existente.

Se debe privilegiar una estructura documental simple y mantenible.

---

## Al Modificar Documentos

Antes de realizar cambios:

1. Revisar el documento completo.
2. Revisar MAPA-DOCUMENTAL.md.
3. Identificar impactos en documentos relacionados.
4. Verificar consistencia normativa.
5. Mantener coherencia entre documentos.

Al proponer modificaciones:

* Explicar impactos relevantes.
* Identificar documentos potencialmente afectados.
* Mantener consistencia documental.
* Evitar duplicidades innecesarias.

---

## Restricciones

No inventar normativa.

No inventar estructuras organizacionales inexistentes.

No eliminar contenido técnico relevante de los estándares sin justificación.

No cambiar códigos documentales sin motivo sustentado.

No transformar documentos prácticos en marcos teóricos extensos.

Priorizar siempre:

* Aplicabilidad.
* Simplicidad.
* Trazabilidad.
* Mantenibilidad.
* Consistencia documental.

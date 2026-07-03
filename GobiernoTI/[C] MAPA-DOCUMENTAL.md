# MAPA DOCUMENTAL DE TECNOLOGÍAS DE INFORMACIÓN

## Propósito

Este documento describe la relación entre los documentos normativos de TI del FISE, sus dependencias principales y las evidencias mínimas esperadas para fines de trazabilidad y auditoría.

El mapa documental debe utilizarse antes de crear, modificar o eliminar contenido normativo, con la finalidad de mantener consistencia entre directivas, procedimientos, estándares y catálogos.

## Estructura General

La estructura documental distingue entre directivas marco, procedimientos operativos y estándares técnicos transversales. Los estándares no son hijos jerárquicos de la Directiva de Gobierno de TI; se mantienen separados y se aplican como referencia técnica para los procedimientos que correspondan.

```text
DIR-GOB-TI
|
+-- DIR-SEG-TI
|   +-- PRO-ACC-TI
|   +-- PRO-RES-TI
|   +-- PRO-INC-MAY-TI
|
+-- DIR-GST-TI
|   +-- CAT-SER-TI
|   +-- PRO-DES-TI
|   +-- PRO-CAM-TI
|   +-- PRO-INC-MAY-TI

EST-DES-TI
|
+-- PRO-DES-TI
+-- PRO-CAM-TI

EST-BD-TI
|
+-- PRO-DES-TI
+-- PRO-CAM-TI
+-- PRO-RES-TI

Formatos
|
+-- FOR-ACC-TI
+-- FOR-CAM-TI
+-- FOR-REQ-TI
+-- FOR-PRU-TI
+-- FOR-DES-TI
```

## Inventario Documental

| Tipo | Documento vigente |
|------|-------------------|
| Portada | README.md |
| Mapa documental | [C] MAPA-DOCUMENTAL.md |
| Capacitación | [C] CAPACITACION-TI.md |
| Capacitación | [C] CAPACITACION-USO-FORMATOS-TI.md |
| Directiva | DIR-GOB-TI.md |
| Directiva | DIR-GST-TI.md |
| Directiva | DIR-SEG-TI.md |
| Procedimiento | PRO-ACC-TI.md |
| Procedimiento | PRO-CAM-TI.md |
| Procedimiento | PRO-DES-TI.md |
| Procedimiento | PRO-INC-MAY-TI.md |
| Procedimiento | PRO-RES-TI.md |
| Estándar | EST-BD-TI.md |
| Estándar | EST-DES-TI.md |
| Catálogo | CAT-SER-TI.md |
| Formato | FOR-ACC-TI.md |
| Formato | FOR-CAM-TI.md |
| Formato | FOR-REQ-TI.md |
| Formato | FOR-PRU-TI.md |
| Formato | FOR-DES-TI.md |
| Casos de ejemplo | CASOS-EJEMPLO/README.md |
| Caso de ejemplo | CASOS-EJEMPLO/CASO-01-ALTA-USUARIO.md |
| Caso de ejemplo | CASOS-EJEMPLO/CASO-02-CAMBIO-MENOR-FILTRO-BANDEJA.md |
| Caso de ejemplo | CASOS-EJEMPLO/CASO-03-CAMBIO-MAYOR-FLUJO-PAGOS-ADELANTADOS.md |
| Caso de ejemplo | CASOS-EJEMPLO/CASO-04-CAMBIO-EMERGENCIA-ERROR-GRABAR-SOLICITUD.md |

`AGENTS.md` contiene instrucciones internas de mantenimiento para asistentes o agentes de trabajo. No forma parte del marco documental normativo, pero debe mantenerse alineado con los nombres vigentes de los documentos.

## Relación de Documentos

### [C] CAPACITACION-TI

Guía de apoyo para capacitación interna sobre la estructura del marco documental, los usuarios interesados, el uso de evidencias, los formatos y un caso integral de desarrollo complejo. No constituye un documento normativo ni crea obligaciones adicionales.

Documentos relacionados:

- README.md.
- [C] MAPA-DOCUMENTAL.md.
- CASOS-EJEMPLO.
- PRO-DES-TI.
- PRO-CAM-TI.
- PRO-ACC-TI.
- EST-DES-TI.
- EST-BD-TI.

Impactos de cambio:

- Si se modifican documentos, formatos, criterios de evidencia o casos de ejemplo, revisar esta guía para mantenerla alineada.
- La guía debe mantenerse como material orientador y no debe crear requisitos adicionales a los documentos normativos.

### [C] CAPACITACION-USO-FORMATOS-TI

Guía práctica para decidir cuándo conviene utilizar los formatos TIC y cuándo puede emplearse evidencia equivalente en Jira, Mesa de Servicios, correo, comentario estructurado o registro similar. No constituye un documento normativo ni crea obligaciones adicionales.

Documentos relacionados:

- README.md.
- [C] MAPA-DOCUMENTAL.md.
- FOR-ACC-TI.
- FOR-CAM-TI.
- FOR-REQ-TI.
- FOR-PRU-TI.
- FOR-DES-TI.
- PRO-ACC-TI.
- PRO-DES-TI.
- PRO-CAM-TI.

Impactos de cambio:

- Si se modifican criterios de uso, obligatoriedad o reemplazo de formatos, revisar esta guía para mantenerla alineada.
- Si se modifican los campos mínimos de los formatos, revisar esta guía para evitar contradicciones sobre evidencias equivalentes.
- La guía debe mantenerse como material orientador y no debe convertir los formatos en requisitos adicionales cuando exista evidencia suficiente.

### CASOS-EJEMPLO

Carpeta de apoyo para capacitación interna. Contiene ejemplos prácticos de aplicación del marco documental y no constituye un documento normativo.

Documentos relacionados:

- PRO-ACC-TI.
- PRO-CAM-TI.
- PRO-DES-TI.
- EST-DES-TI.
- EST-BD-TI.
- CAT-SER-TI.

Impactos de cambio:

- Si se modifican evidencias, clasificación de cambios o flujos de aprobación, revisar los casos de ejemplo para mantenerlos alineados.
- Los casos no deben crear obligaciones adicionales a las directivas, procedimientos, estándares o catálogos vigentes.

### FORMATOS

Formatos de apoyo para documentar accesos, cambios, requerimientos, evidencias de validación o pruebas y despliegues de software. Pueden usarse como documentos independientes, adjuntos o campos equivalentes en Jira, Mesa de Servicios, correo, comentario estructurado o registro similar.

Documentos relacionados:

- PRO-ACC-TI.
- PRO-DES-TI.
- PRO-CAM-TI.
- EST-DES-TI.
- EST-BD-TI.

Impactos de cambio:

- Si se modifican los campos mínimos de FOR-ACC-TI, revisar PRO-ACC-TI, DIR-SEG-TI y CAT-SER-TI.
- Si se modifican los campos mínimos de FOR-CAM-TI, revisar PRO-CAM-TI, PRO-DES-TI y EST-BD-TI.
- Si se modifican los campos mínimos de FOR-REQ-TI, revisar PRO-DES-TI y EST-DES-TI.
- Si se modifican los campos mínimos de FOR-PRU-TI, revisar PRO-DES-TI, PRO-CAM-TI y EST-DES-TI.
- Si se modifican los campos mínimos de FOR-DES-TI, revisar PRO-DES-TI, PRO-CAM-TI y EST-BD-TI.
- Los formatos no deben crear obligaciones adicionales cuando el ticket, historia, correo o registro equivalente contiene información suficiente.

### DIR-GOB-TI

Documento marco de gobierno de TI. Define principios, responsabilidades generales, toma de decisiones, portafolio, riesgos, indicadores y mejora continua.

Documentos relacionados:

- DIR-SEG-TI.
- DIR-GST-TI.

Impactos de cambio:

- Si se modifican responsabilidades generales de TI, revisar directivas y procedimientos relacionados.
- Si se agregan indicadores o nuevos procesos, verificar que no se creen obligaciones desproporcionadas para el equipo de TI.

### DIR-SEG-TI

Define lineamientos de seguridad de la información, clasificación de información, accesos, credenciales, uso aceptable, seguridad operativa e incidentes de seguridad.

Documentos relacionados:

- PRO-ACC-TI.
- PRO-RES-TI.
- PRO-INC-MAY-TI.
- EST-BD-TI.
- EST-DES-TI.

Impactos de cambio:

- Si se modifican controles de acceso, revisar PRO-ACC-TI.
- Si se modifican controles de respaldo, revisar PRO-RES-TI.
- Si se modifican criterios de incidentes de seguridad, revisar PRO-INC-MAY-TI.
- Si se modifican requisitos de seguridad de aplicaciones o datos, revisar EST-DES-TI y EST-BD-TI.

### DIR-GST-TI

Define lineamientos generales para la gestión de servicios tecnológicos, solicitudes, incidentes, problemas, cambios, activos, mantenimiento, monitoreo y catálogo de servicios.

Documentos relacionados:

- CAT-SER-TI.
- PRO-CAM-TI.
- PRO-DES-TI.
- PRO-INC-MAY-TI.
- PRO-ACC-TI.
- PRO-RES-TI.

Impactos de cambio:

- Si se modifican tipos de atención, prioridades o niveles de servicio, revisar CAT-SER-TI.
- Si se modifican lineamientos de cambios, revisar PRO-CAM-TI.
- Si se modifican lineamientos de desarrollo o mantenimiento, revisar PRO-DES-TI.
- Si se modifican criterios de incidentes mayores, revisar PRO-INC-MAY-TI.

### PRO-ACC-TI

Procedimiento para alta, modificación, revisión y baja de accesos.

Documentos relacionados:

- DIR-SEG-TI.
- DIR-GST-TI.
- CAT-SER-TI.
- EST-BD-TI.

Impactos de cambio:

- Si se modifican roles de aprobación, revisar DIR-SEG-TI y CAT-SER-TI.
- Si se modifican accesos privilegiados o periodicidad de revisión, revisar DIR-SEG-TI y EST-BD-TI.

### PRO-CAM-TI

Procedimiento para gestionar cambios tecnológicos de tipo menor, mayor y emergencia.

Documentos relacionados:

- DIR-GST-TI.
- PRO-DES-TI.
- EST-DES-TI.
- EST-BD-TI.
- PRO-RES-TI.

Impactos de cambio:

- Si se modifican evidencias de cambio, revisar PRO-DES-TI, EST-DES-TI y EST-BD-TI.
- Si se modifican requisitos de respaldo o reversa, revisar PRO-RES-TI.
- Si se modifican aprobaciones de pase a producción, revisar PRO-DES-TI.

### PRO-DES-TI

Procedimiento para requerimientos, desarrollo, mantenimiento, validación, conformidad y despliegue de software.

Documentos relacionados:

- DIR-GST-TI.
- DIR-SEG-TI.
- PRO-CAM-TI.
- EST-DES-TI.
- EST-BD-TI.

Impactos de cambio:

- Si se modifican tecnologías preferentes, revisar EST-DES-TI.
- Si se modifican cambios de base de datos, revisar EST-BD-TI y PRO-CAM-TI.
- Si se modifican evidencias de validación, pruebas o despliegue, revisar PRO-CAM-TI.

### PRO-INC-MAY-TI

Procedimiento para declarar, atender, comunicar, recuperar y cerrar incidentes mayores.

Documentos relacionados:

- DIR-GST-TI.
- DIR-SEG-TI.
- CAT-SER-TI.
- PRO-RES-TI.
- PRO-CAM-TI.

Impactos de cambio:

- Si se modifican criterios de criticidad, revisar CAT-SER-TI.
- Si se modifican acciones de recuperación, revisar PRO-RES-TI.
- Si se originan cambios posteriores al incidente, revisar PRO-CAM-TI.

### PRO-RES-TI

Procedimiento para respaldos, verificaciones, recuperación y pruebas de restauración.

Documentos relacionados:

- DIR-SEG-TI.
- DIR-GST-TI.
- PRO-CAM-TI.
- PRO-INC-MAY-TI.
- EST-BD-TI.

Impactos de cambio:

- Si se modifican frecuencias de respaldo, revisar DIR-SEG-TI y EST-BD-TI.
- Si se modifican pruebas de recuperación, revisar PRO-INC-MAY-TI.
- Si se modifican respaldos previos a cambios, revisar PRO-CAM-TI.

### EST-DES-TI

Estándar técnico para desarrollo, arquitectura, tecnologías preferentes, seguridad, calidad, sistemas legados y documentación mínima.

Documentos relacionados:

- PRO-DES-TI.
- PRO-CAM-TI.
- DIR-SEG-TI.
- EST-BD-TI.

Impactos de cambio:

- Si se modifican tecnologías preferentes, revisar PRO-DES-TI.
- Si se modifican controles de seguridad de aplicaciones, revisar DIR-SEG-TI.
- Si se modifican prácticas de despliegue, revisar PRO-CAM-TI.

### EST-BD-TI

Estándar técnico para diseño, administración, nomenclatura, seguridad, integridad, auditoría y cambios de base de datos.

Documentos relacionados:

- PRO-DES-TI.
- PRO-CAM-TI.
- PRO-RES-TI.
- DIR-SEG-TI.

Impactos de cambio:

- Si se modifican reglas de nomenclatura, revisar desarrollos y scripts institucionales afectados.
- Si se modifican controles de acceso a base de datos, revisar PRO-ACC-TI y DIR-SEG-TI.
- Si se modifican respaldos, restauración o scripts, revisar PRO-RES-TI y PRO-CAM-TI.

### CAT-SER-TI

Catálogo de servicios tecnológicos, tipos de atención, prioridades, niveles de servicio referenciales y grupos resolutores.

Documentos relacionados:

- DIR-GST-TI.
- PRO-ACC-TI.
- PRO-INC-MAY-TI.
- PRO-DES-TI.

Impactos de cambio:

- Si se agregan o retiran servicios, revisar responsabilidades y niveles de atención.
- Si se modifican prioridades, revisar PRO-INC-MAY-TI.
- Si se modifican servicios de accesos, revisar PRO-ACC-TI.

## Matriz de Evidencias Mínimas

| Proceso | Documento principal | Evidencia mínima |
|---------|---------------------|------------------|
| Gobierno de TI | DIR-GOB-TI | Portafolio o listado de iniciativas, riesgos relevantes, indicadores o informes disponibles. |
| Gestión de servicios | DIR-GST-TI / CAT-SER-TI | Tickets, registros de atención, prioridades, responsables y cierre. |
| Gestión de accesos | PRO-ACC-TI | Solicitud, aprobación, ticket, implementación, baja o revisión periódica. |
| Desarrollo de software | PRO-DES-TI | Requerimiento, código fuente, validación o pruebas según corresponda, conformidad y evidencia de despliegue. |
| Gestión de cambios | PRO-CAM-TI | Solicitud, evaluación técnica, aprobación cuando corresponda, validación proporcional, despliegue y cierre. |
| Formatos | FOR-ACC-TI / FOR-CAM-TI / FOR-REQ-TI / FOR-PRU-TI / FOR-DES-TI | Contenido mínimo de acceso, cambio, requerimiento, validación o despliegue, o campos equivalentes en Jira, correo, comentario o registro similar. |
| Respaldos y recuperación | PRO-RES-TI | Logs, registros de ejecución, verificaciones, solicitudes de restauración y pruebas de recuperación. |
| Incidentes mayores | PRO-INC-MAY-TI | Registro del incidente, comunicaciones, acciones realizadas, validación y cierre. |
| Seguridad de información | DIR-SEG-TI | Controles aplicados, revisiones de acceso, gestión de incidentes y evidencias de monitoreo cuando corresponda. |
| Base de datos | EST-BD-TI | Scripts, aprobaciones cuando correspondan, validación proporcional, registro de despliegue, respaldo o plan de reversa cuando corresponda. |
| Desarrollo y código fuente | EST-DES-TI | Repositorio, trazabilidad de versión, documentación mínima y evidencia de validación o pruebas según corresponda. |

## Criterios de Consistencia

Antes de modificar un documento se deberá verificar:

1. Si el cambio afecta responsabilidades.
2. Si el cambio crea nuevas evidencias obligatorias.
3. Si el cambio modifica plazos, prioridades o niveles de servicio.
4. Si el cambio impacta seguridad, accesos, respaldos, cambios o desarrollo.
5. Si el cambio resulta aplicable para una estructura de TI pequeña.

No deberán incorporarse obligaciones que requieran comités, áreas especializadas o herramientas que la organización no tenga, salvo que se indique expresamente como recomendación progresiva o condicionada a disponibilidad operativa.

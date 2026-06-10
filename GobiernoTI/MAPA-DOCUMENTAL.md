# MAPA DOCUMENTAL DE TECNOLOGIAS DE INFORMACION

## Proposito

Este documento describe la relacion entre los documentos normativos de TI del FISE, sus dependencias principales y las evidencias minimas esperadas para fines de trazabilidad y auditoria.

El mapa documental debe utilizarse antes de crear, modificar o eliminar contenido normativo, con la finalidad de mantener consistencia entre directivas, procedimientos, estandares y catalogos.

## Estructura General

La estructura documental distingue entre directivas marco, procedimientos operativos y estandares tecnicos transversales. Los estandares no son hijos jerarquicos de la Directiva de Gobierno de TI; se mantienen separados y se aplican como referencia tecnica para los procedimientos que correspondan.

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
```

## Relacion de Documentos

### CASOS-EJEMPLO

Carpeta de apoyo para capacitacion interna. Contiene ejemplos practicos de aplicacion del marco documental y no constituye un documento normativo.

Documentos relacionados:

- PRO-ACC-TI.
- PRO-CAM-TI.
- PRO-DES-TI.
- EST-DES-TI.
- EST-BD-TI.
- CAT-SER-TI.

Impactos de cambio:

- Si se modifican evidencias, clasificacion de cambios o flujos de aprobacion, revisar los casos de ejemplo para mantenerlos alineados.
- Los casos no deben crear obligaciones adicionales a las directivas, procedimientos, estandares o catalogos vigentes.

### DIR-GOB-TI

Documento marco de gobierno de TI. Define principios, responsabilidades generales, toma de decisiones, portafolio, riesgos, indicadores y mejora continua.

Documentos relacionados:

- DIR-SEG-TI.
- DIR-GST-TI.

Impactos de cambio:

- Si se modifican responsabilidades generales de TI, revisar directivas y procedimientos relacionados.
- Si se agregan indicadores o nuevos procesos, verificar que no se creen obligaciones desproporcionadas para el equipo de TI.

### DIR-SEG-TI

Define lineamientos de seguridad de la informacion, clasificacion de informacion, accesos, credenciales, uso aceptable, seguridad operativa e incidentes de seguridad.

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

Define lineamientos generales para la gestion de servicios tecnologicos, solicitudes, incidentes, problemas, cambios, activos, mantenimiento, monitoreo y catalogo de servicios.

Documentos relacionados:

- CAT-SER-TI.
- PRO-CAM-TI.
- PRO-DES-TI.
- PRO-INC-MAY-TI.
- PRO-ACC-TI.
- PRO-RES-TI.

Impactos de cambio:

- Si se modifican tipos de atencion, prioridades o niveles de servicio, revisar CAT-SER-TI.
- Si se modifican lineamientos de cambios, revisar PRO-CAM-TI.
- Si se modifican lineamientos de desarrollo o mantenimiento, revisar PRO-DES-TI.
- Si se modifican criterios de incidentes mayores, revisar PRO-INC-MAY-TI.

### PRO-ACC-TI

Procedimiento para alta, modificacion, revision y baja de accesos.

Documentos relacionados:

- DIR-SEG-TI.
- DIR-GST-TI.
- CAT-SER-TI.
- EST-BD-TI.

Impactos de cambio:

- Si se modifican roles de aprobacion, revisar DIR-SEG-TI y CAT-SER-TI.
- Si se modifican accesos privilegiados o periodicidad de revision, revisar DIR-SEG-TI y EST-BD-TI.

### PRO-CAM-TI

Procedimiento para gestionar cambios tecnologicos de tipo menor, mayor y emergencia.

Documentos relacionados:

- DIR-GST-TI.
- PRO-DES-TI.
- EST-DES-TI.
- EST-BD-TI.
- PRO-RES-TI.

Impactos de cambio:

- Si se modifican evidencias de cambio, revisar PRO-DES-TI, EST-DES-TI y EST-BD-TI.
- Si se modifican requisitos de respaldo o reversa, revisar PRO-RES-TI.
- Si se modifican aprobaciones de pase a produccion, revisar PRO-DES-TI.

### PRO-DES-TI

Procedimiento para requerimientos, desarrollo, mantenimiento, validacion, conformidad y despliegue de software.

Documentos relacionados:

- DIR-GST-TI.
- DIR-SEG-TI.
- PRO-CAM-TI.
- EST-DES-TI.
- EST-BD-TI.

Impactos de cambio:

- Si se modifican tecnologias preferentes, revisar EST-DES-TI.
- Si se modifican cambios de base de datos, revisar EST-BD-TI y PRO-CAM-TI.
- Si se modifican evidencias de validacion, pruebas o despliegue, revisar PRO-CAM-TI.

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
- Si se modifican acciones de recuperacion, revisar PRO-RES-TI.
- Si se originan cambios posteriores al incidente, revisar PRO-CAM-TI.

### PRO-RES-TI

Procedimiento para respaldos, verificaciones, recuperacion y pruebas de restauracion.

Documentos relacionados:

- DIR-SEG-TI.
- DIR-GST-TI.
- PRO-CAM-TI.
- PRO-INC-MAY-TI.
- EST-BD-TI.

Impactos de cambio:

- Si se modifican frecuencias de respaldo, revisar DIR-SEG-TI y EST-BD-TI.
- Si se modifican pruebas de recuperacion, revisar PRO-INC-MAY-TI.
- Si se modifican respaldos previos a cambios, revisar PRO-CAM-TI.

### EST-DES-TI

Estandar tecnico para desarrollo, arquitectura, tecnologias preferentes, seguridad, calidad, sistemas legados y documentacion minima.

Documentos relacionados:

- PRO-DES-TI.
- PRO-CAM-TI.
- DIR-SEG-TI.
- EST-BD-TI.

Impactos de cambio:

- Si se modifican tecnologias preferentes, revisar PRO-DES-TI.
- Si se modifican controles de seguridad de aplicaciones, revisar DIR-SEG-TI.
- Si se modifican practicas de despliegue, revisar PRO-CAM-TI.

### EST-BD-TI

Estandar tecnico para diseno, administracion, nomenclatura, seguridad, integridad, auditoria y cambios de base de datos.

Documentos relacionados:

- PRO-DES-TI.
- PRO-CAM-TI.
- PRO-RES-TI.
- DIR-SEG-TI.

Impactos de cambio:

- Si se modifican reglas de nomenclatura, revisar desarrollos y scripts institucionales afectados.
- Si se modifican controles de acceso a base de datos, revisar PRO-ACC-TI y DIR-SEG-TI.
- Si se modifican respaldos, restauracion o scripts, revisar PRO-RES-TI y PRO-CAM-TI.

### CAT-SER-TI

Catalogo de servicios tecnologicos, tipos de atencion, prioridades, niveles de servicio referenciales y grupos resolutores.

Documentos relacionados:

- DIR-GST-TI.
- PRO-ACC-TI.
- PRO-INC-MAY-TI.
- PRO-DES-TI.

Impactos de cambio:

- Si se agregan o retiran servicios, revisar responsabilidades y niveles de atencion.
- Si se modifican prioridades, revisar PRO-INC-MAY-TI.
- Si se modifican servicios de accesos, revisar PRO-ACC-TI.

## Matriz de Evidencias Minimas

| Proceso | Documento principal | Evidencia minima |
|---------|---------------------|------------------|
| Gobierno de TI | DIR-GOB-TI | Portafolio o listado de iniciativas, riesgos relevantes, indicadores o informes disponibles. |
| Gestion de servicios | DIR-GST-TI / CAT-SER-TI | Tickets, registros de atencion, prioridades, responsables y cierre. |
| Gestion de accesos | PRO-ACC-TI | Solicitud, aprobacion, ticket, implementacion, baja o revision periodica. |
| Desarrollo de software | PRO-DES-TI | Requerimiento, codigo fuente, validacion o pruebas segun corresponda, conformidad y evidencia de despliegue. |
| Gestion de cambios | PRO-CAM-TI | Solicitud, evaluacion tecnica, aprobacion cuando corresponda, validacion proporcional, despliegue y cierre. |
| Respaldos y recuperacion | PRO-RES-TI | Logs, registros de ejecucion, verificaciones, solicitudes de restauracion y pruebas de recuperacion. |
| Incidentes mayores | PRO-INC-MAY-TI | Registro del incidente, comunicaciones, acciones realizadas, validacion y cierre. |
| Seguridad de informacion | DIR-SEG-TI | Controles aplicados, revisiones de acceso, gestion de incidentes y evidencias de monitoreo cuando corresponda. |
| Base de datos | EST-BD-TI | Scripts, aprobaciones cuando correspondan, validacion proporcional, registro de despliegue, respaldo o plan de reversa cuando corresponda. |
| Desarrollo y codigo fuente | EST-DES-TI | Repositorio, trazabilidad de version, documentacion minima y evidencia de validacion o pruebas segun corresponda. |

## Criterios de Consistencia

Antes de modificar un documento se debera verificar:

1. Si el cambio afecta responsabilidades.
2. Si el cambio crea nuevas evidencias obligatorias.
3. Si el cambio modifica plazos, prioridades o niveles de servicio.
4. Si el cambio impacta seguridad, accesos, respaldos, cambios o desarrollo.
5. Si el cambio resulta aplicable para una estructura de TI pequena.

No deberan incorporarse obligaciones que requieran comites, areas especializadas o herramientas que la organizacion no tenga, salvo que se indique expresamente como recomendacion progresiva o condicionada a disponibilidad operativa.

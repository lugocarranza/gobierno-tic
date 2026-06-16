# Marco Documental de Tecnologias de Informacion

## Proposito

Este repositorio contiene la documentacion normativa de Tecnologias de Informacion (TI) del Fondo de Inclusion Social Energetico (FISE).

El objetivo es mantener un marco documental consistente, practico y auditable para la gestion de TI, aplicable a una entidad publica con un area tecnologica pequena y recursos limitados.

La documentacion busca servir como base para:

- Gobierno de TI.
- Gestion de servicios tecnologicos.
- Seguridad de la informacion.
- Gestion de accesos.
- Desarrollo y mantenimiento de software.
- Gestion de cambios.
- Respaldos y recuperacion.
- Atencion de incidentes mayores.
- Estandares tecnicos minimos.

## Criterios de Diseno

Los documentos han sido definidos considerando los siguientes criterios:

- Simplicidad operativa.
- Trazabilidad suficiente.
- Seguridad razonable.
- Cumplimiento normativo.
- Evidencia verificable para auditoria.
- Mantenibilidad por un equipo pequeno.
- Uso eficiente de recursos.

Las referencias a marcos como ITIL, COBIT, ISO/IEC 27001, ISO/IEC 20000 o ISO/IEC 38500 se consideran buenas practicas de referencia y no implican una adopcion integral obligatoria.

## Contexto Organizacional

El marco documental considera una estructura de TI pequena, donde una misma persona puede asumir mas de una responsabilidad de acuerdo con la necesidad operativa.

Como referencia, se consideran los siguientes roles:

- Coordinador TIC.
- Desarrolladores de software.
- Responsable de Base de Datos.
- Especialista GIS.
- Mesa de Servicios o soporte.
- Proveedores externos cuando corresponda.

No se asume la existencia de estructuras complejas como PMO, oficina especializada de seguridad, comites multinivel, CAB complejos o una implementacion completa de ITIL.

## Estructura Documental

### Directivas

- DIR-GOB-TI: Directiva de Gobierno de Tecnologias de Informacion.
- DIR-GST-TI: Directiva de Gestion de Servicios de Tecnologias de Informacion.
- DIR-SEG-TI: Directiva de Seguridad de la Informacion.

### Procedimientos

- PRO-ACC-TI: Procedimiento de Gestion de Accesos.
- PRO-CAM-TI: Procedimiento de Gestion de Cambios.
- PRO-DES-TI: Procedimiento de Desarrollo y Mantenimiento de Software.
- PRO-INC-MAY-TI: Procedimiento de Gestion de Incidentes Mayores.
- PRO-RES-TI: Procedimiento de Gestion de Respaldos y Recuperacion de Informacion.

### Estandares

- EST-BD-TI: Estandar de Base de Datos.
- EST-DES-TI: Estandar de Desarrollo y Codigo Fuente.

### Catalogos

- CAT-SER-TI: Catalogo de Servicios de Tecnologias de Informacion.

### Formatos Referenciales

- FOR-REQ-TI: Formato Referencial de Requerimiento de Software.
- FOR-PRU-TI: Formato Referencial de Evidencia de Validacion o Pruebas.
- FOR-DES-TI: Formato Referencial de Despliegue de Software.

Los formatos referenciales pueden utilizarse como documentos independientes, adjuntos o campos equivalentes en Jira, Mesa de Servicios, correo, comentario estructurado o registro similar. No crean obligaciones adicionales cuando el registro principal contiene la informacion minima suficiente.

### Material de Apoyo

- CASOS-EJEMPLO: Casos practicos para capacitacion sobre evidencias, documentos recibidos, documentos generados y sustento documental aplicable.

## Uso del Marco Documental

Antes de modificar un documento, se debe revisar el `MAPA-DOCUMENTAL.md` para identificar dependencias, documentos relacionados e impactos potenciales.

Las actualizaciones deben mantener coherencia entre directivas, procedimientos, estandares y catalogos, evitando duplicidades o exigencias que resulten desproporcionadas para la capacidad operativa del area de TI.

La carpeta `CASOS-EJEMPLO` es material orientador y no reemplaza ni modifica las directivas, procedimientos, estandares o catalogos vigentes.

## Evidencia y Auditoria

Para fines de auditoria, los documentos priorizan evidencias simples y verificables, tales como:

- Tickets.
- Correos electronicos.
- Actas.
- Registros de aprobacion.
- Capturas de pantalla.
- Logs.
- Reportes tecnicos.
- Evidencias de pruebas.
- Evidencias de despliegue.
- Registros de revision o verificacion.

La evidencia debe ser suficiente para demostrar solicitud, evaluacion, aprobacion, ejecucion, validacion y cierre, segun corresponda al proceso revisado.

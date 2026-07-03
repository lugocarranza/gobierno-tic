# Marco Documental de Tecnologías de Información

## Propósito

Este repositorio contiene la documentación normativa de Tecnologías de Información (TI) del Fondo de Inclusión Social Energético (FISE).

El objetivo es mantener un marco documental consistente, práctico y auditable para la gestión de TI, aplicable a una entidad pública con un área tecnológica pequeña y recursos limitados.

La documentación busca servir como base para:

- Gobierno de TI.
- Gestión de servicios tecnológicos.
- Seguridad de la información.
- Gestión de accesos.
- Desarrollo y mantenimiento de software.
- Gestión de cambios.
- Respaldos y recuperación.
- Atención de incidentes mayores.
- Estándares técnicos mínimos.

## Criterios de Diseño

Los documentos han sido definidos considerando los siguientes criterios:

- Simplicidad operativa.
- Trazabilidad suficiente.
- Seguridad razonable.
- Cumplimiento normativo.
- Evidencia verificable para auditoría.
- Mantenibilidad por un equipo pequeño.
- Uso eficiente de recursos.

Las referencias a marcos como ITIL, COBIT, ISO/IEC 27001, ISO/IEC 20000 o ISO/IEC 38500 se consideran buenas prácticas de referencia y no implican una adopción integral obligatoria.

## Contexto Organizacional

El marco documental considera una estructura de TI pequeña, donde una misma persona puede asumir más de una responsabilidad de acuerdo con la necesidad operativa.

Como referencia, se consideran los siguientes roles:

- Coordinador TIC o responsable designado de TIC.
- Desarrolladores de software.
- Responsable de Base de Datos.
- Especialista GIS.
- Mesa de Servicios o soporte.
- Proveedores externos cuando corresponda.

No se asume la existencia de estructuras complejas como PMO, oficina especializada de seguridad, comités multinivel, CAB complejos o una implementación completa de ITIL.

## Estructura Documental

### Directivas

- DIR-GOB-TI: Directiva de Gobierno de Tecnologías de Información.
- DIR-GST-TI: Directiva de Gestión de Servicios de Tecnologías de Información.
- DIR-SEG-TI: Directiva de Seguridad de la Información.

### Procedimientos

- PRO-ACC-TI: Procedimiento de Gestión de Accesos.
- PRO-CAM-TI: Procedimiento de Gestión de Cambios.
- PRO-DES-TI: Procedimiento de Desarrollo y Mantenimiento de Software.
- PRO-INC-MAY-TI: Procedimiento de Gestión de Incidentes Mayores.
- PRO-RES-TI: Procedimiento de Gestión de Respaldos y Recuperación de Información.

### Estándares

- EST-BD-TI: Estándar de Base de Datos.
- EST-DES-TI: Estándar de Desarrollo y Código Fuente.

### Catálogos

- CAT-SER-TI: Catálogo de Servicios de Tecnologías de Información.

### Formatos

- FOR-ACC-TI: Formato de Solicitud de Acceso.
- FOR-CAM-TI: Formato de Cambio.
- FOR-REQ-TI: Formato de Especificación de Requerimientos.
- FOR-PRU-TI: Formato de Evidencia de Validación o Pruebas.
- FOR-DES-TI: Formato de Despliegue de Software.

Los formatos pueden utilizarse como documentos independientes, adjuntos o campos equivalentes en Jira, Mesa de Servicios, correo, comentario estructurado o registro similar. No crean obligaciones adicionales cuando el registro principal contiene la información mínima suficiente.

### Material de Apoyo

- [C] CAPACITACION-TI: Guía de capacitación sobre directivas, lineamientos, evidencias y casos de aplicación del marco TIC.
- [C] CAPACITACION-USO-FORMATOS-TI: Guía práctica para decidir cuándo usar formatos TIC y cuándo puede bastar evidencia equivalente.
- CASOS-EJEMPLO: Casos prácticos para capacitación sobre evidencias, documentos recibidos, documentos generados y sustento documental aplicable.

## Uso del Marco Documental

Antes de modificar un documento, se debe revisar el `[C] MAPA-DOCUMENTAL.md` para identificar dependencias, documentos relacionados e impactos potenciales.

Las actualizaciones deben mantener coherencia entre directivas, procedimientos, estándares y catálogos, evitando duplicidades o exigencias que resulten desproporcionadas para la capacidad operativa del área de TI.

La carpeta `CASOS-EJEMPLO` es material orientador y no reemplaza ni modifica las directivas, procedimientos, estándares o catálogos vigentes.

## Evidencia y Auditoría

Para fines de auditoría, los documentos priorizan evidencias simples y verificables, tales como:

- Tickets.
- Correos electrónicos.
- Actas.
- Registros de aprobación.
- Capturas de pantalla.
- Logs.
- Reportes técnicos.
- Evidencias de pruebas.
- Evidencias de despliegue.
- Registros de revisión o verificación.

La evidencia debe ser suficiente para demostrar solicitud, evaluación, aprobación, ejecución, validación y cierre, según corresponda al proceso revisado.

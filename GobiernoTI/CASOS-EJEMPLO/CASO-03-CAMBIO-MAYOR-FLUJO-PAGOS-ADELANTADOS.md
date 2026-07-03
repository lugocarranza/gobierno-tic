# CASO 03: Cambio Mayor - Nuevo Flujo de Atención de Pagos Adelantados

## Objetivo del Caso

Mostrar qué evidencias deben conservarse cuando se implementa un cambio funcional relevante que afecta procesos, reglas de negocio o datos.

## Escenario

El área usuaria solicita implementar un nuevo flujo para registrar, evaluar y atender pagos adelantados.

El cambio incorpora nuevas reglas funcionales, validaciones, estados del proceso, pantallas, reportes y posibles ajustes en base de datos.

## Clasificación

| Elemento | Valor |
|----------|-------|
| Tipo de atención | Requerimiento / cambio |
| Tipo de cambio | Cambio mayor |
| Proceso principal | Desarrollo, gestión de cambios y base de datos |
| Riesgo referencial | Medio o alto |
| Aprobación requerida | Sí, aprobación formal proporcional al impacto |

## Documentos Finales en Jira o Historia de Usuario

Al cierre de la historia de usuario en sprint de Jira, ticket Kanban o herramienta equivalente, deberían figurar:

| Documento o evidencia final | Puede estar como | Sustento |
|-----------------------------|------------------|----------|
| Requerimiento formal o historia de usuario | Historia, ticket, acta, correo o documento adjunto | PRO-DES-TI / DIR-GST-TI |
| FOR-REQ-TI - Especificación de Requerimientos | Formato referencial, campos de Jira o documento equivalente | PRO-DES-TI / EST-DES-TI |
| FOR-CAM-TI - Formato de Cambio | Campos del ticket, comentario estructurado o adjunto | PRO-CAM-TI / FOR-CAM-TI |
| Evaluación técnica e impacto | Comentario técnico, documento interno o adjunto | PRO-CAM-TI / PRO-DES-TI |
| Aprobación formal proporcional | Aprobación en ticket, correo, acta o documento interno | PRO-CAM-TI |
| Evidencia de desarrollo | Commits, versión, merge request o enlace a repositorio | PRO-DES-TI / EST-DES-TI |
| Scripts y validación de base de datos, si aplica | Scripts adjuntos, enlace a repositorio o registro técnico | EST-BD-TI |
| Plan de reversión o mecanismo equivalente | Documento técnico, comentario, registro de despliegue o FOR-DES-TI cuando corresponda | PRO-CAM-TI / EST-BD-TI |
| Manual de usuario, guía de uso o instructivo actualizado | Documento, enlace, correo, captura comentada o material de capacitación | PRO-DES-TI / EST-DES-TI |
| Documento técnico o arquitectura simplificada | Documento interno, nota técnica, enlace a repositorio o adjunto | EST-DES-TI |
| FOR-PRU-TI - Evidencia de Validación o Pruebas | Formato referencial, capturas, comentarios, reportes o registro equivalente | PRO-DES-TI / EST-DES-TI |
| Validación técnica y funcional | Capturas, reportes, correo, acta o comentario de conformidad | PRO-DES-TI |
| FOR-DES-TI - Preparación del Despliegue | Formato referencial, plan del pase o comentario estructurado previo | PRO-CAM-TI / PRO-DES-TI |
| Autorización de pase a producción | Comentario, correo, aprobación en ticket principal o registro de despliegue | PRO-CAM-TI / PRO-DES-TI |
| Fecha real de implementación | Registro de despliegue, comentario en ticket o bitácora técnica | PRO-CAM-TI / PRO-DES-TI |
| Evidencia de despliegue y cierre | Registro de pase, fecha, responsable y estado cerrado | PRO-CAM-TI / PRO-DES-TI |

## Documentos o Evidencias Recibidas

| Momento | Evidencia recibida | Responsable sugerido | Para qué sirve |
|---------|--------------------|----------------------|----------------|
| Inicio | Requerimiento formal, ticket, correo, memorando o acta | Área usuaria | Sustenta la necesidad |
| Análisis | Descripción del nuevo flujo y reglas funcionales | Usuario responsable del proceso | Define alcance funcional |
| Análisis | Identificación de usuarios, roles o áreas impactadas | Área usuaria / Coordinación TIC / responsable designado de TIC | Evalúa impacto operativo |
| Análisis | Información sobre datos, reportes o integraciones afectadas | Responsable técnico / Responsable BD | Evalúa impacto técnico |

## Documentos o Evidencias Generadas

| Momento | Evidencia generada | Responsable sugerido | Conservación sugerida |
|---------|--------------------|----------------------|-----------------------|
| Registro | Ticket o registro del requerimiento | Mesa de Servicios / Coordinación TIC / responsable designado de TIC | Herramienta de seguimiento |
| Análisis | FOR-REQ-TI o campos equivalentes del requerimiento | Responsable técnico / Usuario responsable | Ticket, historia o documento adjunto |
| Evaluación | Evaluación técnica con alcance, impacto, riesgo y dependencias | Responsable técnico | Ticket, documento interno o correo |
| Evaluación | FOR-CAM-TI - Formato de Cambio | Responsable técnico / Coordinación TIC / responsable designado de TIC | Ticket o documento adjunto |
| Evaluación | Clasificación como cambio mayor | Responsable técnico / Coordinación TIC / responsable designado de TIC | FOR-CAM-TI o evaluación |
| Aprobación | Aprobación formal proporcional al impacto | Coordinación TIC o responsable designado de TIC y área usuaria o responsable funcional | Ticket, correo, acta o documento interno |
| Desarrollo | Registro de cambios en repositorio | Desarrollador | Repositorio institucional |
| Base de datos | Scripts DDL o DML, si corresponden | Responsable BD / Desarrollador | Repositorio, ticket o carpeta técnica |
| Preparación | Plan de reversión o mecanismo de rollback | Responsable técnico / Responsable BD | Ticket o documento interno |
| Documentación funcional | Manual de usuario, guía de uso o instructivo actualizado | Responsable funcional / Desarrollador | Ticket, repositorio documental o correo |
| Documentación técnica | Documento técnico o arquitectura simplificada | Responsable técnico | Repositorio, ticket o documento interno |
| Validación | FOR-PRU-TI o registro equivalente de escenarios validados | Desarrollador / Usuario responsable | Ticket, documento adjunto o evidencias enlazadas |
| Validación | Evidencia de validación técnica y funcional | Desarrollador / Usuario responsable | Capturas, registros, correo o acta |
| Pase a producción | Autorización del pase a producción | Coordinación TIC / responsable designado de TIC | Ticket principal, historia, correo o registro de despliegue |
| Preparación del despliegue | FOR-DES-TI o registro equivalente del pase a producción | Coordinación TIC / responsable designado de TIC / Responsable técnico | Ticket, registro de despliegue o documento adjunto |
| Despliegue | Evidencia de implementación en producción | Coordinación TIC / responsable designado de TIC / Responsable técnico | Ticket o registro de despliegue |
| Cierre | Conformidad funcional y cierre | Usuario responsable / Coordinación TIC / responsable designado de TIC | Ticket, correo o acta |

## Flujo Sugerido

```text
Requerimiento formal
|
Evaluación técnica
|
Clasificación como cambio mayor
|
Registro del FOR-CAM-TI o campos equivalentes
|
Aprobación formal proporcional
|
Desarrollo y ajustes técnicos
|
Validación técnica y funcional
|
Autorización del pase a producción
|
Pase a producción
|
Conformidad y cierre
```

## Validación Esperada

La evidencia debe ser proporcional al impacto. Puede incluir:

- Capturas del nuevo flujo.
- Validación de estados del proceso.
- Validación de reglas funcionales.
- Resultado de ejecución de scripts, si aplica.
- Revisión de reportes o datos generados.
- Conformidad del área usuaria.

Como el caso modifica la forma de atención del usuario, debe actualizarse el manual de usuario, guía de uso o instructivo disponible. La evidencia puede ser el documento actualizado, un enlace, un correo de comunicación, material de capacitación o una captura comentada si el cambio es acotado.

Por tratarse de un cambio mayor, se recomienda usar los formatos FOR-REQ-TI, FOR-CAM-TI, FOR-PRU-TI y FOR-DES-TI, o campos equivalentes en Jira, para consolidar el requerimiento, la evaluación del cambio, la validación y la preparación del despliegue. Su uso no reemplaza la aprobación del cambio ni la autorización del pase a producción.

## Llenado Referencial del FOR-CAM-TI

| Campo | Ejemplo |
|-------|---------|
| Código o Ticket | TIC-CAM-0002 |
| Fecha | Fecha de registro del cambio |
| Solicitante | Área usuaria responsable del proceso |
| Responsable Técnico | Líder técnico o desarrollador asignado |
| Descripción del Cambio | Implementar nuevo flujo de atención de pagos adelantados |
| Justificación | Atender una nueva necesidad operativa del proceso |
| Riesgo | Medio o Alto, según impacto |
| Tipo de Cambio | Mayor |

La fecha real de implementación, validación y conformidad se registran como evidencias posteriores en el ticket, correo, acta, registro de despliegue o documento equivalente.

La autorización del pase a producción puede registrarse en el ticket principal, historia de usuario, correo o registro de despliegue. Si el pase agrupa varias historias o tickets, se debe listar los elementos incluidos, por ejemplo: "Se autoriza el despliegue de TIC-201, TIC-202 y TIC-203".

## Sustento Documental

| Documento | Sustento |
|-----------|----------|
| DIR-GST-TI | Gestión de requerimientos, cambios, trazabilidad y mejora de servicios |
| PRO-CAM-TI | Cambio mayor, aprobación formal proporcional, validación y plan de reversión según riesgo |
| FOR-CAM-TI | Formato de Cambio o campos equivalentes en el ticket |
| PRO-DES-TI | Registro del requerimiento, análisis, desarrollo, validación, Anexo B - Evidencias Aceptadas, pase a producción y cierre |
| EST-DES-TI | Calidad, seguridad, trazabilidad de código y validación proporcional |
| EST-BD-TI | Cambios DDL/DML, nomenclatura, validación, scripts, respaldo o reversa cuando corresponda |
| PRO-RES-TI | Respaldo previo o recuperación si el cambio afecta información crítica; Anexo B - Evidencias Aceptadas cuando existan respaldos |

## Cierre Esperado

El caso se considera cerrado cuando:

- El nuevo flujo está implementado.
- Existen evidencias de evaluación, aprobación y validación.
- Los scripts o componentes técnicos están trazados.
- El área usuaria dio conformidad.
- El ticket o requerimiento fue cerrado.

## Evidencia Mínima Para Auditoría

- Requerimiento formal.
- FOR-REQ-TI o campos equivalentes del requerimiento.
- FOR-CAM-TI - Formato de Cambio, o campos equivalentes en el ticket.
- Evaluación técnica.
- Aprobación formal proporcional.
- Evidencia de desarrollo o configuración.
- Scripts y validación de base de datos, si aplica.
- Plan de reversión o mecanismo equivalente, si corresponde.
- Manual de usuario, guía de uso o instructivo actualizado.
- Documento técnico o arquitectura simplificada.
- FOR-PRU-TI o evidencia equivalente de validación.
- Evidencia de validación técnica o funcional.
- Autorización de pase a producción.
- FOR-DES-TI o registro equivalente de preparación del despliegue, cuando aporte trazabilidad.
- Evidencia de despliegue.
- Conformidad y cierre.

# CASO 03: Cambio Mayor - Nuevo Flujo de Atencion de Pagos Adelantados

## Objetivo del Caso

Mostrar que evidencias deben conservarse cuando se implementa un cambio funcional relevante que afecta procesos, reglas de negocio o datos.

## Escenario

El area usuaria solicita implementar un nuevo flujo para registrar, evaluar y atender pagos adelantados.

El cambio incorpora nuevas reglas funcionales, validaciones, estados del proceso, pantallas, reportes y posibles ajustes en base de datos.

## Clasificacion

| Elemento | Valor |
|----------|-------|
| Tipo de atencion | Requerimiento / cambio |
| Tipo de cambio | Cambio mayor |
| Proceso principal | Desarrollo, gestion de cambios y base de datos |
| Riesgo referencial | Medio o alto |
| Aprobacion requerida | Si, aprobacion formal proporcional al impacto |

## Documentos Finales en Jira o Historia de Usuario

Al cierre de la historia de usuario en sprint de Jira, ticket Kanban o herramienta equivalente, deberian figurar:

| Documento o evidencia final | Puede estar como | Sustento |
|-----------------------------|------------------|----------|
| Requerimiento formal o historia de usuario | Historia, ticket, acta, correo o documento adjunto | PRO-DES-TI / DIR-GST-TI |
| Anexo B - Formato de Cambio | Campos del ticket, comentario estructurado o adjunto | PRO-CAM-TI |
| Evaluacion tecnica e impacto | Comentario tecnico, documento interno o adjunto | PRO-CAM-TI / PRO-DES-TI |
| Aprobacion formal proporcional | Aprobacion en ticket, correo, acta o documento interno | PRO-CAM-TI |
| Evidencia de desarrollo | Commits, version, merge request o enlace a repositorio | PRO-DES-TI / EST-DES-TI |
| Scripts y validacion de base de datos, si aplica | Scripts adjuntos, enlace a repositorio o registro tecnico | EST-BD-TI |
| Plan de reversion o mecanismo equivalente | Campo del Anexo B, documento o comentario tecnico | PRO-CAM-TI / EST-BD-TI |
| Manual de usuario, guia de uso o instructivo actualizado | Documento, enlace, correo, captura comentada o material de capacitacion | PRO-DES-TI / EST-DES-TI |
| Documento tecnico o arquitectura simplificada | Documento interno, nota tecnica, enlace a repositorio o adjunto | EST-DES-TI |
| Validacion tecnica y funcional | Capturas, reportes, correo, acta o comentario de conformidad | PRO-DES-TI |
| Autorizacion de pase a produccion | Comentario, correo, aprobacion en ticket principal o registro de despliegue | PRO-CAM-TI / PRO-DES-TI |
| Fecha real de implementacion | Registro de despliegue, comentario en ticket o bitacora tecnica | PRO-CAM-TI / PRO-DES-TI |
| Evidencia de despliegue y cierre | Registro de pase, fecha, responsable y estado cerrado | PRO-CAM-TI / PRO-DES-TI |

## Documentos o Evidencias Recibidas

| Momento | Evidencia recibida | Responsable sugerido | Para que sirve |
|---------|--------------------|----------------------|----------------|
| Inicio | Requerimiento formal, ticket, correo, memorando o acta | Area usuaria | Sustenta la necesidad |
| Analisis | Descripcion del nuevo flujo y reglas funcionales | Usuario responsable del proceso | Define alcance funcional |
| Analisis | Identificacion de usuarios, roles o areas impactadas | Area usuaria / Coordinacion TIC | Evalua impacto operativo |
| Analisis | Informacion sobre datos, reportes o integraciones afectadas | Responsable tecnico / Responsable BD | Evalua impacto tecnico |

## Documentos o Evidencias Generadas

| Momento | Evidencia generada | Responsable sugerido | Conservacion sugerida |
|---------|--------------------|----------------------|-----------------------|
| Registro | Ticket o registro del requerimiento | Mesa de Servicios / Coordinacion TIC | Herramienta de seguimiento |
| Evaluacion | Evaluacion tecnica con alcance, impacto, riesgo y dependencias | Responsable tecnico | Ticket, documento interno o correo |
| Evaluacion | Anexo B - Formato de Cambio | Responsable tecnico / Coordinacion TIC | Ticket o documento adjunto |
| Evaluacion | Clasificacion como cambio mayor | Responsable tecnico / Coordinacion TIC | Anexo B o evaluacion |
| Aprobacion | Aprobacion formal proporcional al impacto | Coordinacion TIC y area usuaria o responsable funcional | Ticket, correo, acta o documento interno |
| Desarrollo | Registro de cambios en repositorio | Desarrollador | Repositorio institucional |
| Base de datos | Scripts DDL o DML, si corresponden | Responsable BD / Desarrollador | Repositorio, ticket o carpeta tecnica |
| Preparacion | Plan de reversion o mecanismo de rollback | Responsable tecnico / Responsable BD | Ticket o documento interno |
| Documentacion funcional | Manual de usuario, guia de uso o instructivo actualizado | Responsable funcional / Desarrollador | Ticket, repositorio documental o correo |
| Documentacion tecnica | Documento tecnico o arquitectura simplificada | Responsable tecnico | Repositorio, ticket o documento interno |
| Validacion | Evidencia de validacion tecnica y funcional | Desarrollador / Usuario responsable | Capturas, registros, correo o acta |
| Pase a produccion | Autorizacion del pase a produccion | Coordinacion TIC | Ticket principal, historia, correo o registro de despliegue |
| Despliegue | Evidencia de implementacion en produccion | Coordinacion TIC / Responsable tecnico | Ticket o registro de despliegue |
| Cierre | Conformidad funcional y cierre | Usuario responsable / Coordinacion TIC | Ticket, correo o acta |

## Flujo Sugerido

```text
Requerimiento formal
|
Evaluacion tecnica
|
Clasificacion como cambio mayor
|
Registro del Anexo B
|
Aprobacion formal proporcional
|
Desarrollo y ajustes tecnicos
|
Validacion tecnica y funcional
|
Autorizacion del pase a produccion
|
Pase a produccion
|
Conformidad y cierre
```

## Validacion Esperada

La evidencia debe ser proporcional al impacto. Puede incluir:

- Capturas del nuevo flujo.
- Validacion de estados del proceso.
- Validacion de reglas funcionales.
- Resultado de ejecucion de scripts, si aplica.
- Revision de reportes o datos generados.
- Conformidad del area usuaria.

Como el caso modifica la forma de atencion del usuario, debe actualizarse el manual de usuario, guia de uso o instructivo disponible. La evidencia puede ser el documento actualizado, un enlace, un correo de comunicacion, material de capacitacion o una captura comentada si el cambio es acotado.

## Llenado Referencial del Anexo B

| Campo | Ejemplo |
|-------|---------|
| Codigo o Ticket | TIC-CAM-0002 |
| Fecha | Fecha de registro del cambio |
| Solicitante | Area usuaria responsable del proceso |
| Responsable Tecnico | Lider tecnico o desarrollador asignado |
| Descripcion del Cambio | Implementar nuevo flujo de atencion de pagos adelantados |
| Justificacion | Atender una nueva necesidad operativa del proceso |
| Riesgo | Medio o Alto, segun impacto |
| Tipo de Cambio | Mayor |
| Plan de Reversion | Restaurar version anterior, revertir scripts o deshabilitar flujo nuevo |

La fecha real de implementacion, validacion y conformidad se registran como evidencias posteriores en el ticket, correo, acta, registro de despliegue o documento equivalente.

La autorizacion del pase a produccion puede registrarse en el ticket principal, historia de usuario, correo o registro de despliegue. Si el pase agrupa varias historias o tickets, se debe listar los elementos incluidos, por ejemplo: "Se autoriza el despliegue de TIC-201, TIC-202 y TIC-203".

## Sustento Documental

| Documento | Sustento |
|-----------|----------|
| DIR-GST-TI | Gestion de requerimientos, cambios, trazabilidad y mejora de servicios |
| PRO-CAM-TI | Cambio mayor, Anexo B - Formato de Cambio, aprobacion formal proporcional, validacion y plan de reversion segun riesgo |
| PRO-DES-TI | Registro del requerimiento, analisis, desarrollo, validacion, Anexo B - Evidencias Aceptadas, pase a produccion y cierre |
| EST-DES-TI | Calidad, seguridad, trazabilidad de codigo y validacion proporcional |
| EST-BD-TI | Cambios DDL/DML, nomenclatura, validacion, scripts, respaldo o reversa cuando corresponda |
| PRO-RES-TI | Respaldo previo o recuperacion si el cambio afecta informacion critica; Anexo B - Evidencias Aceptadas cuando existan respaldos |

## Cierre Esperado

El caso se considera cerrado cuando:

- El nuevo flujo esta implementado.
- Existen evidencias de evaluacion, aprobacion y validacion.
- Los scripts o componentes tecnicos estan trazados.
- El area usuaria dio conformidad.
- El ticket o requerimiento fue cerrado.

## Evidencia Minima Para Auditoria

- Requerimiento formal.
- Anexo B - Formato de Cambio.
- Evaluacion tecnica.
- Aprobacion formal proporcional.
- Evidencia de desarrollo o configuracion.
- Scripts y validacion de base de datos, si aplica.
- Plan de reversion o mecanismo equivalente, si corresponde.
- Manual de usuario, guia de uso o instructivo actualizado.
- Documento tecnico o arquitectura simplificada.
- Evidencia de validacion tecnica o funcional.
- Autorizacion de pase a produccion.
- Evidencia de despliegue.
- Conformidad y cierre.

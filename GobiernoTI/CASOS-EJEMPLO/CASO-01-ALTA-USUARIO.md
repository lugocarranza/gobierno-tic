# CASO 01: Alta de Usuario

## Objetivo del Caso

Mostrar que evidencias deben conservarse cuando se solicita y habilita el acceso de un nuevo usuario a servicios tecnologicos institucionales.

## Escenario

Ingresa una nueva persona al FISE y requiere correo institucional, acceso al sistema correspondiente a su area, carpeta compartida y acceso a la Mesa de Servicios.

## Clasificacion

| Elemento | Valor |
|----------|-------|
| Tipo de atencion | Solicitud |
| Proceso principal | Gestion de accesos |
| Riesgo referencial | Bajo o medio, segun los sistemas solicitados |
| Aprobacion requerida | Si, por jefatura o coordinacion solicitante y validacion administrativa cuando corresponda |

## Documentos Finales en Jira o Ticket de Atencion

Al cierre del ticket de Mesa de Servicios, Kanban Jira o herramienta equivalente, deberian figurar:

| Documento o evidencia final | Puede estar como | Sustento |
|-----------------------------|------------------|----------|
| Solicitud de acceso | FOR-ACC-TI, formulario, ticket o correo con campos equivalentes | PRO-ACC-TI / FOR-ACC-TI |
| Validacion de vinculo laboral o contractual | Comentario, correo o validacion adjunta | PRO-ACC-TI |
| Aprobacion del area responsable | Comentario, correo, aprobacion en ticket o formato | PRO-ACC-TI / DIR-SEG-TI |
| Registro de accesos implementados | Comentario tecnico, captura o registro del sistema | PRO-ACC-TI |
| Comunicacion de habilitacion | Correo o comentario en ticket | PRO-ACC-TI / DIR-GST-TI |
| Cierre del ticket | Estado cerrado con resumen de atencion | DIR-GST-TI |

## Documentos o Evidencias Recibidas

| Momento | Evidencia recibida | Responsable sugerido | Para que sirve |
|---------|--------------------|----------------------|----------------|
| Inicio | Solicitud de acceso por ticket, correo o formato | Jefatura o coordinacion solicitante | Sustenta la necesidad del acceso |
| Inicio | Datos del usuario: nombres, cargo, area, fecha de inicio | Jefatura solicitante / Gestion de Personas | Permite crear la cuenta correctamente |
| Validacion | Confirmacion de vinculo laboral o contractual | Gestion de Personas | Verifica que el usuario puede recibir accesos |
| Aprobacion | Aprobacion del responsable del area | Jefatura o coordinacion solicitante | Autoriza el acceso solicitado |

## Documentos o Evidencias Generadas

| Momento | Evidencia generada | Responsable sugerido | Conservacion sugerida |
|---------|--------------------|----------------------|-----------------------|
| Registro | Ticket de atencion | Mesa de Servicios / Coordinacion TIC / responsable designado de TIC | En Mesa de Servicios o herramienta disponible |
| Implementacion | Registro de cuenta creada y perfiles asignados | Coordinacion TIC / responsable designado de TIC | Ticket, captura o registro tecnico |
| Implementacion | Evidencia de MFA o controles aplicados cuando corresponda | Coordinacion TIC / responsable designado de TIC | Ticket o captura |
| Notificacion | Comunicacion de habilitacion al usuario o area | Coordinacion TIC / responsable designado de TIC | Correo o comentario en ticket |
| Cierre | Ticket cerrado con resumen de accesos habilitados | Mesa de Servicios / Coordinacion TIC / responsable designado de TIC | Ticket cerrado |

## Flujo Sugerido

```text
Solicitud
|
Validacion de vinculo
|
Aprobacion del area
|
Implementacion de accesos
|
Notificacion
|
Cierre del ticket
```

## Sustento Documental

| Documento | Sustento |
|-----------|----------|
| DIR-SEG-TI | Control de accesos, minimo privilegio, necesidad de acceso y revocacion |
| DIR-GST-TI | Mesa de Servicios como punto de contacto y trazabilidad de atenciones |
| PRO-ACC-TI | Alta de accesos, validacion, aprobacion, implementacion, registro y evidencias |
| FOR-ACC-TI | Formato de Solicitud de Acceso o campos equivalentes en el ticket |
| CAT-SER-TI | Servicios de gestion de accesos, correo institucional y sistemas institucionales |

## Cierre Esperado

El caso se considera cerrado cuando:

- El usuario tiene los accesos autorizados.
- La solicitud, aprobacion e implementacion estan registradas.
- El usuario o area fue notificado.
- El ticket contiene resumen de cierre.

## Evidencia Minima Para Auditoria

- Solicitud o ticket.
- FOR-ACC-TI - Formato de Solicitud de Acceso, o campos equivalentes en el ticket.
- Validacion de vinculo laboral o contractual.
- Aprobacion del area responsable.
- Evidencia de implementacion.
- Comunicacion de habilitacion.
- Cierre del ticket.

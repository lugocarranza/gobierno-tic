# CASO 01: Alta de Usuario

## Objetivo del Caso

Mostrar qué evidencias deben conservarse cuando se solicita y habilita el acceso de un nuevo usuario a servicios tecnológicos institucionales.

## Escenario

Ingresa una nueva persona al FISE y requiere correo institucional, acceso al sistema correspondiente a su área, carpeta compartida y acceso a la Mesa de Servicios.

## Clasificación

| Elemento | Valor |
|----------|-------|
| Tipo de atención | Solicitud |
| Proceso principal | Gestión de accesos |
| Riesgo referencial | Bajo o medio, según los sistemas solicitados |
| Aprobación requerida | Sí, por jefatura o coordinación solicitante y validación administrativa cuando corresponda |

## Documentos Finales en Jira o Ticket de Atención

Al cierre del ticket de Mesa de Servicios, Kanban Jira o herramienta equivalente, deberían figurar:

| Documento o evidencia final | Puede estar como | Sustento |
|-----------------------------|------------------|----------|
| Solicitud de acceso | FOR-ACC-TI, formulario, ticket o correo con campos equivalentes | PRO-ACC-TI / FOR-ACC-TI |
| Validación de vínculo laboral o contractual | Comentario, correo o validación adjunta | PRO-ACC-TI |
| Aprobación del área responsable | Comentario, correo, aprobación en ticket o formato | PRO-ACC-TI / DIR-SEG-TI |
| Registro de accesos implementados | Comentario técnico, captura o registro del sistema | PRO-ACC-TI |
| Comunicación de habilitación | Correo o comentario en ticket | PRO-ACC-TI / DIR-GST-TI |
| Cierre del ticket | Estado cerrado con resumen de atención | DIR-GST-TI |

## Documentos o Evidencias Recibidas

| Momento | Evidencia recibida | Responsable sugerido | Para qué sirve |
|---------|--------------------|----------------------|----------------|
| Inicio | Solicitud de acceso por ticket, correo o formato | Jefatura o coordinación solicitante | Sustenta la necesidad del acceso |
| Inicio | Datos del usuario: nombres, cargo, área, fecha de inicio | Jefatura solicitante / Gestión de Personas | Permite crear la cuenta correctamente |
| Validación | Confirmación de vínculo laboral o contractual | Gestión de Personas | Verifica que el usuario puede recibir accesos |
| Aprobación | Aprobación del responsable del área | Jefatura o coordinación solicitante | Autoriza el acceso solicitado |

## Documentos o Evidencias Generadas

| Momento | Evidencia generada | Responsable sugerido | Conservación sugerida |
|---------|--------------------|----------------------|-----------------------|
| Registro | Ticket de atención | Mesa de Servicios / Coordinación TIC / responsable designado de TIC | En Mesa de Servicios o herramienta disponible |
| Implementación | Registro de cuenta creada y perfiles asignados | Coordinación TIC / responsable designado de TIC | Ticket, captura o registro técnico |
| Implementación | Evidencia de MFA o controles aplicados cuando corresponda | Coordinación TIC / responsable designado de TIC | Ticket o captura |
| Notificación | Comunicación de habilitación al usuario o área | Coordinación TIC / responsable designado de TIC | Correo o comentario en ticket |
| Cierre | Ticket cerrado con resumen de accesos habilitados | Mesa de Servicios / Coordinación TIC / responsable designado de TIC | Ticket cerrado |

## Flujo Sugerido

```text
Solicitud
|
Validación de vínculo
|
Aprobación del área
|
Implementación de accesos
|
Notificación
|
Cierre del ticket
```

## Sustento Documental

| Documento | Sustento |
|-----------|----------|
| DIR-SEG-TI | Control de accesos, mínimo privilegio, necesidad de acceso y revocación |
| DIR-GST-TI | Mesa de Servicios como punto de contacto y trazabilidad de atenciones |
| PRO-ACC-TI | Alta de accesos, validación, aprobación, implementación, registro y evidencias |
| FOR-ACC-TI | Formato de Solicitud de Acceso o campos equivalentes en el ticket |
| CAT-SER-TI | Servicios de gestión de accesos, correo institucional y sistemas institucionales |

## Cierre Esperado

El caso se considera cerrado cuando:

- El usuario tiene los accesos autorizados.
- La solicitud, aprobación e implementación están registradas.
- El usuario o área fue notificado.
- El ticket contiene resumen de cierre.

## Evidencia Mínima Para Auditoría

- Solicitud o ticket.
- FOR-ACC-TI - Formato de Solicitud de Acceso, o campos equivalentes en el ticket.
- Validación de vínculo laboral o contractual.
- Aprobación del área responsable.
- Evidencia de implementación.
- Comunicación de habilitación.
- Cierre del ticket.

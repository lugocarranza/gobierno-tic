# CASO 04: Cambio de Emergencia - Error al Grabar Solicitud

## Objetivo del Caso

Mostrar como documentar una atencion urgente cuando un error impide continuar un flujo operativo.

## Escenario

Los usuarios reportan que el sistema no permite grabar una solicitud. Al intentar guardar, aparece un error y el flujo no puede continuar.

La incidencia afecta la operacion del area usuaria y requiere correccion inmediata.

## Clasificacion

| Elemento | Valor |
|----------|-------|
| Tipo de atencion | Incidente / cambio de emergencia |
| Tipo de cambio | Cambio de emergencia |
| Proceso principal | Gestion de cambios e incidente operativo |
| Riesgo referencial | Medio o alto, segun impacto |
| Aprobacion requerida | Autorizacion rapida y regularizacion posterior |

## Documentos Finales en Jira o Ticket de Incidente

Al cierre del ticket Kanban, incidente Jira o herramienta equivalente, deberian figurar:

| Documento o evidencia final | Puede estar como | Sustento |
|-----------------------------|------------------|----------|
| Reporte del incidente | Ticket, correo, llamada registrada o comentario de Mesa de Servicios | DIR-GST-TI |
| Evidencia del error | Captura, mensaje de error, log o descripcion reproducible | PRO-CAM-TI / PRO-DES-TI |
| Autorizacion rapida | Comentario, correo, mensaje institucional o registro de decision | PRO-CAM-TI |
| Acciones ejecutadas | Comentario tecnico, commit, bitacora o enlace a repositorio | PRO-CAM-TI / PRO-DES-TI |
| Anexo B - Formato de Cambio | Regularizado despues de estabilizar la operacion | PRO-CAM-TI |
| Validacion de recuperacion | Captura, confirmacion del usuario o prueba funcional simple | PRO-CAM-TI / PRO-DES-TI |
| Fecha real de implementacion | Comentario tecnico, bitacora o registro de atencion urgente | PRO-CAM-TI |
| Evaluacion de incidente mayor, si aplica | Declaracion, resumen o referencia al flujo de incidente mayor | PRO-INC-MAY-TI |
| Cierre | Estado cerrado con resumen y resultado | DIR-GST-TI |

## Documentos o Evidencias Recibidas

| Momento | Evidencia recibida | Responsable sugerido | Para que sirve |
|---------|--------------------|----------------------|----------------|
| Deteccion | Reporte del usuario por ticket, correo o llamada registrada | Usuario afectado / Mesa de Servicios | Identifica el incidente |
| Diagnostico | Captura del error o descripcion del comportamiento | Usuario afectado / Responsable tecnico | Permite reproducir o analizar la falla |
| Evaluacion | Identificacion del impacto operativo | Coordinacion TIC / Area usuaria | Sustenta la urgencia |
| Autorizacion | Autorizacion rapida para corregir | Coordinacion TIC o responsable designado | Permite ejecutar el cambio urgente |

## Documentos o Evidencias Generadas

| Momento | Evidencia generada | Responsable sugerido | Conservacion sugerida |
|---------|--------------------|----------------------|-----------------------|
| Registro | Ticket o registro del incidente | Mesa de Servicios / Coordinacion TIC | Herramienta de seguimiento |
| Diagnostico | Causa probable o analisis breve | Responsable tecnico | Ticket o comentario tecnico |
| Atencion | Acciones ejecutadas para corregir | Responsable tecnico | Ticket, repositorio o bitacora |
| Validacion inmediata | Evidencia de que la solicitud ya graba correctamente | Responsable tecnico / Usuario afectado | Captura, correo o comentario en ticket |
| Regularizacion | Anexo B - Formato de Cambio, regularizado posteriormente | Coordinacion TIC / Responsable tecnico | Ticket o documento interno |
| Cierre | Resumen de cierre y conformidad cuando corresponda | Coordinacion TIC / Area usuaria | Ticket cerrado |

## Flujo Sugerido

```text
Reporte del incidente
|
Evaluacion de impacto
|
Autorizacion rapida
|
Correccion urgente
|
Validacion inmediata
|
Regularizacion documental
|
Cierre
```

## Validacion Esperada

La validacion puede realizarse antes o inmediatamente despues de la implementacion, segun la urgencia.

Evidencias posibles:

- Captura del error original.
- Captura o comentario que confirme que la solicitud se graba correctamente.
- Prueba funcional simple realizada por el responsable tecnico.
- Confirmacion del usuario afectado.
- Registro del cambio aplicado.

## Llenado Referencial del Anexo B

El Anexo B puede completarse despues de restablecer la operacion.

| Campo | Ejemplo |
|-------|---------|
| Codigo o Ticket | TIC-INC-0003 |
| Fecha | Fecha del incidente o de regularizacion |
| Solicitante | Usuario o area que reporta la falla |
| Responsable Tecnico | Responsable que atiende la correccion |
| Descripcion del Cambio | Correccion urgente del error que impedia grabar solicitudes |
| Justificacion | Restablecer la continuidad del flujo operativo |
| Riesgo | Medio o Alto, segun afectacion |
| Tipo de Cambio | Emergencia |
| Plan de Reversion | Restaurar version anterior o revertir ajuste aplicado si falla |

La fecha real de implementacion, validacion y conformidad se registran durante la regularizacion posterior mediante comentarios, correo, evidencia tecnica, cierre del ticket o medio equivalente.

## Sustento Documental

| Documento | Sustento |
|-----------|----------|
| DIR-GST-TI | Gestion de incidentes, priorizacion, trazabilidad y restablecimiento del servicio |
| DIR-SEG-TI | Gestion de incidentes de seguridad cuando el error involucre confidencialidad, integridad o disponibilidad |
| PRO-CAM-TI | Cambio de emergencia, autorizacion rapida, Anexo B regularizado, validacion y regularizacion posterior |
| PRO-DES-TI | Mantenimiento correctivo, Anexo B - Evidencias Aceptadas y mecanismos abreviados ante urgencia |
| PRO-INC-MAY-TI | Aplicable si el impacto permite declararlo incidente mayor; Anexos A y B como referencia de flujo y criticidad |
| EST-DES-TI | Validacion proporcional y trazabilidad del codigo fuente |
| EST-BD-TI | Aplicable si la correccion requiere scripts DDL/DML o ajuste de datos |

## Cierre Esperado

El caso se considera cerrado cuando:

- La solicitud puede grabarse correctamente.
- La correccion esta registrada.
- La evidencia de validacion fue conservada.
- La regularizacion documental fue completada.
- El ticket o incidente fue cerrado.

## Evidencia Minima Para Auditoria

- Reporte del incidente.
- Evidencia del error.
- Autorizacion rapida o registro de decision.
- Anexo B - Formato de Cambio, regularizado posteriormente.
- Acciones ejecutadas.
- Evidencia de validacion.
- Regularizacion posterior del cambio.
- Cierre del ticket.

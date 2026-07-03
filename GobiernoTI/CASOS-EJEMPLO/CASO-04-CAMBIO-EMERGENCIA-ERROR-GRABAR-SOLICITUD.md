# CASO 04: Cambio de Emergencia - Error al Grabar Solicitud

## Objetivo del Caso

Mostrar cómo documentar una atención urgente cuando un error impide continuar un flujo operativo.

## Escenario

Los usuarios reportan que el sistema no permite grabar una solicitud. Al intentar guardar, aparece un error y el flujo no puede continuar.

La incidencia afecta la operación del área usuaria y requiere corrección inmediata.

## Clasificación

| Elemento | Valor |
|----------|-------|
| Tipo de atención | Incidente / cambio de emergencia |
| Tipo de cambio | Cambio de emergencia |
| Proceso principal | Gestión de cambios e incidente operativo |
| Riesgo referencial | Medio o alto, según impacto |
| Aprobación requerida | Autorización rápida y regularización posterior |

## Documentos Finales en Jira o Ticket de Incidente

Al cierre del ticket Kanban, incidente Jira o herramienta equivalente, deberían figurar:

| Documento o evidencia final | Puede estar como | Sustento |
|-----------------------------|------------------|----------|
| Reporte del incidente | Ticket, correo, llamada registrada o comentario de Mesa de Servicios | DIR-GST-TI |
| Evidencia del error | Captura, mensaje de error, log o descripción reproducible | PRO-CAM-TI / PRO-DES-TI |
| Autorización rápida | Comentario, correo, mensaje institucional o registro de decisión | PRO-CAM-TI |
| Acciones ejecutadas | Comentario técnico, commit, bitácora o enlace a repositorio | PRO-CAM-TI / PRO-DES-TI |
| FOR-CAM-TI - Formato de Cambio | Regularizado después de estabilizar la operación | PRO-CAM-TI / FOR-CAM-TI |
| Validación de recuperación | Captura, confirmación del usuario o prueba funcional simple | PRO-CAM-TI / PRO-DES-TI |
| FOR-PRU-TI o evidencia equivalente | Regularizado después si conviene consolidar la validación | PRO-DES-TI |
| Fecha real de implementación | Comentario técnico, bitácora o registro de atención urgente | PRO-CAM-TI |
| FOR-DES-TI o registro equivalente | Regularizado después solo si se requiere resumir la preparación del pase ejecutado | PRO-CAM-TI / PRO-DES-TI |
| Evaluación de incidente mayor, si aplica | Declaración, resumen o referencia al flujo de incidente mayor | PRO-INC-MAY-TI |
| Cierre | Estado cerrado con resumen y resultado | DIR-GST-TI |

## Documentos o Evidencias Recibidas

| Momento | Evidencia recibida | Responsable sugerido | Para qué sirve |
|---------|--------------------|----------------------|----------------|
| Detección | Reporte del usuario por ticket, correo o llamada registrada | Usuario afectado / Mesa de Servicios | Identifica el incidente |
| Diagnóstico | Captura del error o descripción del comportamiento | Usuario afectado / Responsable técnico | Permite reproducir o analizar la falla |
| Evaluación | Identificación del impacto operativo | Coordinación TIC / responsable designado de TIC / Área usuaria | Sustenta la urgencia |
| Autorización | Autorización rápida para corregir | Coordinación TIC o responsable designado de TIC | Permite ejecutar el cambio urgente |

## Documentos o Evidencias Generadas

| Momento | Evidencia generada | Responsable sugerido | Conservación sugerida |
|---------|--------------------|----------------------|-----------------------|
| Registro | Ticket o registro del incidente | Mesa de Servicios / Coordinación TIC / responsable designado de TIC | Herramienta de seguimiento |
| Diagnóstico | Causa probable o análisis breve | Responsable técnico | Ticket o comentario técnico |
| Atención | Acciones ejecutadas para corregir | Responsable técnico | Ticket, repositorio o bitácora |
| Validación inmediata | Evidencia de que la solicitud ya graba correctamente | Responsable técnico / Usuario afectado | Captura, correo o comentario en ticket |
| Regularización | FOR-CAM-TI - Formato de Cambio, regularizado posteriormente | Coordinación TIC / responsable designado de TIC / Responsable técnico | Ticket o documento interno |
| Regularización | FOR-PRU-TI o FOR-DES-TI, si corresponde por riesgo, impacto o necesidad de resumir la validación o preparación del pase | Coordinación TIC / responsable designado de TIC / Responsable técnico | Ticket, registro de despliegue o documento interno |
| Cierre | Resumen de cierre y conformidad cuando corresponda | Coordinación TIC / responsable designado de TIC / Área usuaria | Ticket cerrado |

## Flujo Sugerido

```text
Reporte del incidente
|
Evaluación de impacto
|
Autorización rápida
|
Corrección urgente
|
Validación inmediata
|
Regularización documental
|
Cierre
```

## Validación Esperada

La validación puede realizarse antes o inmediatamente después de la implementación, según la urgencia.

Evidencias posibles:

- Captura del error original.
- Captura o comentario que confirme que la solicitud se graba correctamente.
- Prueba funcional simple realizada por el responsable técnico.
- Confirmación del usuario afectado.
- Registro del cambio aplicado.

## Llenado Referencial del FOR-CAM-TI

El FOR-CAM-TI puede completarse después de restablecer la operación.

| Campo | Ejemplo |
|-------|---------|
| Código o Ticket | TIC-INC-0003 |
| Fecha | Fecha del incidente o de regularización |
| Solicitante | Usuario o área que reporta la falla |
| Responsable Técnico | Responsable que atiende la corrección |
| Descripción del Cambio | Corrección urgente del error que impedía grabar solicitudes |
| Justificación | Restablecer la continuidad del flujo operativo |
| Riesgo | Medio o Alto, según afectación |
| Tipo de Cambio | Emergencia |

La fecha real de implementación, validación y conformidad se registran durante la regularización posterior mediante comentarios, correo, evidencia técnica, cierre del ticket o medio equivalente.

Si la emergencia requirió un despliegue coordinado, scripts, reversa o validaciones que convenga consolidar, el FOR-DES-TI o el FOR-PRU-TI podrán completarse después de estabilizar la operación. El FOR-DES-TI se usará solo para resumir la preparación del pase ejecutado; el resultado de la emergencia puede quedar en el ticket, comentario, bitácora o cierre. Si el ticket contiene fecha, responsable, acciones ejecutadas, validación y resultado, no será necesario elaborar un formato separado.

## Sustento Documental

| Documento | Sustento |
|-----------|----------|
| DIR-GST-TI | Gestión de incidentes, priorización, trazabilidad y restablecimiento del servicio |
| DIR-SEG-TI | Gestión de incidentes de seguridad cuando el error involucre confidencialidad, integridad o disponibilidad |
| PRO-CAM-TI | Cambio de emergencia, autorización rápida, validación y regularización posterior |
| FOR-CAM-TI | Formato de Cambio regularizado posteriormente o campos equivalentes |
| PRO-DES-TI | Mantenimiento correctivo, Anexo B - Evidencias Aceptadas y mecanismos abreviados ante urgencia |
| PRO-INC-MAY-TI | Aplicable si el impacto permite declararlo incidente mayor; Anexos A y B como referencia de flujo y criticidad |
| EST-DES-TI | Validación proporcional y trazabilidad del código fuente |
| EST-BD-TI | Aplicable si la corrección requiere scripts DDL/DML o ajuste de datos |

## Cierre Esperado

El caso se considera cerrado cuando:

- La solicitud puede grabarse correctamente.
- La corrección está registrada.
- La evidencia de validación fue conservada.
- La regularización documental fue completada.
- El ticket o incidente fue cerrado.

## Evidencia Mínima Para Auditoría

- Reporte del incidente.
- Evidencia del error.
- Autorización rápida o registro de decisión.
- FOR-CAM-TI - Formato de Cambio, regularizado posteriormente, o campos equivalentes en el ticket.
- Acciones ejecutadas.
- Evidencia de validación.
- FOR-PRU-TI o FOR-DES-TI regularizado, cuando corresponda por riesgo, impacto o necesidad de resumir la validación o preparación del pase.
- Regularización posterior del cambio.
- Cierre del ticket.

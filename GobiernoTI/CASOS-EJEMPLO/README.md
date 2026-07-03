# Casos de Ejemplo para Evidencias TI

## Propósito

Esta carpeta contiene casos ficticios y realistas para capacitar al equipo de TI sobre qué evidencias deben recibirse, generarse y conservarse durante la atención de accesos, requerimientos, cambios y emergencias.

Los casos son material de apoyo y no reemplazan a las directivas, procedimientos, estándares o catálogos vigentes.

## Cómo Usar Estos Casos

Cada caso muestra:

- Objetivo del caso.
- Escenario.
- Clasificación.
- Documentos finales que deben figurar en Jira.
- Documentos o evidencias recibidas.
- Documentos o evidencias generadas.
- Momento en que se genera cada evidencia.
- Responsable sugerido.
- Sustento documental aplicable.
- Cierre esperado.

La finalidad es que el equipo identifique qué evidencia es suficiente y en qué momento debe conservarse, sin crear burocracia adicional.

## Casos Incluidos

| Caso | Escenario | Proceso principal |
|------|-----------|-------------------|
| CASO-01 | Alta de usuario | Gestión de accesos |
| CASO-02 | Filtro en bandeja de solicitudes | Cambio menor / desarrollo |
| CASO-03 | Nuevo flujo de pagos adelantados | Cambio mayor / desarrollo |
| CASO-04 | Error al grabar solicitud | Cambio de emergencia |

## Índice

- [CASO-01-ALTA-USUARIO.md](CASO-01-ALTA-USUARIO.md)
- [CASO-02-CAMBIO-MENOR-FILTRO-BANDEJA.md](CASO-02-CAMBIO-MENOR-FILTRO-BANDEJA.md)
- [CASO-03-CAMBIO-MAYOR-FLUJO-PAGOS-ADELANTADOS.md](CASO-03-CAMBIO-MAYOR-FLUJO-PAGOS-ADELANTADOS.md)
- [CASO-04-CAMBIO-EMERGENCIA-ERROR-GRABAR-SOLICITUD.md](CASO-04-CAMBIO-EMERGENCIA-ERROR-GRABAR-SOLICITUD.md)

## Criterio General

La evidencia debe permitir reconstruir, de forma simple:

1. Quién solicitó.
2. Qué se solicitó.
3. Quién evaluó o autorizó, cuando corresponda.
4. Qué se ejecutó.
5. Cómo se validó.
6. Cuándo se cerró.

Para cambios menores bastará una validación simple o evidencia equivalente. Para cambios mayores se requiere evidencia razonable de evaluación, aprobación, validación y cierre. Para cambios de emergencia se permite regularizar la evidencia luego de estabilizar el servicio.

## Anexos Operativos Considerados

Los casos consideran los anexos operativos del marco documental cuando aplican:

| Documento | Anexo | Uso en los casos |
|-----------|-------|------------------|
| FOR-ACC-TI | Formato de Solicitud de Acceso | Alta, modificación o baja de accesos. Puede estar como formato adjunto o como campos del ticket. |
| FOR-CAM-TI | Formato de Cambio | Cambios menores, mayores y de emergencia. En emergencia puede regularizarse después. |
| PRO-DES-TI | Anexo B - Evidencias Aceptadas | Requerimientos de desarrollo, validación, despliegue y cierre. |
| FOR-REQ-TI | Formato de Especificación de Requerimientos | Recomendado para desarrollos nuevos, mejoras significativas o cambios funcionales relevantes; puede reemplazarse por campos equivalentes en Jira. |
| FOR-PRU-TI | Formato de Evidencia de Validación o Pruebas | Recomendado cuando existan varios escenarios, riesgo medio/alto o evidencia que convenga consolidar. |
| FOR-DES-TI | Formato de Despliegue de Software | Recomendado para despliegues con varios cambios, ventana coordinada, scripts, respaldo, reversa o comunicación a usuarios. |
| PRO-INC-MAY-TI | Anexos A y B | Solo cuando el incidente se declare como incidente mayor o se use como referencia de criticidad. |
| PRO-RES-TI | Anexos A y B | Solo cuando existan respaldos, restauraciones o verificaciones asociadas al caso. |

Los anexos de los estándares técnicos se usan como referencia técnica y no como formatos de atención.

Los formatos no son obligatorios cuando el ticket, historia, correo, comentario o registro equivalente contiene la información mínima suficiente.

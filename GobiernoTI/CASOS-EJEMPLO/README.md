# Casos de Ejemplo para Evidencias TI

## Proposito

Esta carpeta contiene casos ficticios y realistas para capacitar al equipo de TI sobre que evidencias deben recibirse, generarse y conservarse durante la atencion de accesos, requerimientos, cambios y emergencias.

Los casos son material de apoyo y no reemplazan a las directivas, procedimientos, estandares o catalogos vigentes.

## Como Usar Estos Casos

Cada caso muestra:

- Objetivo del caso.
- Escenario.
- Clasificacion.
- Documentos finales que deben figurar en Jira.
- Documentos o evidencias recibidas.
- Documentos o evidencias generadas.
- Momento en que se genera cada evidencia.
- Responsable sugerido.
- Sustento documental aplicable.
- Cierre esperado.

La finalidad es que el equipo identifique que evidencia es suficiente y en que momento debe conservarse, sin crear burocracia adicional.

## Casos Incluidos

| Caso | Escenario | Proceso principal |
|------|-----------|-------------------|
| CASO-01 | Alta de usuario | Gestion de accesos |
| CASO-02 | Filtro en bandeja de solicitudes | Cambio menor / desarrollo |
| CASO-03 | Nuevo flujo de pagos adelantados | Cambio mayor / desarrollo |
| CASO-04 | Error al grabar solicitud | Cambio de emergencia |

## Indice

- [CASO-01-ALTA-USUARIO.md](CASO-01-ALTA-USUARIO.md)
- [CASO-02-CAMBIO-MENOR-FILTRO-BANDEJA.md](CASO-02-CAMBIO-MENOR-FILTRO-BANDEJA.md)
- [CASO-03-CAMBIO-MAYOR-FLUJO-PAGOS-ADELANTADOS.md](CASO-03-CAMBIO-MAYOR-FLUJO-PAGOS-ADELANTADOS.md)
- [CASO-04-CAMBIO-EMERGENCIA-ERROR-GRABAR-SOLICITUD.md](CASO-04-CAMBIO-EMERGENCIA-ERROR-GRABAR-SOLICITUD.md)

## Criterio General

La evidencia debe permitir reconstruir, de forma simple:

1. Quien solicito.
2. Que se solicito.
3. Quien evaluo o autorizo, cuando corresponda.
4. Que se ejecuto.
5. Como se valido.
6. Cuando se cerro.

Para cambios menores bastara una validacion simple o evidencia equivalente. Para cambios mayores se requiere evidencia razonable de evaluacion, aprobacion, validacion y cierre. Para cambios de emergencia se permite regularizar la evidencia luego de estabilizar el servicio.

## Anexos Operativos Considerados

Los casos consideran los anexos operativos del marco documental cuando aplican:

| Documento | Anexo | Uso en los casos |
|-----------|-------|------------------|
| PRO-ACC-TI | Anexo A - Formato de Solicitud de Acceso | Alta, modificacion o baja de accesos. Puede estar como formato adjunto o como campos del ticket. |
| PRO-CAM-TI | Anexo B - Formato de Cambio | Cambios menores, mayores y de emergencia. En emergencia puede regularizarse despues. |
| PRO-DES-TI | Anexo B - Evidencias Aceptadas | Requerimientos de desarrollo, validacion, despliegue y cierre. |
| FOR-REQ-TI | Formato Referencial de Requerimiento de Software | Recomendado para desarrollos nuevos, mejoras significativas o cambios funcionales relevantes; puede reemplazarse por campos equivalentes en Jira. |
| FOR-PRU-TI | Formato Referencial de Evidencia de Validacion o Pruebas | Recomendado cuando existan varios escenarios, riesgo medio/alto o evidencia que convenga consolidar. |
| FOR-DES-TI | Formato Referencial de Despliegue de Software | Recomendado para despliegues con varios cambios, ventana coordinada, scripts, respaldo, reversa o comunicacion a usuarios. |
| PRO-INC-MAY-TI | Anexos A y B | Solo cuando el incidente se declare como incidente mayor o se use como referencia de criticidad. |
| PRO-RES-TI | Anexos A y B | Solo cuando existan respaldos, restauraciones o verificaciones asociadas al caso. |

Los anexos de los estandares tecnicos se usan como referencia tecnica y no como formatos de atencion.

Los formatos referenciales no son obligatorios cuando el ticket, historia, correo, comentario o registro equivalente contiene la informacion minima suficiente.

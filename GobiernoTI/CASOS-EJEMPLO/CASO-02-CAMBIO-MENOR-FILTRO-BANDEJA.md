# CASO 02: Cambio Menor - Filtro en Bandeja de Solicitudes

## Objetivo del Caso

Mostrar cómo documentar un requerimiento menor de desarrollo sin generar aprobaciones innecesarias.

## Escenario

El área usuaria solicita agregar un filtro por estado en la bandeja de solicitudes para facilitar la búsqueda de registros.

El cambio no modifica reglas de negocio, cálculos, datos históricos, permisos, integraciones ni procesos críticos.

## Clasificación

| Elemento | Valor |
|----------|-------|
| Tipo de atención | Requerimiento |
| Tipo de cambio | Cambio menor |
| Proceso principal | Desarrollo y gestión de cambios |
| Riesgo referencial | Bajo |
| Aprobación requerida | No requiere aprobación formal previa |

## Documentos Finales en Jira o Historia de Usuario

Al cierre del ticket Kanban, historia de usuario en sprint de Jira o herramienta equivalente, deberían figurar:

| Documento o evidencia final | Puede estar como | Sustento |
|-----------------------------|------------------|----------|
| Ticket, requerimiento o historia de usuario | Registro principal en Jira o Mesa de Servicios | PRO-DES-TI / DIR-GST-TI |
| FOR-CAM-TI - Formato de Cambio | Campos del ticket, comentario estructurado o adjunto | PRO-CAM-TI / FOR-CAM-TI |
| Registro de implementación | Commit, comentario técnico, bitácora o enlace a repositorio | PRO-DES-TI / EST-DES-TI |
| Validación simple | Captura, comentario de conformidad o revisión funcional | PRO-CAM-TI / PRO-DES-TI |
| Guía breve, captura comentada o actualización de instructivo | Solo si el filtro cambia la forma de uso habitual o requiere comunicación al usuario | PRO-DES-TI / EST-DES-TI |
| Autorización de pase a producción | Comentario en el mismo ticket o historia | PRO-CAM-TI / PRO-DES-TI |
| Fecha real de implementación | Comentario en ticket, registro de despliegue o cierre técnico | PRO-CAM-TI |
| Cierre | Estado cerrado con resumen del resultado | DIR-GST-TI |

En un cambio menor, los formatos FOR-CAM-TI, FOR-REQ-TI, FOR-PRU-TI y FOR-DES-TI no son obligatorios si el ticket, historia, correo o comentario contiene los datos mínimos del cambio, requerimiento, validación y pase a producción. Pueden usarse como apoyo solo cuando aporten claridad o trazabilidad adicional.

## Documentos o Evidencias Recibidas

| Momento | Evidencia recibida | Responsable sugerido | Para qué sirve |
|---------|--------------------|----------------------|----------------|
| Inicio | Ticket, correo o requerimiento del área usuaria | Usuario solicitante | Identifica la necesidad |
| Análisis | Descripción simple del filtro requerido | Usuario solicitante / Desarrollador | Delimita el alcance |
| Análisis | Pantalla o referencia de la bandeja actual, si existe | Usuario solicitante / Desarrollador | Ayuda a validar el resultado |

## Documentos o Evidencias Generadas

| Momento | Evidencia generada | Responsable sugerido | Conservación sugerida |
|---------|--------------------|----------------------|-----------------------|
| Registro | Ticket o registro del requerimiento | Mesa de Servicios / Coordinación TIC / responsable designado de TIC | Herramienta de seguimiento |
| Análisis | FOR-CAM-TI o campos equivalentes del cambio, llenado con datos mínimos | Responsable técnico | Ticket o documento adjunto |
| Análisis | Confirmación de que es cambio menor | Responsable técnico | FOR-CAM-TI o comentario en ticket |
| Implementación | Registro del cambio realizado en repositorio o bitácora | Desarrollador | Repositorio o ticket |
| Validación | Captura del filtro implementado o resultado de revisión | Desarrollador / Usuario solicitante | Ticket |
| Documentación | Guía breve, captura comentada o instructivo actualizado, si corresponde | Desarrollador / Usuario solicitante | Ticket, correo o repositorio documental |
| Pase a producción | Autorización de pase en el mismo ticket o comentario | Coordinación TIC / responsable designado de TIC | Ticket o historia de usuario |
| Cierre | Conformidad simple o cierre del ticket | Usuario solicitante / Coordinación TIC / responsable designado de TIC | Ticket o correo |

## Flujo Sugerido

```text
Solicitud
|
Registro del requerimiento
|
Clasificación como cambio menor
|
Registro mínimo del FOR-CAM-TI o campos equivalentes
|
Implementación
|
Validación simple
|
Autorización de pase en el mismo ticket
|
Cierre
```

## Llenado Referencial del FOR-CAM-TI

| Campo | Ejemplo |
|-------|---------|
| Código o Ticket | TIC-REQ-0001 |
| Fecha | Fecha de registro del ticket |
| Solicitante | Área usuaria responsable de la bandeja |
| Responsable Técnico | Desarrollador asignado |
| Descripción del Cambio | Agregar filtro por estado en la bandeja de solicitudes |
| Justificación | Facilitar la búsqueda y seguimiento de solicitudes |
| Riesgo | Bajo |
| Tipo de Cambio | Menor |

El FOR-CAM-TI puede registrarse dentro del mismo ticket si la herramienta permite capturar estos campos.

La fecha real de implementación, validación y conformidad no requieren reenviar el FOR-CAM-TI completo. Pueden quedar como comentarios, capturas, correo o cierre del ticket.

## Validación Esperada

Para este tipo de cambio basta una evidencia simple, por ejemplo:

- Captura de la bandeja con el nuevo filtro.
- Comentario del usuario indicando conformidad.
- Resultado de revisión funcional simple.
- Cierre del ticket con descripción del cambio.

No se requieren pruebas unitarias obligatorias ni aprobación formal previa.

El manual de usuario o instructivo no es obligatorio para todo cambio menor. Se actualiza solo cuando el ajuste modifica la forma en que el usuario opera el sistema o cuando se necesita comunicar el nuevo uso; en ese caso puede bastar una captura comentada, una guía breve o un comentario instructivo en el ticket.

La autorización del pase a producción puede registrarse en el mismo ticket o historia, por ejemplo: "Cambio menor validado. Se autoriza pase a producción".

## Sustento Documental

| Documento | Sustento |
|-----------|----------|
| DIR-GST-TI | Gestión de solicitudes, trazabilidad y atención mediante Mesa de Servicios |
| PRO-CAM-TI | Cambio menor, no requiere aprobación formal previa, validación proporcional |
| FOR-CAM-TI | Formato de Cambio o campos equivalentes en el ticket |
| PRO-DES-TI | Registro de requerimiento, validación técnica o funcional, Anexo B - Evidencias Aceptadas y cierre |
| EST-DES-TI | Validaciones o pruebas proporcionales a complejidad, riesgo e impacto |
| FOR-REQ-TI / FOR-PRU-TI / FOR-DES-TI | Formatos opcionales; pueden reemplazarse por campos equivalentes en el ticket |

## Cierre Esperado

El caso se considera cerrado cuando:

- El filtro fue implementado.
- Existe evidencia simple del resultado.
- El usuario o responsable dio conformidad cuando corresponde.
- El ticket fue cerrado con descripción del cambio.

## Evidencia Mínima Para Auditoría

- Ticket o requerimiento.
- FOR-CAM-TI - Formato de Cambio, con datos mínimos, o campos equivalentes en el ticket.
- Descripción del filtro solicitado.
- Registro del cambio realizado.
- Captura, conformidad o validación simple.
- Autorización de pase a producción, cuando aplique.
- Cierre del ticket.

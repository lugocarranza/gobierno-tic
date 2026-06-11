# CASO 02: Cambio Menor - Filtro en Bandeja de Solicitudes

## Objetivo del Caso

Mostrar como documentar un requerimiento menor de desarrollo sin generar aprobaciones innecesarias.

## Escenario

El area usuaria solicita agregar un filtro por estado en la bandeja de solicitudes para facilitar la busqueda de registros.

El cambio no modifica reglas de negocio, calculos, datos historicos, permisos, integraciones ni procesos criticos.

## Clasificacion

| Elemento | Valor |
|----------|-------|
| Tipo de atencion | Requerimiento |
| Tipo de cambio | Cambio menor |
| Proceso principal | Desarrollo y gestion de cambios |
| Riesgo referencial | Bajo |
| Aprobacion requerida | No requiere aprobacion formal previa |

## Documentos Finales en Jira o Historia de Usuario

Al cierre del ticket Kanban, historia de usuario en sprint de Jira o herramienta equivalente, deberian figurar:

| Documento o evidencia final | Puede estar como | Sustento |
|-----------------------------|------------------|----------|
| Ticket, requerimiento o historia de usuario | Registro principal en Jira o Mesa de Servicios | PRO-DES-TI / DIR-GST-TI |
| Anexo B - Formato de Cambio | Campos del ticket, comentario estructurado o adjunto | PRO-CAM-TI |
| Registro de implementacion | Commit, comentario tecnico, bitacora o enlace a repositorio | PRO-DES-TI / EST-DES-TI |
| Validacion simple | Captura, comentario de conformidad o revision funcional | PRO-CAM-TI / PRO-DES-TI |
| Guia breve, captura comentada o actualizacion de instructivo | Solo si el filtro cambia la forma de uso habitual o requiere comunicacion al usuario | PRO-DES-TI / EST-DES-TI |
| Autorizacion de pase a produccion | Comentario en el mismo ticket o historia | PRO-CAM-TI / PRO-DES-TI |
| Fecha real de implementacion | Comentario en ticket, registro de despliegue o cierre tecnico | PRO-CAM-TI |
| Cierre | Estado cerrado con resumen del resultado | DIR-GST-TI |

## Documentos o Evidencias Recibidas

| Momento | Evidencia recibida | Responsable sugerido | Para que sirve |
|---------|--------------------|----------------------|----------------|
| Inicio | Ticket, correo o requerimiento del area usuaria | Usuario solicitante | Identifica la necesidad |
| Analisis | Descripcion simple del filtro requerido | Usuario solicitante / Desarrollador | Delimita el alcance |
| Analisis | Pantalla o referencia de la bandeja actual, si existe | Usuario solicitante / Desarrollador | Ayuda a validar el resultado |

## Documentos o Evidencias Generadas

| Momento | Evidencia generada | Responsable sugerido | Conservacion sugerida |
|---------|--------------------|----------------------|-----------------------|
| Registro | Ticket o registro del requerimiento | Mesa de Servicios / Coordinacion TIC | Herramienta de seguimiento |
| Analisis | Anexo B - Formato de Cambio, llenado con datos minimos | Responsable tecnico | Ticket o documento adjunto |
| Analisis | Confirmacion de que es cambio menor | Responsable tecnico | Anexo B o comentario en ticket |
| Implementacion | Registro del cambio realizado en repositorio o bitacora | Desarrollador | Repositorio o ticket |
| Validacion | Captura del filtro implementado o resultado de revision | Desarrollador / Usuario solicitante | Ticket |
| Documentacion | Guia breve, captura comentada o instructivo actualizado, si corresponde | Desarrollador / Usuario solicitante | Ticket, correo o repositorio documental |
| Pase a produccion | Autorizacion de pase en el mismo ticket o comentario | Coordinacion TIC | Ticket o historia de usuario |
| Cierre | Conformidad simple o cierre del ticket | Usuario solicitante / Coordinacion TIC | Ticket o correo |

## Flujo Sugerido

```text
Solicitud
|
Registro del requerimiento
|
Clasificacion como cambio menor
|
Registro minimo del Anexo B
|
Implementacion
|
Validacion simple
|
Autorizacion de pase en el mismo ticket
|
Cierre
```

## Llenado Referencial del Anexo B

| Campo | Ejemplo |
|-------|---------|
| Codigo o Ticket | TIC-REQ-0001 |
| Fecha | Fecha de registro del ticket |
| Solicitante | Area usuaria responsable de la bandeja |
| Responsable Tecnico | Desarrollador asignado |
| Descripcion del Cambio | Agregar filtro por estado en la bandeja de solicitudes |
| Justificacion | Facilitar la busqueda y seguimiento de solicitudes |
| Riesgo | Bajo |
| Tipo de Cambio | Menor |
| Plan de Reversion | Retirar el filtro o restaurar version anterior del componente |

El Anexo B puede registrarse dentro del mismo ticket si la herramienta permite capturar estos campos.

La fecha real de implementacion, validacion y conformidad no requieren reenviar el Anexo B completo. Pueden quedar como comentarios, capturas, correo o cierre del ticket.

## Validacion Esperada

Para este tipo de cambio basta una evidencia simple, por ejemplo:

- Captura de la bandeja con el nuevo filtro.
- Comentario del usuario indicando conformidad.
- Resultado de revision funcional simple.
- Cierre del ticket con descripcion del cambio.

No se requieren pruebas unitarias obligatorias ni aprobacion formal previa.

El manual de usuario o instructivo no es obligatorio para todo cambio menor. Se actualiza solo cuando el ajuste modifica la forma en que el usuario opera el sistema o cuando se necesita comunicar el nuevo uso; en ese caso puede bastar una captura comentada, una guia breve o un comentario instructivo en el ticket.

La autorizacion del pase a produccion puede registrarse en el mismo ticket o historia, por ejemplo: "Cambio menor validado. Se autoriza pase a produccion".

## Sustento Documental

| Documento | Sustento |
|-----------|----------|
| DIR-GST-TI | Gestion de solicitudes, trazabilidad y atencion mediante Mesa de Servicios |
| PRO-CAM-TI | Cambio menor, Anexo B - Formato de Cambio, no requiere aprobacion formal previa, validacion proporcional |
| PRO-DES-TI | Registro de requerimiento, validacion tecnica o funcional, Anexo B - Evidencias Aceptadas y cierre |
| EST-DES-TI | Validaciones o pruebas proporcionales a complejidad, riesgo e impacto |

## Cierre Esperado

El caso se considera cerrado cuando:

- El filtro fue implementado.
- Existe evidencia simple del resultado.
- El usuario o responsable dio conformidad cuando corresponde.
- El ticket fue cerrado con descripcion del cambio.

## Evidencia Minima Para Auditoria

- Ticket o requerimiento.
- Anexo B - Formato de Cambio, con datos minimos.
- Descripcion del filtro solicitado.
- Registro del cambio realizado.
- Captura, conformidad o validacion simple.
- Autorizacion de pase a produccion, cuando aplique.
- Cierre del ticket.

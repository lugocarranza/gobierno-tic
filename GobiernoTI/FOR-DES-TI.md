# FOR-DES-TI - FORMATO DE DESPLIEGUE DE SOFTWARE

## 1. Datos Generales

| Campo | Valor |
|---------|---------|
| Ticket(s) o requerimiento(s) incluidos | |
| Sistema o servicio | |
| Ambiente | Producción / Pruebas / Otro |
| Responsable del despliegue | |
| Fecha programada | |
| Autorización de pase a producción | Ticket / correo / comentario / acta / otro |

## 2. Descripción del Despliegue

Describir brevemente los cambios, componentes o versiones que serán implementados.

## 3. Componentes a Desplegar

### 3.1 Aplicación

| Componente o archivo | Versión / referencia |
|----------------------|----------------------|
| | |

### 3.2 Base de Datos

| Script | Tipo | Requiere respaldo o reversa |
|----------|----------|----------------------------|
| | DDL / DML / Otro | Sí / No |

### 3.3 Configuración u Otros Componentes

| Elemento | Descripción |
|------------|-------------|
| | |

## 4. Respaldo Previo

| Aspecto | Detalle |
|----------|---------|
| ¿Requiere respaldo previo? | Sí / No |
| Evidencia o ubicación del respaldo | |
| Responsable | |

## 5. Procedimiento de Despliegue

| N° | Paso | Responsable | Observación previa / referencia |
|----|------|-------------|---------------------------------|
| 1 | | | |
| 2 | | | |

## 6. Plan de Reversión

Indicar cómo se retornará al estado anterior si el despliegue presenta fallas.

| N° | Paso de reversión | Responsable | Observación |
|----|-------------------|-------------|-------------|
| 1 | | | |
| 2 | | | |

## Nota Posterior al Pase

Los datos generados después de ejecutar el pase, como día y hora efectiva, comprobaciones realizadas, comunicaciones enviadas, resultado obtenido o incidencias, deberán registrarse luego en el ticket, comentario, bitácora, registro de despliegue, cierre técnico o medio equivalente.

## Uso del Formato

Este formato es referencial y se utiliza para preparar o consolidar la información necesaria antes de ejecutar un pase a producción o despliegue coordinado.

Se recomienda cuando el despliegue agrupe varios cambios, requiera una ventana coordinada, incluya scripts, respaldo previo, plan de reversión, comunicación a usuarios o coordinación especial. Cuando exista ventana coordinada, podrá indicarse en la descripción del despliegue o en el ticket.

El contenido mínimo podrá registrarse en este documento, en Jira, Mesa de Servicios, correo institucional, comentario estructurado, bitácora, registro de despliegue o medio equivalente. No es obligatorio crear un registro separado de despliegue si el ticket o historia contiene la información suficiente.

Este formato no reemplaza la aprobación del cambio ni la autorización del pase a producción; dichas evidencias deberán constar en el ticket, correo, comentario, acta, registro de despliegue o documento equivalente.

## Ejemplo Orientador

Si el pase a producción corresponde a un cambio menor o a un único ticket sin coordinación especial, la preparación del despliegue puede quedar registrada mediante un comentario en el mismo ticket, siempre que indique fecha programada, responsable, componentes a implementar y referencia a la autorización del pase.

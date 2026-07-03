---
codigo: PRO-CAM-TI
titulo: Procedimiento de Gestión de Cambios
version: 1.0
tipo: Procedimiento
responsable: Coordinación de Tecnologías de Información
estado: Vigente
---

# PROCEDIMIENTO DE GESTIÓN DE CAMBIOS

## 1. FINALIDAD

Establecer el procedimiento para controlar la implementación de cambios en los sistemas de información, infraestructura tecnológica, bases de datos y servicios digitales administrados por el Fondo de Inclusión Social Energético (FISE), minimizando los riesgos operativos y garantizando la trazabilidad de las modificaciones realizadas.

## 2. OBJETIVO

Asegurar que todo cambio tecnológico sea evaluado, autorizado, implementado y documentado de manera controlada.

## 3. ALCANCE

Aplica a:

- Sistemas institucionales.
- Aplicaciones desarrolladas o mantenidas por el FISE.
- Bases de datos.
- Infraestructura tecnológica.
- Redes y comunicaciones.
- Servicios en la nube.
- Componentes de seguridad informática.

## 4. DEFINICIONES

### Cambio

Modificación planificada sobre un sistema, servicio, infraestructura o componente tecnológico.

### Cambio Menor

Cambio de bajo riesgo, impacto limitado y complejidad reducida. No requiere aprobación formal previa, pero deberá quedar registrado y contar con validación o conformidad cuando corresponda.

**Ejemplos:**

- Ajustes de textos.
- Nuevas fotografías o imágenes.
- Nuevos reportes simples.
- Nuevos campos sin impacto crítico.
- Ajustes menores de interfaz.
- Configuraciones menores.

### Cambio Mayor

Cambio con impacto funcional, operativo, contable, tecnológico, de seguridad o de datos relevante.

**Ejemplos:**

- Nuevos procesos.
- Modificaciones de liquidación.
- Integraciones entre sistemas.
- Cambios contables.
- Modificación masiva de datos.
- Cambio de arquitectura.
- Migración de servidores.
- Cambio de motor de base de datos.

### Cambio de Emergencia

Cambio requerido para restablecer un servicio crítico, atender un incidente de seguridad o mitigar un riesgo operativo inmediato.

## 5. ROLES Y RESPONSABILIDADES

### 5.1 Solicitante

Responsable de:

- Identificar la necesidad.
- Sustentar el requerimiento.
- Validar el resultado cuando corresponda.

### 5.2 Responsable Técnico

Responsable de:

- Evaluar el cambio.
- Estimar riesgos.
- Implementar el cambio.
- Documentar evidencias.

### 5.3 Coordinación TIC o responsable designado de TIC

Responsable de:

- Aprobar cambios.
- Autorizar despliegues a producción.
- Supervisar la ejecución.
- Gestionar excepciones.

## 6. POLÍTICAS GENERALES

### 6.1

Todo cambio deberá estar asociado a un ticket, requerimiento, incidente o necesidad formalmente identificada.

### 6.2

Los cambios se clasificarán como menores, mayores o de emergencia, considerando impacto, riesgo, urgencia, criticidad y alcance.

### 6.3

Los cambios deberán realizarse preferentemente en ambientes distintos al de producción antes de su despliegue.

### 6.4

Todo cambio deberá contar con una validación proporcional a su impacto.

### 6.5

Cuando el cambio implique riesgos significativos o sea clasificado como cambio mayor, deberá definirse un mecanismo de reversión.

### 6.6

No se realizarán cambios directos en producción sin autorización de la Coordinación TIC o responsable designado de TIC, salvo situaciones de emergencia.

### 6.7

La gestión de cambios no requiere la constitución de un comité permanente. Los cambios mayores deberán contar con aprobación formal proporcional al impacto, en la que participen la Coordinación TIC o responsable designado de TIC, el responsable técnico y el área usuaria o responsable funcional cuando corresponda.

## 7. PROCEDIMIENTO DE GESTIÓN DE CAMBIOS

### 7.1 Solicitud

El cambio podrá originarse por:

- Requerimiento de usuario.
- Proyecto.
- Incidente.
- Problema identificado.
- Necesidad técnica.

La solicitud deberá registrarse mediante:

- Mesa de Servicios.
- Jira.
- Correo electrónico institucional.
- Documento interno.

### 7.2 Evaluación

El responsable técnico evaluará:

- Alcance.
- Impacto.
- Riesgo.
- Dependencias.
- Necesidad de reversión.
- Tipo de cambio.

### 7.3 Aprobación

La aprobación se realizará de acuerdo con el tipo de cambio:

| Tipo de cambio | Aprobación mínima |
|----------------|-------------------|
| Cambio menor | No requiere aprobación formal previa. Debe quedar registrado y contar con validación o conformidad cuando corresponda. |
| Cambio mayor | Coordinación TIC o responsable designado de TIC, responsable técnico y área usuaria o responsable funcional. |
| Cambio de emergencia | Autorización rápida de Coordinación TIC o responsable designado de TIC, con regularización posterior. |

Cuando el cambio mayor tenga impacto institucional significativo, presupuestal, contractual, contable, de seguridad o continuidad operativa, podrá requerirse aprobación de Dirección Ejecutiva u otras áreas competentes.

La aprobación podrá realizarse mediante:

- Ticket.
- Correo electrónico.
- Acta.
- Documento interno.

Cuando la aprobación o autorización sea realizada por un responsable designado de TIC, la designación o autorización deberá quedar registrada en ticket, correo, comentario, acta o registro equivalente.

La aprobación del cambio y la autorización del pase a producción son controles distintos. La aprobación del cambio confirma que el cambio puede ejecutarse; la autorización del pase a producción confirma que uno o más cambios validados pueden implementarse en producción.

Ambas evidencias podrán registrarse en el mismo ticket, historia de usuario, correo electrónico, comentario o documento equivalente. No se requiere crear un ticket separado únicamente para autorizar el pase a producción.

### 7.4 Implementación

Una vez aprobado el cambio:

- Se realizará el desarrollo o configuración.
- Se ejecutarán validaciones o pruebas según corresponda.
- Se prepararán los componentes para despliegue.

### 7.5 Validación

Previo al pase a producción deberá existir evidencia de validación técnica o funcional, proporcional al tipo, riesgo e impacto del cambio.

Para cambios menores bastará una validación simple o evidencia equivalente.

Para cambios mayores deberá conservarse evidencia de validación técnica o funcional.

En cambios de emergencia, la evidencia podrá regularizarse posteriormente.

Las evidencias podrán consistir en:

- Capturas de pantalla.
- Correos de conformidad.
- Registro de validaciones o pruebas.
- Validación del usuario responsable.

### 7.6 Pase a Producción

La implementación en producción deberá ser autorizada por la Coordinación TIC o responsable designado de TIC.

La autorización del pase a producción podrá corresponder a un cambio individual o a un conjunto de cambios validados. Cuando el pase agrupe varios cambios, deberá indicarse la relación de tickets, historias o requerimientos incluidos.

La autorización podrá registrarse en el mismo ticket del cambio, historia de usuario, correo electrónico, comentario, registro de despliegue o documento equivalente.

El uso de un ticket o registro específico de despliegue será opcional y se recomienda cuando el pase agrupe múltiples cambios, requiera una ventana coordinada, comunicación a usuarios, respaldo previo o plan de reversión.

Cuando resulte útil para preparar o consolidar la información del pase antes de ejecutarlo, podrá utilizarse el FOR-DES-TI - Formato de Despliegue de Software, o un registro equivalente. Su uso no crea la obligación de abrir un ticket separado de despliegue si el ticket del cambio, historia, correo, comentario o registro existente contiene la información suficiente.

Cuando corresponda deberá realizarse:

- Respaldo previo.
- Ventana de implementación.
- Comunicación a usuarios afectados.
- Plan de reversión para cambios mayores o de riesgo significativo.

### 7.7 Cierre

El cambio se considerará concluido cuando:

- Se encuentre implementado.
- Exista conformidad funcional o técnica, cuando corresponda.
- Se registren las evidencias correspondientes.

## 8. CAMBIOS DE EMERGENCIA

### 8.1 Aplicación

Podrán ejecutarse cuando:

- Exista interrupción de un servicio crítico.
- Se presente un incidente de seguridad.
- Exista riesgo operativo significativo.

### 8.2 Aprobación

La autorización podrá otorgarse mediante:

- Correo electrónico.
- Comunicación verbal.
- Mensaje institucional.

La documentación deberá regularizarse posteriormente.

### 8.3 Registro

Todo cambio de emergencia deberá quedar documentado una vez restablecida la operación.

La regularización deberá incluir, como mínimo, la justificación, responsable, acciones ejecutadas, resultado obtenido y evidencia de validación.

## 9. PLAN DE REVERSIÓN

Cuando el riesgo lo justifique, el cambio deberá contar con un mecanismo de reversión que permita restaurar la situación anterior en caso de falla.

Podrá consistir en:

- Restauración de respaldos.
- Despliegue de versión anterior.
- Reversión de scripts.
- Restauración de configuraciones.

## 10. EVIDENCIAS MÍNIMAS

Todo cambio deberá conservar, según corresponda:

| Evidencia | Obligatoria |
|------------|-------------|
| Solicitud o requerimiento | Sí |
| Evaluación técnica | Sí |
| Aprobación del cambio | Según tipo de cambio; el cambio menor no requiere aprobación formal previa |
| Evidencia de validación o pruebas | Según tipo, riesgo e impacto |
| Evidencia de despliegue | Sí |
| Autorización de pase a producción | Sí, cuando aplique despliegue |
| Conformidad funcional o técnica | Sí, cuando corresponda |
| Plan de reversión | Según riesgo / obligatorio para cambios mayores cuando corresponda |
| Comunicación a usuarios afectados | Según impacto |

## 11. INDICADORES

La Coordinación TIC o responsable designado de TIC podrá monitorear:

- Cambios implementados.
- Cambios exitosos.
- Cambios revertidos.
- Cambios de emergencia.
- Incidentes posteriores al cambio.

## 12. VIGENCIA

El presente procedimiento entra en vigencia a partir de su aprobación.

# ANEXO A

## Flujo Simplificado

```text
Solicitud
↓
Evaluación Técnica
↓
Aprobación
↓
Implementación
↓
Validación
↓
Pase a Producción
↓
Cierre
```

# ANEXO B

## Formato de Cambio

Podrá utilizarse el FOR-CAM-TI - Formato de Cambio, o campos equivalentes en ticket, Jira, correo, comentario estructurado o documento interno.

El formato es referencial y sirve como registro inicial o evaluación del cambio. No reemplaza la aprobación del cambio, la autorización del pase a producción, la evidencia de validación, la evidencia de despliegue ni el cierre del cambio.

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

### Cambio Estándar

Cambio recurrente, de bajo riesgo y previamente autorizado.

**Ejemplos:**

- Actualización de catálogos.
- Configuraciones menores.
- Reinicio programado de servicios.

### Cambio Normal

Cambio que requiere evaluación y aprobación previa.

**Ejemplos:**

- Nuevas funcionalidades.
- Modificaciones de procesos.
- Cambios en bases de datos.
- Integraciones entre sistemas.

### Cambio de Emergencia

Cambio requerido para restablecer un servicio crítico o mitigar un incidente grave.

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

### 5.3 Coordinación TIC

Responsable de:

- Aprobar cambios.
- Autorizar despliegues a producción.
- Supervisar la ejecución.
- Gestionar excepciones.

## 6. POLÍTICAS GENERALES

### 6.1

Todo cambio deberá estar asociado a un ticket, requerimiento, incidente o necesidad formalmente identificada.

### 6.2

Los cambios deberán realizarse preferentemente en ambientes distintos al de producción antes de su despliegue.

### 6.3

Todo cambio deberá contar con evidencia mínima de validación.

### 6.4

Cuando el cambio implique riesgos significativos, deberá definirse un mecanismo de reversión.

### 6.5

No se realizarán cambios directos en producción sin autorización de la Coordinación TIC, salvo situaciones de emergencia.

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

### 7.3 Aprobación

Los cambios normales deberán ser aprobados por la Coordinación TIC.

La aprobación podrá realizarse mediante:

- Ticket.
- Correo electrónico.
- Acta.
- Documento interno.

### 7.4 Implementación

Una vez aprobado el cambio:

- Se realizará el desarrollo o configuración.
- Se ejecutarán pruebas.
- Se prepararán los componentes para despliegue.

### 7.5 Validación

Previo al pase a producción deberá existir evidencia de validación técnica o funcional.

Las evidencias podrán consistir en:

- Capturas de pantalla.
- Correos de conformidad.
- Registro de pruebas.
- Validación del usuario responsable.

### 7.6 Pase a Producción

La implementación en producción deberá ser autorizada por la Coordinación TIC.

Cuando corresponda deberá realizarse:

- Respaldo previo.
- Ventana de implementación.
- Comunicación a usuarios afectados.

### 7.7 Cierre

El cambio se considerará concluido cuando:

- Se encuentre implementado.
- Exista conformidad funcional o técnica.
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
| Aprobación | Sí |
| Evidencia de pruebas | Sí |
| Evidencia de despliegue | Sí |
| Conformidad funcional o técnica | Sí |

## 11. INDICADORES

La Coordinación TIC podrá monitorear:

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

## Formato Simplificado de Cambio

### Información General

- Código o Ticket
- Fecha
- Solicitante
- Responsable Técnico

### Descripción del Cambio

### Justificación

### Riesgo

- Bajo
- Medio
- Alto

### Plan de Reversión

### Resultado de Pruebas

### Fecha de Implementación

### Conformidad
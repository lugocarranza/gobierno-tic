---
codigo: PRO-RES-TI
titulo: Procedimiento de Gestión de Respaldos y Recuperación de Información
version: 1.0
tipo: Procedimiento
responsable: Coordinación de Tecnologías de Información
estado: Vigente
---

# PROCEDIMIENTO DE GESTIÓN DE RESPALDOS Y RECUPERACIÓN DE INFORMACIÓN

## 1. FINALIDAD

Establecer las actividades mínimas para la generación, conservación y recuperación de respaldos de información administrada por el Fondo de Inclusión Social Energético (FISE), con la finalidad de reducir el riesgo de pérdida de información y facilitar la recuperación de los servicios tecnológicos cuando sea necesario.

## 2. OBJETIVO

Garantizar la disponibilidad de copias de respaldo de la información institucional crítica y establecer mecanismos básicos para su recuperación ante fallas operativas, errores humanos o incidentes tecnológicos.

## 3. ALCANCE

Aplica a:

- Bases de datos institucionales.
- Sistemas de información.
- Servidores de aplicaciones.
- Archivos institucionales administrados por la Coordinación TIC.
- Configuraciones críticas de infraestructura tecnológica.

## 4. DEFINICIONES

### Respaldo

Copia de información realizada con el propósito de permitir su recuperación posterior.

### Recuperación

Proceso mediante el cual se restaura información previamente respaldada.

### Restauración

Actividad técnica destinada a recuperar información a partir de un respaldo disponible.

## 5. ROLES Y RESPONSABILIDADES

### 5.1 Coordinación de Tecnologías de Información

Responsable de:

- Definir los mecanismos de respaldo.
- Supervisar la ejecución de respaldos.
- Mantener evidencias de ejecución.
- Coordinar actividades de recuperación cuando corresponda.

### 5.2 Responsable de Base de Datos

Responsable de:

- Ejecutar o supervisar los respaldos de bases de datos.
- Verificar la disponibilidad de los archivos generados.
- Ejecutar restauraciones cuando sean requeridas.

### 5.3 Administradores de Sistemas

Responsables de:

- Ejecutar respaldos de servidores o aplicaciones bajo su administración.
- Informar cualquier falla detectada.

## 6. POLÍTICAS GENERALES

### 6.1

La información considerada crítica deberá contar con mecanismos de respaldo periódicos.

### 6.2

Los respaldos deberán almacenarse en medios o ubicaciones diferentes al entorno operativo principal cuando ello resulte técnicamente posible.

### 6.3

La Coordinación TIC deberá conservar evidencia de la ejecución de los respaldos.

### 6.4

La recuperación de información deberá ser autorizada por la Coordinación TIC o por el responsable funcional correspondiente.

### 6.5

Los respaldos deberán protegerse contra accesos no autorizados.

### 6.6
Los respaldos asociados a servicios o sistemas críticos deberán ser verificados periódicamente mediante pruebas de recuperación, cuando resulte técnica y operativamente viable.
Como mínimo, se procurará realizar una prueba de recuperación anual sobre al menos uno de los servicios o sistemas críticos administrados por el FISE.
Las pruebas efectuadas y sus resultados deberán conservarse como evidencia.

## 7. RESPALDOS

### 7.1 Información Comprendida

Como mínimo deberán considerarse:

- Bases de datos institucionales.
- Configuraciones críticas de servidores.
- Archivos institucionales administrados por TIC.
- Aplicaciones y componentes tecnológicos que la Coordinación TIC determine.

### 7.2 Frecuencia Referencial

| Tipo de Información | Frecuencia Referencial |
|---------------------|------------------------|
| Bases de datos institucionales | Diaria |
| Archivos institucionales | Semanal |
| Configuraciones críticas | Cuando existan cambios relevantes |
| Aplicaciones y sistemas | Según necesidad operativa |

La frecuencia podrá ajustarse según las necesidades operativas o capacidades tecnológicas disponibles.

### 7.3 Conservación

Los respaldos deberán conservarse por el tiempo que determine la Coordinación TIC de acuerdo con la criticidad de la información y la capacidad disponible.

## 8. VERIFICACIÓN

La Coordinación TIC realizará verificaciones periódicas para confirmar que los respaldos se estén generando correctamente.

Las verificaciones podrán realizarse mediante:

- Revisión de registros.
- Validación de archivos generados.
- Confirmación de tareas programadas.

## 9. RECUPERACIÓN DE INFORMACIÓN

### 9.1 Casos Aplicables

La recuperación podrá realizarse ante:

- Eliminación accidental de información.
- Corrupción de datos.
- Fallas de software.
- Fallas de infraestructura.
- Incidentes de seguridad.
- Otras situaciones que afecten la disponibilidad de la información.

### 9.2 Solicitud

La recuperación deberá ser solicitada por:

- Usuario responsable de la información.
- Responsable funcional.
- Coordinación TIC.

### 9.3 Restauración

La restauración deberá realizarse utilizando el respaldo más adecuado disponible, procurando minimizar el impacto sobre la operación institucional.

### 9.4 Validación

Luego de la restauración se verificará:

- Integridad de la información.
- Disponibilidad de los datos recuperados.
- Correcto funcionamiento del servicio afectado.

## 10. PRUEBAS DE RECUPERACIÓN

La Coordinación TIC realizará al menos una prueba de recuperación anual sobre información o servicios críticos.

Cuando no resulte técnica u operativamente viable ejecutar una prueba completa, podrá realizarse una verificación parcial o documentarse la limitación correspondiente.

Las pruebas podrán consistir en:

- Restauración de bases de datos.
- Recuperación de archivos.
- Verificación de respaldos seleccionados.
- Restauración parcial en un ambiente controlado.

La prueba o verificación deberá dejar evidencia del alcance, fecha, responsable, resultado y observaciones identificadas.

## 11. EVIDENCIAS

Como mínimo se conservarán:

- Registros de ejecución de respaldos.
- Archivos de log.
- Capturas de verificación.
- Solicitudes de recuperación.
- Evidencias de restauración realizadas.
- Evidencias de pruebas o verificaciones de recuperación.
- Excepciones o limitaciones documentadas cuando corresponda.

## 12. EXCEPCIONES

Cuando existan limitaciones técnicas, presupuestales o contractuales que impidan aplicar alguna disposición del presente procedimiento, la Coordinación TIC podrá definir mecanismos alternativos razonables que permitan reducir el riesgo asociado.

## 13. VIGENCIA

El presente procedimiento entra en vigencia a partir de su aprobación.

# ANEXO A

## Resumen de Responsabilidades

| Actividad | Responsable |
|------------|-------------|
| Definir respaldos | Coordinación TIC |
| Ejecutar respaldos BD | Responsable BD |
| Ejecutar respaldos de sistemas | Administrador correspondiente |
| Verificar respaldos | Coordinación TIC |
| Autorizar recuperación | Coordinación TIC / Responsable funcional |
| Ejecutar restauración | Responsable técnico |

# ANEXO B

## Evidencias Aceptadas

Se consideran evidencias válidas:

- Registros automáticos de respaldo.
- Logs de ejecución.
- Correos electrónicos.
- Tickets.
- Capturas de pantalla.
- Informes técnicos.

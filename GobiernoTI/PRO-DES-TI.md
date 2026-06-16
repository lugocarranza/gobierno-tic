---
codigo: PRO-DES-TI
titulo: Procedimiento de Desarrollo y Mantenimiento de Software
version: 1.0
tipo: Procedimiento
responsable: Coordinación de Tecnologías de Información
estado: Vigente
---

# PROCEDIMIENTO DE DESARROLLO Y MANTENIMIENTO DE SOFTWARE

## 1. FINALIDAD

Establecer el procedimiento para la atención de requerimientos, desarrollo, mantenimiento, validación y despliegue de software administrado por el Fondo de Inclusión Social Energético (FISE), garantizando la trazabilidad y calidad mínima de las soluciones implementadas.

## 2. OBJETIVO

Asegurar que todo desarrollo o modificación de software sea gestionado de manera controlada, documentada y alineada a las necesidades institucionales.

## 3. ALCANCE

Aplica a:

- Nuevos desarrollos.
- Mantenimientos correctivos.
- Mantenimientos evolutivos.
- Integraciones entre sistemas.
- Reportes y consultas especializadas.
- Ajustes de bases de datos asociados a aplicaciones.

Comprende los sistemas institucionales administrados por el FISE.

## 4. DOCUMENTOS RELACIONADOS

- Directiva de Gestión de Servicios TI.
- Directiva de Seguridad de la Información.
- Estándares de Código Fuente.
- Estándares de Base de Datos.
- Procedimiento de Gestión de Cambios.

## 5. ROLES Y RESPONSABILIDADES

### 5.1 Usuario Solicitante

Responsable de:

- Identificar la necesidad.
- Proporcionar información funcional.
- Validar el resultado obtenido.

### 5.2 Coordinación TIC

Responsable de:

- Priorizar requerimientos.
- Asignar responsables.
- Autorizar el pase a producción cuando corresponda.

### 5.3 Analista / Desarrollador

Responsable de:

- Analizar la solicitud.
- Realizar el desarrollo.
- Documentar los cambios.
- Ejecutar pruebas técnicas.

### 5.4 Usuario Responsable del Proceso

Responsable de:

- Ejecutar pruebas funcionales.
- Validar los resultados.
- Brindar conformidad para producción.

## 6. POLÍTICAS GENERALES

### 6.1

Todo desarrollo deberá originarse a partir de un requerimiento formal.

### 6.2

Todo desarrollo deberá estar registrado en la herramienta institucional de seguimiento (Mesa de Servicios, Jira u otra).

### 6.3

No se realizarán cambios directos en producción sin autorización previa, salvo incidentes de emergencia debidamente justificados.

### 6.4

Todo código fuente deberá almacenarse en el repositorio institucional.

### 6.5

Todo despliegue deberá contar con evidencia mínima de validación o pruebas, según la complejidad, riesgo e impacto del cambio.

## 7. CICLO DE DESARROLLO

### 7.1 Registro del Requerimiento

El requerimiento podrá originarse mediante:

- Ticket.
- Correo electrónico.
- Memorando.
- Documento funcional.
- Acta de reunión.

La solicitud deberá indicar como mínimo:

- Necesidad identificada.
- Objetivo.
- Usuario responsable.
- Prioridad.

Para desarrollos nuevos, mejoras significativas o cambios funcionales relevantes, podrá utilizarse el FOR-REQ-TI - Formato Referencial de Especificación de Requerimientos, o campos equivalentes en Jira, Mesa de Servicios, correo, historia de usuario o documento similar. Para requerimientos simples bastará que el registro principal contenga la información mínima necesaria.

### 7.2 Análisis

El responsable técnico evaluará:

- Alcance.
- Impacto.
- Complejidad.
- Riesgos.
- Dependencias.

Cuando corresponda podrá elaborarse una especificación funcional simplificada.

### 7.3 Desarrollo

El desarrollo deberá realizarse siguiendo los estándares institucionales vigentes.

Podrá incluir:

- Desarrollo de software.
- Ajustes de base de datos.
- Integraciones.
- Reportes.
- Automatizaciones.

### 7.4 Validación Técnica

El desarrollador verificará, según corresponda:

- Funcionamiento correcto.
- Integridad de datos.
- Manejo de errores.
- Compatibilidad con procesos existentes.

Para cambios simples o de bajo impacto, la validación podrá consistir en una revisión funcional básica, revisión visual, captura de pantalla, resultado de ejecución o evidencia equivalente.

La evidencia podrá consistir en:

- Capturas de pantalla.
- Resultados de ejecución.
- Registro de validaciones o pruebas.
- Videos.
- Correos electrónicos.

Cuando existan varios escenarios de validación, riesgo medio o alto, impacto funcional relevante o evidencia técnica que convenga consolidar, podrá utilizarse el FOR-PRU-TI - Formato Referencial de Evidencia de Validación o Pruebas, o un registro equivalente en la herramienta institucional.

### 7.5 Validación Funcional

El usuario responsable validará, cuando corresponda:

- Cumplimiento del requerimiento.
- Resultados esperados.
- Operatividad del proceso.

La conformidad podrá otorgarse mediante:

- Correo electrónico.
- Ticket.
- Acta.
- Documento de conformidad.

### 7.6 Pase a Producción

Una vez obtenida la validación o conformidad que corresponda:

- Se programará el despliegue.
- Se ejecutarán los cambios autorizados.
- Se registrará la fecha de implementación.

La autorización del pase a producción podrá registrarse en el mismo ticket, historia de usuario, correo, comentario o documento equivalente. Cuando un despliegue agrupe varios cambios o historias, podrá utilizarse un registro o ticket de despliegue que indique los cambios incluidos, responsable, fecha o ventana de implementación y evidencias de validación.

El FOR-DES-TI - Formato Referencial de Despliegue de Software podrá utilizarse para preparar o consolidar la información del pase antes de ejecutarlo, especialmente cuando el despliegue agrupe varios cambios, tenga ventana coordinada, incluya scripts, respaldo previo, plan de reversión, comunicación a usuarios o coordinación especial. No será obligatorio crear un formato separado si el ticket, historia, correo, comentario o registro equivalente contiene la información suficiente.

Los datos generados después de ejecutar el pase, como día y hora efectiva, comprobaciones realizadas, comunicaciones enviadas y resultado obtenido, podrán registrarse luego en el ticket, comentario, bitácora, registro de despliegue o cierre técnico.

Cuando corresponda, se realizará respaldo previo.

### 7.7 Cierre

La solicitud se considerará concluida cuando:

- El cambio se encuentre en producción.
- Exista conformidad funcional o técnica, cuando corresponda.
- Se registren las evidencias correspondientes.

## 8. MANTENIMIENTO CORRECTIVO

Corresponde a la corrección de errores que afecten el funcionamiento de una aplicación.

Las correcciones seguirán el mismo flujo definido en el presente procedimiento.

Cuando la urgencia lo justifique podrán aplicarse mecanismos abreviados de aprobación.

## 9. MANTENIMIENTO EVOLUTIVO

Corresponde a mejoras, optimizaciones o nuevas funcionalidades solicitadas por los usuarios.

Su implementación seguirá el ciclo completo establecido en este procedimiento.

## 10. CAMBIOS DE EMERGENCIA

Cuando un incidente crítico requiera una atención inmediata:

- Se podrá ejecutar el cambio con autorización verbal o por correo.
- La regularización documental deberá completarse posteriormente.

## 11. EVIDENCIAS MÍNIMAS

Todo desarrollo deberá conservar, como mínimo:

| Evidencia | Obligatoria |
|------------|-------------|
| Requerimiento | Sí |
| Registro del ticket | Sí |
| Código fuente | Sí |
| Evidencia de validación o pruebas | Según complejidad, riesgo e impacto |
| Conformidad funcional | Sí, cuando corresponda según tipo, riesgo e impacto |
| Manual de usuario, guía o instructivo actualizado | Cuando el cambio modifique la forma de uso del sistema |
| Documento técnico o arquitectura simplificada | Cuando el desarrollo o mejora sea significativo |
| Evidencia de despliegue | Sí |
| Autorización de pase a producción | Sí, cuando aplique despliegue |

## 12. INDICADORES

La Coordinación TIC podrá monitorear:

- Requerimientos atendidos.
- Tiempo promedio de implementación.
- Incidentes posteriores a producción.
- Cambios implementados.
- Requerimientos pendientes.

## 13. VIGENCIA

El presente procedimiento entra en vigor a partir de su aprobación.

# ANEXO A

## Flujo Simplificado

```text
Requerimiento
↓
Análisis
↓
Desarrollo
↓
Validación Técnica
↓
Validación Funcional
↓
Aprobación Usuario
↓
Pase a Producción
↓
Cierre
```

# ANEXO B

## Evidencias Aceptadas

Se consideran evidencias válidas:

- Tickets.
- Correos electrónicos.
- Actas.
- Capturas de pantalla.
- Reportes de validación o pruebas.
- Registros de despliegue.
- Versiones almacenadas en repositorio.
- Manuales de usuario, guías breves, instructivos o capturas comentadas.
- Documentos técnicos, arquitectura simplificada o notas técnicas.
- Formatos referenciales FOR-REQ-TI, FOR-PRU-TI y FOR-DES-TI, o campos equivalentes en la herramienta institucional.

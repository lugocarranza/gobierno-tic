---
codigo: EST-BD-TI
titulo: Estándar de Base de Datos
version: 1.0
tipo: Estandar
responsable: Coordinación de Tecnologías de Información
estado: Vigente
---

# ESTÁNDAR DE BASE DE DATOS

## 1. OBJETIVO

Establecer los lineamientos, políticas y estándares para el diseño, desarrollo, administración y mantenimiento de bases de datos institucionales del Fondo de Inclusión Social Energético (FISE), con la finalidad de asegurar consistencia, integridad, seguridad, trazabilidad y mantenibilidad de la información.

## 2. ALCANCE

El presente estándar aplica a:

- Bases de datos institucionales.
- Sistemas de información desarrollados o administrados por el FISE.
- Ambientes de desarrollo, certificación y producción.
- Componentes de inteligencia de negocios, integración de datos y analítica.
- Personal técnico, desarrolladores, administradores de bases de datos y proveedores que participen en el diseño, desarrollo o mantenimiento de soluciones tecnológicas del FISE.

## 3. DEFINICIONES

### 3.1 Administrador de Base de Datos (DBA)

Responsable de implementar, administrar, monitorear y brindar soporte a las bases de datos institucionales, garantizando la integridad, disponibilidad y seguridad de la información.

### 3.2 Ambiente de Desarrollo

Entorno destinado al desarrollo y pruebas iniciales de componentes de base de datos asociados a una aplicación.

### 3.3 Ambiente de Certificación

Entorno destinado a la validación funcional y técnica de aplicaciones y componentes de base de datos antes de su despliegue en producción.

### 3.4 Ambiente de Producción

Entorno donde operan los sistemas institucionales y se ejecutan los procesos oficiales del FISE.

### 3.5 Base de Datos

Conjunto organizado de datos almacenados electrónicamente para soportar procesos institucionales y aplicaciones informáticas.

### 3.6 Clave Primaria (Primary Key)

Conjunto de uno o más atributos que identifican de manera única cada registro de una tabla.

### 3.7 Clave Foránea (Foreign Key)

Columna o conjunto de columnas que establecen una relación con la clave primaria de otra tabla.

### 3.8 Constraint

Restricción aplicada sobre una tabla o columna para garantizar la integridad y validez de los datos.

### 3.9 Enmascaramiento de Datos

Proceso mediante el cual se oculta o transforma información sensible para impedir su exposición en ambientes distintos al de producción.

### 3.10 Esquema

Conjunto lógico de objetos de base de datos que pertenecen a una misma aplicación o dominio funcional.

### 3.11 Función

Rutina almacenada que recibe parámetros y devuelve un valor.

### 3.12 Procedimiento

Rutina almacenada que ejecuta una serie de operaciones y no devuelve un valor obligatorio.

### 3.13 Sinónimo

Objeto lógico utilizado como alias para referenciar otros objetos de base de datos.

### 3.14 Tabla

Estructura de almacenamiento compuesta por filas y columnas que contiene información relacionada.

### 3.15 Trigger

Objeto de base de datos que ejecuta automáticamente instrucciones ante eventos específicos sobre los datos.

### 3.16 Usuario de Aplicación (UA)

Cuenta utilizada por una aplicación para establecer conexión con la base de datos.

### 3.17 Usuario de Base de Datos (UBD)

Cuenta asignada a una persona para realizar consultas, soporte o actividades autorizadas sobre la base de datos.

### 3.18 Vista

Objeto lógico basado en una consulta que presenta información proveniente de una o más tablas.

## 4. RESPONSABILIDADES

### 4.1 Administrador de Base de Datos (DBA)

Responsable de:

- Administrar los motores de bases de datos institucionales.
- Verificar el cumplimiento del presente estándar.
- Gestionar usuarios y permisos de base de datos.
- Implementar mecanismos de respaldo y recuperación.
- Implementar mecanismos de enmascaramiento de datos cuando corresponda.
- Monitorear el desempeño de las bases de datos.
- Informar incidentes que afecten la disponibilidad, integridad o rendimiento de los servicios.

### 4.2 Coordinación de Tecnologías de Información

Responsable de:

- Aprobar el presente estándar.
- Supervisar su cumplimiento.
- Definir lineamientos técnicos complementarios.
- Resolver excepciones debidamente sustentadas.

### 4.3 Responsable de Base de Datos

Responsable de:

- Diseñar y mantener estructuras de datos.
- Elaborar modelos de datos.
- Aplicar las convenciones de nomenclatura establecidas.
- Coordinar con los desarrolladores la implementación de cambios.

### 4.4 Equipo de Desarrollo

Responsable de:

- Cumplir los lineamientos definidos en el presente estándar.
- Diseñar soluciones compatibles con los modelos de datos aprobados.
- Documentar los cambios realizados.
- Coordinar con el responsable de base de datos las modificaciones estructurales.

### 4.5 Responsable Funcional

Responsable de:

- Validar los requerimientos funcionales relacionados con los datos.
- Identificar información sensible.
- Participar en la validación de los cambios implementados.

# 5. POLÍTICAS DE BASE DE DATOS

## 5.1 Acceso y Seguridad

- Todo acceso a bases de datos deberá estar debidamente autorizado.
- Los accesos deberán otorgarse aplicando el principio de mínimo privilegio.
- Los usuarios serán personales e intransferibles.
- Los accesos privilegiados requerirán autorización expresa de la Coordinación TIC.
- Los ambientes de producción deberán restringir el acceso de escritura únicamente al personal autorizado.
- Las credenciales deberán mantenerse protegidas y no podrán compartirse.

## 5.2 Control

- El presente estándar deberá revisarse periódicamente para asegurar su vigencia y adecuación tecnológica.
- Toda modificación estructural relevante deberá cumplir los procedimientos institucionales de gestión de cambios.

## 5.3 Excepciones

- Toda excepción al presente estándar deberá encontrarse debidamente sustentada y aprobada por la Coordinación TIC.
- Las excepciones deberán documentarse y conservarse como evidencia.

## 5.4 Integridad de Datos

- Toda tabla deberá definir su clave primaria.
- Las relaciones entre tablas deberán implementarse mediante claves foráneas cuando corresponda.
- Las reglas de validación deberán implementarse mediante restricciones de integridad o mecanismos equivalentes.
- Se deberán evitar registros huérfanos y duplicidades no controladas.

## 5.5 Enmascaramiento de Datos

- La información sensible deberá protegerse en ambientes distintos al de producción.
- El enmascaramiento deberá aplicarse antes de poner información productiva a disposición de ambientes de desarrollo o certificación.
- Se consideran datos sensibles, entre otros:

  - Credenciales y contraseñas.
  - Datos personales.
  - Información financiera.
  - Expedientes institucionales.
  - Información contractual.
  - Información declarada como confidencial por el propietario de la información.

## 5.6 Desempeño y Optimización

- Las estructuras de base de datos deberán diseñarse considerando criterios de rendimiento y escalabilidad.
- Las consultas de alto impacto deberán ser evaluadas y optimizadas antes de su paso a producción.
- Los índices deberán implementarse cuando contribuyan a mejorar el desempeño de las consultas y procesos institucionales.

## 5.7 Programación

- Las reglas de negocio deberán implementarse preferentemente en la capa de aplicación.
- La lógica implementada en la base de datos deberá limitarse a funciones técnicas, integridad de datos, auditoría o procesos que justifiquen su ejecución en dicho nivel.
- Todo objeto programable deberá encontrarse documentado y versionado conforme a los estándares institucionales.

## 5.8 Aplicación Proporcional del Estándar

El presente estándar deberá aplicarse de manera proporcional a la criticidad, complejidad y alcance de cada sistema o cambio.

Para mantener una carga operativa razonable en una estructura de TI pequeña, se consideran controles mínimos obligatorios:

- Acceso autorizado y trazable a bases de datos.
- Uso del principio de mínimo privilegio.
- Identificación clara de objetos por aplicación o dominio funcional.
- Nomenclatura consistente para tablas y columnas nuevas o modificadas.
- Clave primaria en tablas nuevas, salvo justificación técnica documentada.
- Campos de auditoría en tablas relevantes cuando resulte aplicable.
- Validación previa de cambios DDL o DML relevantes, proporcional al riesgo e impacto.
- Asociación de cambios a un ticket, requerimiento o cambio aprobado.
- Evidencia de despliegue, resultado y conformidad cuando corresponda.
- Respaldo o mecanismo de reversión para cambios de riesgo medio o alto.

Se consideran lineamientos recomendados o aplicables según complejidad:

- Uso de vistas materializadas.
- Sinónimos.
- Paquetes.
- Modelamiento dimensional.
- Componentes de inteligencia de negocios o integración de datos.
- Documentación técnica extendida de objetos programables.
- Optimización avanzada de índices o consultas.

Las excepciones deberán sustentarse y conservarse como evidencia, sin que ello implique dejar de aplicar los controles mínimos obligatorios.

# 6. ESTÁNDARES DE NOMENCLATURA

## 6.1 Consideraciones Generales

Todo modelo de datos deberá ser revisado y aprobado por el responsable de base de datos antes del inicio del desarrollo o implementación.

Los nombres de objetos de base de datos deberán cumplir las siguientes reglas:

- Utilizar únicamente letras (A-Z), números (0-9) y guion bajo (`_`).
- Escribirse en mayúsculas.
- Mantener nombres descriptivos y entendibles.
- Evitar abreviaturas innecesarias.
- Utilizar nomenclatura uniforme en todos los sistemas institucionales.
- Registrar comentarios descriptivos en la metadata de la base de datos.
- Evitar caracteres especiales, tildes y la letra Ñ.

### Ejemplos

```text
ANIO_EXPEDIENTE
CO_TIPO_SOLICITUD
FE_REGISTRO
```

Cuando sea necesario utilizar nombres compuestos, cada palabra deberá separarse mediante guion bajo (`_`).

### Metadatos

Toda tabla y columna relevante deberá contar con comentarios descriptivos utilizando los mecanismos disponibles del motor de base de datos.

Ejemplo:

```sql
COMMENT ON TABLE BON_TC_SOLICITUD IS
'Solicitudes registradas para el programa BonoGas';
```

```sql
COMMENT ON COLUMN BON_TC_SOLICITUD.CO_ESTADO IS
'Estado actual de la solicitud';
```

---

## 6.2 Identificador de Aplicación

Todos los objetos de base de datos deberán incorporar un identificador que permita asociarlos a una aplicación o dominio funcional.

### Formato General

```text
<ID_APLICACION>_<ID_OBJETO>_<NOMBRE_OBJETO>
```

### Ejemplos Referenciales

| Identificador | Aplicación |
|---------------|------------|
| BON | BonoGas |
| GNV | Ahorro GNV |
| GLP | Vale FISE GLP |
| SIF | Sistema Integral FISE |
| GIS | Sistemas GIS |
| ERP | ERP Institucional |
| MDI | Modelo de Datos Institucional |

La Coordinación TIC podrá definir nuevos identificadores conforme se incorporen nuevos sistemas.

---

## 6.3 Esquemas y Usuarios

### Formato General

```text
<PREFIJO>_<NOMBRE>
```

### Esquemas

| Prefijo | Descripción |
|----------|------------|
| ES | Esquema propietario |

### Ejemplos

```text
ES_BON
ES_GNV
ES_SIF
```

### Usuarios de Aplicación

| Prefijo | Descripción |
|----------|------------|
| US | Usuario de Aplicación |

### Ejemplos

```text
US_BON_WEB
US_BON_API
US_SIF_BATCH
```

### Usuarios de Consulta

| Prefijo | Descripción |
|----------|------------|
| UC | Usuario de Consulta |

### Ejemplos

```text
UC_ANALISTA
UC_AUDITORIA
```

---

## 6.4 Tablas

### Formato General

```text
<APLICACION>_<TIPO_TABLA>_<NOMBRE_TABLA>
```

### Estructura

| Elemento | Descripción |
|-----------|-------------|
| Aplicación | Código de la aplicación |
| Tipo de Tabla | Clasificación funcional |
| Nombre | Nombre descriptivo |

### Ejemplo

```text
BON_TC_SOLICITUD
```

Donde:

| Componente | Valor |
|------------|--------|
| Aplicación | BON |
| Tipo | TC |
| Nombre | SOLICITUD |

### Tipos de Tabla

| Tipo de Contenido | Código |
|-------------------|---------|
| Maestra | TM |
| Cabecera | TC |
| Detalle | TD |
| Trazabilidad / Movimiento | TZ |
| Auxiliar | TX |
| Log | TL |
| Histórica | TH |
| Temporal | TT |
| Parámetros | TP |
| Auditoría | TA |

### Ejemplos

```text
BON_TM_TIPO_BENEFICIARIO
BON_TC_SOLICITUD
BON_TD_SOLICITUD_DETALLE
BON_TZ_SEGUIMIENTO
BON_TA_SOLICITUD
```

### Reglas

- El nombre de la tabla deberá escribirse en singular.
- Toda tabla deberá contar con comentario descriptivo.
- Toda tabla deberá poseer una clave primaria.
- Las relaciones deberán implementarse mediante claves foráneas cuando corresponda.

---

## 6.5 Columnas

### Formato General

```text
<PREFIJO>_<NOMBRE_COLUMNA>
```

### Ejemplo

```text
ID_SOLICITUD
```

Donde:

| Componente | Valor |
|------------|--------|
| Prefijo | ID |
| Nombre | SOLICITUD |

### Prefijos Estándar

| Prefijo | Descripción |
|----------|------------|
| ID | Identificador |
| CO | Código |
| DE | Descripción |
| CM | Comentario |
| NU | Número |
| SE | Secuencia |
| IN | Indicador |
| TI | Tipo |
| ES | Estado |
| FE | Fecha |
| MO | Monto |
| PC | Porcentaje |
| CA | Cantidad |
| NO | Nombre |
| AP | Apellido |
| ME | Medida |
| US | Usuario |
| TE | Terminal |
| DI | Dirección |
| IP | Dirección IP |
| PW | Contraseña |
| ED | Edad |
| FL | Indicador Booleano |

### Ejemplos

| Campo | Descripción |
|---------|------------|
| ID_SOLICITUD | Identificador de solicitud |
| CO_CONCESIONARIA | Código de concesionaria |
| FE_REGISTRO | Fecha de registro |
| MO_FINANCIAMIENTO | Monto financiado |
| US_CREACION | Usuario de creación |
| ES_SOLICITUD | Estado de solicitud |

### Reglas para Claves Primarias

Las claves primarias deberán ubicarse al inicio de la definición de la tabla.

Formato:

```text
ID_<NOMBRE_TABLA>
```

### Ejemplo

Tabla:

```text
BON_TC_SOLICITUD
```

Clave primaria:

```text
ID_SOLICITUD
```

### Reglas para Claves Foráneas

Las claves foráneas deberán utilizar el mismo identificador de la entidad referenciada.

### Ejemplos

```text
ID_SOLICITUD
ID_CONCESIONARIA
ID_BENEFICIARIO
```

### Campos Booleanos

Los campos booleanos deberán indicar claramente el estado que representan.

### Ejemplos

```text
FL_ACTIVO
FL_VIGENTE
FL_APROBADO
```

### Campos de Fecha

Los campos de fecha deberán indicar claramente el evento asociado.

### Ejemplos

```text
FE_REGISTRO
FE_APROBACION
FE_CREACION
FE_ACTUALIZACION
```

### Comentarios de Columnas

Toda columna relevante deberá contar con descripción registrada en metadata.

#### Campo Confidencial

```sql
COMMENT ON COLUMN BON_TC_SOLICITUD.CO_DOCUMENTO IS
'Número de documento del beneficiario. Dato confidencial.';
```

#### Clave Foránea

```sql
COMMENT ON COLUMN BON_TC_SOLICITUD.ID_CONCESIONARIA IS
'Foránea de la tabla BON_TM_CONCESIONARIA';
```

#### Campo Booleano

```sql
COMMENT ON COLUMN BON_TC_SOLICITUD.FL_ACTIVO IS
'Indicador de registro activo (1=Sí, 0=No)';
```

## 6.6 Campos de Auditoría

Las tablas de mayor relevancia, tales como tablas maestras, cabeceras, detalles, trazabilidad y auditoría, deberán incluir campos que permitan registrar la creación y modificación de los registros.

Los campos de auditoría podrán omitirse en tablas temporales, históricas, logs u otras donde técnicamente no resulte necesario.

### Campos Estándar de Auditoría

| Campo | Longitud Referencial | Descripción | Nulo |
|---------|---------|-------------|-------|
| US_CREACION | 38 | Usuario creador del registro | No |
| IP_CREACION | 38 | Dirección IP o equipo origen | No |
| FE_CREACION | Fecha/Hora | Fecha y hora de creación | No |
| US_ACTUALIZACION | 38 | Usuario modificador | Sí |
| IP_ACTUALIZACION | 38 | Dirección IP o equipo de modificación | Sí |
| FE_ACTUALIZACION | Fecha/Hora | Fecha y hora de modificación | Sí |

### Ejemplo

| Campo | Ejemplo |
|---------|---------|
| US_CREACION | MLOPEZ |
| IP_CREACION | 192.168.1.10 |
| FE_CREACION | 2026-01-15 10:45:00 |
| US_ACTUALIZACION | JPEREZ |
| IP_ACTUALIZACION | 192.168.1.15 |
| FE_ACTUALIZACION | 2026-01-20 15:20:00 |

### Comentarios de Metadata

Se recomienda registrar comentarios descriptivos sobre los campos de auditoría.

Ejemplo:

```sql
COMMENT ON COLUMN BON_TC_SOLICITUD.US_CREACION IS
'Usuario que registró inicialmente la información';
```

---

## 6.7 Tablas de Auditoría

Las tablas destinadas al almacenamiento de auditoría deberán utilizar el identificador:

```text
TA
```

### Formato

```text
<APLICACION>_TA_<NOMBRE_TABLA>
```

### Ejemplos

```text
BON_TA_SOLICITUD
GNV_TA_CERTIFICACION
SIF_TA_USUARIO
```

### Campo Obligatorio de Auditoría

Además de los campos estándar de auditoría, las tablas de auditoría deberán incluir el siguiente campo:

| Campo | Descripción |
|---------|-------------|
| TI_ACCION | Tipo de operación realizada |

### Valores Permitidos

| Valor | Descripción |
|---------|-------------|
| INS | Inserción |
| UPD | Actualización |
| DEL | Eliminación |

### Ejemplo

```sql
COMMENT ON COLUMN BON_TA_SOLICITUD.TI_ACCION IS
'Tipo de acción realizada: INS=Inserción, UPD=Actualización, DEL=Eliminación';
```

---

## 6.8 Constraints

Los constraints deberán nombrarse de forma uniforme para facilitar su identificación y mantenimiento.

### Formato General

```text
<TIPO_CONSTRAINT>_<APLICACION>_<NOMBRE>
```

### Tipos de Constraint

| Tipo | Prefijo |
|---------|---------|
| Primary Key | PK |
| Foreign Key | FK |
| Unique | UK |
| Check | CK |

### Ejemplos

#### Clave Primaria

```text
PK_BON_SOLICITUD
```

#### Clave Foránea

```text
FK_BON_CONCESIONARIA
```

#### Restricción Unique

```text
UK_BON_CODIGO_SOLICITUD
```

#### Restricción Check

```text
CK_BON_ESTADO
```

### Recomendaciones

- Toda tabla deberá poseer una clave primaria.
- Las relaciones deberán implementarse mediante claves foráneas.
- Las reglas de validación deberán implementarse mediante restricciones cuando sea técnicamente viable.
- Evitar lógica compleja en restricciones.

---

## 6.9 Índices

Los índices deberán crearse únicamente cuando aporten mejoras reales de rendimiento.

### Formato General

```text
<NOMBRE_TABLA>_<CAMPO>_IDX
```

### Ejemplos

```text
BON_SOLICITUD_FE_REGISTRO_IDX
BON_SOLICITUD_CO_ESTADO_IDX
SIF_USUARIO_NO_USUARIO_IDX
```

### Índices Compuestos

Cuando el índice involucre múltiples columnas deberá utilizarse un nombre descriptivo.

### Ejemplo

```text
BON_SOLICITUD_ESTADO_FECHA_IDX
```

### Recomendaciones

- Crear índices sobre columnas utilizadas frecuentemente en búsquedas.
- Evitar índices innecesarios.
- Revisar periódicamente índices con bajo uso.
- Evaluar impacto sobre operaciones masivas de inserción y actualización.

---

## 6.10 Vistas y Vistas Materializadas

Las vistas deberán nombrarse siguiendo una convención uniforme.

### Formato General

```text
<APLICACION>_<TIPO_VISTA>_<NOMBRE>
```

### Tipos de Vista

| Tipo | Identificador |
|---------|---------------|
| Vista | VW |
| Vista Materializada | VM |

### Ejemplos

#### Vista

```text
BON_VW_SOLICITUDES
```

#### Vista Materializada

```text
BON_VM_REPORTE_FINANCIAMIENTO
```

### Recomendaciones

- Utilizar nombres descriptivos.
- Documentar la finalidad de la vista.
- Evitar vistas excesivamente complejas cuando afecten el rendimiento.
- Evaluar el uso de vistas materializadas para procesos analíticos o consultas recurrentes de gran volumen.

---

## 6.11 Sinónimos

Los sinónimos podrán utilizarse para abstraer propietarios, ubicaciones o nombres físicos de objetos de base de datos.

### Objetivos

- Simplificar referencias.
- Reducir dependencias de esquemas específicos.
- Facilitar cambios de implementación.

### Formato Referencial

```text
<ESQUEMA_DESTINO>_<OBJETO>_<ESQUEMA_ORIGEN>_<OBJETO>
```

### Ejemplo Conceptual

```sql
CREATE SYNONYM BON_SOLICITUD
FOR ES_BON.BON_TC_SOLICITUD;
```

### Recomendaciones

- Utilizar sinónimos cuando existan dependencias entre esquemas.
- Evitar nombres ambiguos.
- Mantener documentación de los sinónimos implementados.
- Utilizar sinónimos para desacoplar aplicaciones de cambios estructurales internos.

## 6.12 Procedimientos

Los procedimientos almacenados deberán utilizar una nomenclatura uniforme que permita identificar fácilmente la aplicación a la que pertenecen y su propósito funcional.

### Formato General

```text
<ID_APLICACION>_PRC_<NOMBRE>
```

### Ejemplos

```text
BON_PRC_REGISTRAR_SOLICITUD
BON_PRC_GENERAR_LIQUIDACION
GNV_PRC_ACTUALIZAR_CERTIFICACION
SIF_PRC_CERRAR_PROCESO
```

### Lineamientos

- El nombre deberá describir claramente la acción realizada.
- Utilizar verbos en infinitivo o acciones concretas.
- Evitar abreviaturas ambiguas.
- Mantener consistencia con la terminología funcional utilizada por la aplicación.

---

## 6.13 Funciones

Las funciones deberán utilizar una nomenclatura que permita identificar claramente el valor o resultado que devuelven.

### Formato General

```text
<ID_APLICACION>_FUN_<NOMBRE>
```

### Ejemplos

```text
BON_FUN_CALCULAR_FINANCIAMIENTO
BON_FUN_OBTENER_ESTADO
GNV_FUN_DIAS_VIGENCIA
SIF_FUN_VALIDAR_PERIODO
```

### Lineamientos

- Toda función deberá devolver un único resultado.
- Las funciones deberán evitar efectos secundarios sobre los datos.
- La lógica implementada deberá ser reutilizable y claramente documentada.

---

## 6.14 Triggers

Los triggers deberán utilizarse únicamente cuando exista una necesidad técnica debidamente justificada.

### Formato General

```text
<ID_APLICACION>_TRG_<NOMBRE>
```

### Ejemplos

```text
BON_TRG_AUD_SOLICITUD
BON_TRG_ESTADO_SOLICITUD
GNV_TRG_AUD_CERTIFICACION
```

### Lineamientos

- Evitar implementar reglas de negocio complejas mediante triggers.
- Utilizar triggers preferentemente para:
  - Auditoría.
  - Trazabilidad.
  - Validaciones técnicas.
  - Sincronizaciones controladas.
- Documentar claramente su propósito y alcance.

---

## 6.15 Secuencias

Las secuencias deberán utilizarse cuando se requiera la generación controlada de identificadores numéricos.

### Formato General

```text
<ID_APLICACION>_SEQ_<NOMBRE>
```

### Ejemplos

```text
BON_SEQ_SOLICITUD
BON_SEQ_LIQUIDACION
GNV_SEQ_CERTIFICACION
SIF_SEQ_PROCESO
```

### Lineamientos

- Mantener una secuencia por entidad cuando corresponda.
- Documentar la relación entre la secuencia y la tabla asociada.
- Registrar dicha relación en los comentarios de metadata cuando resulte aplicable.

### Ejemplo

```sql
COMMENT ON COLUMN BON_TC_SOLICITUD.ID_SOLICITUD IS
'Identificador único de la solicitud. Secuencia: BON_SEQ_SOLICITUD';
```

---

## 6.16 Roles

Los roles deberán utilizarse para agrupar permisos y facilitar la administración de accesos.

### Formato General

```text
<ID_APLICACION>_ROL_<NOMBRE>
```

### Ejemplos

```text
BON_ROL_ADMIN
BON_ROL_CONSULTA
BON_ROL_OPERADOR

SIF_ROL_ADMIN
SIF_ROL_AUDITOR
```

### Lineamientos

- Asignar privilegios mediante roles y no directamente a usuarios cuando sea posible.
- Mantener segregación de funciones.
- Aplicar el principio de mínimo privilegio.
- Revisar periódicamente los roles y permisos asignados.

---

## 6.17 Comentarios y Versionado de Objetos

Todos los procedimientos, funciones, paquetes y triggers deberán incluir información mínima de documentación técnica.

### Información Mínima Recomendada

- Nombre del objeto.
- Propósito.
- Autor.
- Fecha de creación.
- Historial de modificaciones.
- Observaciones relevantes.

### Ejemplo Referencial

```sql
/*
NOMBRE:
BON_FUN_CALCULAR_FINANCIAMIENTO

PROPOSITO:
Calcula el monto de financiamiento aplicable
a una solicitud BonoGas.

REVISIONES:

Fecha        Autor              Descripción
----------   ----------------   --------------------------
01/01/2026   J. Perez           Creación inicial.
15/03/2026   M. Torres          Ajuste de validaciones.

NOTAS:
Mantener alineado con las reglas vigentes
del programa BonoGas.
*/
```

### Control de Cambios

Cuando un objeto sea modificado deberá mantenerse evidencia de:

- Fecha del cambio.
- Responsable.
- Descripción del ajuste.
- Requerimiento o ticket asociado.

### Buenas Prácticas

- Mantener el código fuente bajo control de versiones institucional.
- Registrar los cambios mediante repositorios autorizados.
- Evitar modificaciones directas sin trazabilidad.
- Relacionar cada despliegue con el procedimiento institucional de gestión de cambios.

---

## 6.18 Paquetes

Cuando el motor de base de datos soporte paquetes o módulos equivalentes, éstos deberán utilizarse para agrupar funcionalidades relacionadas.

### Formato General

```text
<ID_APLICACION>_PKG_<NOMBRE>
```

### Ejemplos

```text
BON_PKG_FINANCIAMIENTO
BON_PKG_LIQUIDACION

GNV_PKG_CERTIFICACION
```

### Lineamientos

- Agrupar funciones y procedimientos relacionados.
- Evitar paquetes excesivamente grandes o difíciles de mantener.
- Mantener cohesión funcional dentro del paquete.
- Documentar su propósito general.

## 6.19 Inteligencia de Negocios (BI) e Integración de Datos

Cuando el FISE implemente soluciones de inteligencia de negocios, integración de datos, analítica o almacenamiento histórico de información, deberán aplicarse estándares de nomenclatura consistentes que faciliten la administración y mantenimiento de los componentes involucrados.

### Objetos de Integración de Datos (ETL)

| Tipo de Objeto | Código |
|---------------|---------|
| Paquete | PQ |
| Flujo de Datos | FD |
| Grupo de Paquetes | GP |
| Flujo de Proceso | FP |
| Flujo de Reproceso | FR |
| Conexión / Data Source | DS |
| Arquitectura / Proyecto | AQ |

### Ejemplos

```text
BON_PQ_CARGA_BENEFICIARIOS
BON_FD_SOLICITUDES
BON_GP_CARGA_DIARIA
BON_FP_LIQUIDACION
BON_FR_REPROCESO_ERRORES
BON_DS_PRODUCCION
BON_AQ_DATAWAREHOUSE
```

### Lineamientos

- Los nombres deberán reflejar claramente el proceso implementado.
- Mantener consistencia entre ambientes.
- Evitar abreviaturas ambiguas.
- Documentar las dependencias entre procesos.

---

## 6.20 Variables Globales, Locales y Parámetros

Cuando las herramientas de integración de datos utilicen variables o parámetros, deberá mantenerse una nomenclatura uniforme.

### Variables Globales

Formato:

```text
$VG_<NOMBRE>
```

Ejemplos:

```text
$VG_FECHA_PROCESO
$VG_RUTA_RESPALDO
$VG_PERIODO_LIQUIDACION
```

### Variables Locales

Formato:

```text
$VL_<NOMBRE>
```

Ejemplos:

```text
$VL_TOTAL_REGISTROS
$VL_CONTADOR
$VL_ESTADO_CARGA
```

### Parámetros

Formato:

```text
$P_<NOMBRE>
```

Ejemplos:

```text
$P_FECHA_INICIO
$P_FECHA_FIN
$P_ID_PROCESO
```

### Recomendaciones

- Utilizar nombres descriptivos.
- Evitar variables genéricas como:
  - TEMP
  - VAR1
  - TEST
- Documentar finalidad y alcance de cada variable relevante.

---

## 6.21 Modelamiento Dimensional

Cuando se implementen soluciones analíticas o de inteligencia de negocios, se recomienda utilizar principios de modelamiento dimensional.

### Componentes

| Tipo | Código |
|--------|---------|
| Data Warehouse | DW |
| Tabla de Hechos | HE |
| Tabla Dimensión | DM |

### Ejemplos

#### Data Warehouse

```text
FISE_DW_BENEFICIOS
```

#### Tabla de Hechos

```text
BON_HE_FINANCIAMIENTO
```

#### Tabla Dimensión

```text
BON_DM_BENEFICIARIO
BON_DM_CONCESIONARIA
BON_DM_TIEMPO
```

### Lineamientos

- Las tablas de hechos deberán contener métricas cuantificables.
- Las dimensiones deberán almacenar atributos descriptivos.
- Mantener trazabilidad entre el origen transaccional y el modelo analítico.
- Documentar reglas de transformación y agregación.

---

# 7. ANEXOS

## 7.1 Requerimientos DML

Se consideran operaciones DML aquellas que modifican datos sin alterar la estructura de la base de datos.

### Operaciones Incluidas

```sql
INSERT
UPDATE
DELETE
MERGE
```

### Lineamientos

- Todo script DML deberá encontrarse asociado a un requerimiento, ticket o cambio aprobado.
- Los cambios deberán ser trazables.
- Cuando corresponda, deberá existir respaldo previo de la información afectada.
- Las operaciones masivas deberán validarse previamente en ambientes de certificación o mediante un mecanismo equivalente, según disponibilidad operativa.

### Evidencias Recomendadas

- Script ejecutado.
- Resultado de validación.
- Ticket o requerimiento asociado.
- Evidencia de conformidad.

---

## 7.2 Requerimientos DDL

Se consideran operaciones DDL aquellas que modifican la estructura lógica de la base de datos.

### Operaciones Incluidas

```sql
CREATE
ALTER
DROP
TRUNCATE
RENAME
```

### Casos Típicos

- Creación de tablas.
- Modificación de tablas.
- Creación de índices.
- Creación de vistas.
- Creación de procedimientos.
- Creación de funciones.
- Creación de secuencias.
- Modificación de objetos existentes.

### Lineamientos

- Todo cambio DDL deberá gestionarse mediante el Procedimiento de Gestión de Cambios.
- Deberá existir validación previa proporcional al riesgo e impacto del cambio.
- Los cambios deberán encontrarse documentados.
- Deberá evaluarse el impacto sobre aplicaciones existentes.

### Evidencias Requeridas

- Script DDL.
- Evidencia de validación o pruebas, según corresponda.
- Aprobación correspondiente.
- Registro del despliegue.

---

## 7.3 Respaldos y Despliegues

Todo cambio estructural relevante deberá considerar mecanismos de respaldo y recuperación.

### Consideraciones Mínimas

Antes de una implementación relevante se recomienda:

- Respaldo de objetos afectados.
- Respaldo de información crítica.
- Validación del plan de reversión.
- Verificación de dependencias.

### Plan de Reversión

Cuando el riesgo lo justifique, deberá existir un mecanismo documentado que permita restaurar la situación anterior.

El plan podrá incluir:

- Restauración de respaldos.
- Reversión de scripts.
- Restauración de versiones anteriores.
- Reconfiguración de objetos afectados.

### Evidencias de Despliegue

Como mínimo deberán conservarse:

- Scripts ejecutados.
- Fecha de implementación.
- Responsable de la ejecución.
- Resultado de validaciones.
- Evidencia de conformidad cuando corresponda.

---

# 8. CONTROL DE EXCEPCIONES

Las excepciones al presente estándar deberán:

- Estar debidamente sustentadas.
- Contar con evaluación técnica.
- Ser aprobadas por la Coordinación de Tecnologías de Información.
- Mantener evidencia documental.

Las excepciones no constituyen modificaciones permanentes del estándar.

---

# 9. VIGENCIA

El presente estándar entra en vigencia a partir de su aprobación y permanecerá vigente hasta su modificación o derogación expresa.

---

# ANEXO A

## Resumen de Prefijos de Columnas

| Prefijo | Significado |
|----------|------------|
| ID | Identificador |
| CO | Código |
| DE | Descripción |
| CM | Comentario |
| NU | Número |
| SE | Secuencia |
| IN | Indicador |
| TI | Tipo |
| ES | Estado |
| FE | Fecha |
| MO | Monto |
| PC | Porcentaje |
| CA | Cantidad |
| NO | Nombre |
| AP | Apellido |
| ME | Medida |
| US | Usuario |
| TE | Terminal |
| DI | Dirección |
| IP | Dirección IP |
| PW | Contraseña |
| ED | Edad |
| FL | Indicador Booleano |

# ANEXO B

## Resumen de Tipos de Tabla

| Código | Tipo |
|----------|------|
| TM | Maestra |
| TC | Cabecera |
| TD | Detalle |
| TZ | Trazabilidad |
| TX | Auxiliar |
| TL | Log |
| TH | Histórica |
| TT | Temporal |
| TP | Parámetros |
| TA | Auditoría |


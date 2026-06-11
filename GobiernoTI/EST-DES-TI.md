---
codigo: EST-DES-TI
titulo: Estándar de Desarrollo y Código Fuente
version: 1.0
tipo: Estandar
responsable: Coordinación de Tecnologías de Información
estado: Vigente
---

# ESTÁNDAR DE DESARROLLO Y CÓDIGO FUENTE

## 1. OBJETIVO

Establecer los lineamientos tecnológicos mínimos para el desarrollo, mantenimiento y evolución de los sistemas de información del Fondo de Inclusión Social Energético (FISE), promoviendo la interoperabilidad, seguridad, mantenibilidad, escalabilidad y calidad de las soluciones implementadas.

## 2. ALCANCE

Aplica a:

- Nuevos desarrollos.
- Mantenimientos correctivos.
- Mantenimientos evolutivos.
- Integraciones de sistemas.
- Componentes desarrollados internamente o por terceros para el FISE.

Comprende los sistemas informáticos administrados por el FISE.

## 3. DEFINICIONES

### API REST

Interfaz de programación que permite la comunicación e integración entre sistemas mediante servicios web basados en HTTP.

### Arquitectura Monolítica

Modelo de desarrollo en el que todos los componentes funcionales de una aplicación son desplegados como una única unidad.

### Microservicio

Componente de software independiente que implementa una funcionalidad específica del negocio y puede desplegarse de manera autónoma.

### Backend

Componente encargado de implementar la lógica de negocio, procesamiento de datos e integración con otros sistemas.

### Frontend

Componente encargado de la interacción entre el usuario y la aplicación.

### DTO (Data Transfer Object)

Objeto utilizado para transportar información entre capas o servicios de una aplicación.

### Framework

Conjunto de herramientas y componentes reutilizables que facilitan el desarrollo de software.

### Repositorio de Código Fuente

Herramienta utilizada para almacenar y controlar versiones del código fuente de las aplicaciones.

### Sistema Legado

Aplicación desarrollada antes de la vigencia del presente estándar y que mantiene tecnologías o arquitecturas previamente implementadas.

### Autenticación

Proceso mediante el cual se verifica la identidad de un usuario o sistema.

### Autorización

Proceso mediante el cual se determinan los permisos de acceso de un usuario o sistema autenticado.

### Despliegue

Proceso de instalación y publicación de una versión de software en un ambiente determinado.

## 4. PRINCIPIOS GENERALES

Los desarrollos de software deberán orientarse a los siguientes principios:

- Reutilización de componentes.
- Interoperabilidad entre sistemas.
- Seguridad desde el diseño.
- Mantenibilidad del código.
- Escalabilidad de las aplicaciones.
- Uso preferente de estándares abiertos.
- Trazabilidad de cambios y versiones.

## 5. TECNOLOGÍAS DE DESARROLLO

### 5.1 Backend

Los nuevos desarrollos deberán utilizar preferentemente:

- Java.
- Spring Boot.
- API REST para integración entre sistemas.

### 5.2 Frontend

Los nuevos desarrollos deberán utilizar preferentemente:

- Angular.
- React.

### 5.3 Control de Versiones

Todo desarrollo deberá almacenarse en un repositorio institucional que permita el control de cambios y la trazabilidad de versiones.

## 6. ARQUITECTURA DE APLICACIONES

Las aplicaciones deberán implementarse utilizando una arquitectura por capas que permita separar adecuadamente la presentación, lógica de negocio y acceso a datos.

Podrán emplearse las siguientes arquitecturas:

### 6.1 Arquitectura Monolítica

Aplicable para soluciones de complejidad baja o media, donde los requerimientos de escalabilidad e integración sean limitados.

### 6.2 Arquitectura de Microservicios

Aplicable cuando se presente alguna de las siguientes condiciones:

- Alto volumen de usuarios concurrentes.
- Necesidad de escalabilidad independiente por módulos.
- Integraciones complejas con sistemas externos.
- Procesos de larga duración que puedan afectar el rendimiento general de la aplicación.
- Necesidad de despliegues independientes por componente.

## 7. DESARROLLO E INTEGRACIÓN

Durante el desarrollo se promoverá el uso de buenas prácticas de ingeniería de software, incluyendo:

- Arquitectura por capas.
- DTO (Data Transfer Object).
- Inyección de dependencias.
- Manejo centralizado de excepciones.
- Validación de datos de entrada.
- Componentes reutilizables.
- Principios SOLID.
- Documentación básica del código.

Las integraciones entre aplicaciones deberán realizarse preferentemente mediante API REST sobre HTTPS.

## 8. SEGURIDAD

Las aplicaciones deberán implementar mecanismos de seguridad acordes a los lineamientos institucionales vigentes.

Como mínimo se deberá considerar:

- Autenticación de usuarios.
- Autorización basada en perfiles o roles.
- Registro de auditoría de operaciones críticas.
- Protección de datos sensibles.
- Uso de protocolos seguros de comunicación.

Se recomienda el uso de estándares como:

- OAuth 2.0.
- OpenID Connect.
- Mecanismos equivalentes de autenticación y autorización.

## 9. CALIDAD Y RENDIMIENTO

Previo a la puesta en producción, los desarrollos deberán ser evaluados considerando criterios de:

- Funcionamiento correcto.
- Rendimiento.
- Seguridad.
- Disponibilidad.
- Mantenibilidad.

Las validaciones o pruebas deberán ser proporcionales a la complejidad, riesgo e impacto del cambio.

Para cambios simples o de bajo impacto, podrá bastar una validación funcional, visual, revisión del resultado, captura de pantalla o evidencia equivalente.

Para cambios de mayor impacto, se deberá conservar evidencia razonable de validación técnica o funcional. Las pruebas podrán realizarse de forma manual o mediante herramientas especializadas según la complejidad del sistema.

## 10. SISTEMAS LEGADOS

Las aplicaciones heredadas o desarrolladas previamente a la aprobación del presente estándar podrán mantener su arquitectura, lenguaje de programación, componentes tecnológicos y mecanismos de integración originales.

Las actividades de mantenimiento y soporte sobre sistemas legados se realizarán respetando las tecnologías existentes, siempre que estas continúen operativas y cuenten con soporte técnico adecuado.

Las mejoras evolutivas procurarán alinearse progresivamente al presente estándar en la medida que resulte técnica, operativa y económicamente viable.

## 11. DOCUMENTACIÓN MÍNIMA

Todo desarrollo o mejora significativa deberá contar, como mínimo, con la siguiente documentación:

- Documento de requerimiento o necesidad.
- Código fuente almacenado en repositorio institucional.
- Documento técnico o arquitectura simplificada.
- Manual de usuario, guía breve o instructivo actualizado, cuando el cambio modifique la forma de uso del sistema.
- Evidencia de validación o pruebas realizadas, según corresponda.
- Evidencia de despliegue cuando corresponda.

El manual de usuario o instructivo deberá actualizarse cuando el desarrollo incorpore o modifique pantallas, pasos de atención, reglas visibles para el usuario, perfiles, reportes, mensajes relevantes o cualquier funcionalidad que cambie la operación habitual del sistema. Para cambios menores bastará una guía breve, captura comentada, correo instructivo o actualización del material existente, según corresponda.

## 12. EXCEPCIONES

Cualquier excepción al presente estándar deberá:

- Ser sustentada técnicamente.
- Contar con evaluación de impacto.
- Ser aprobada por la Coordinación de Tecnologías de Información del FISE.
- Mantener evidencia documental de la aprobación correspondiente.

## 13. CUMPLIMIENTO

El incumplimiento de las disposiciones establecidas en el presente estándar podrá dar lugar a las acciones administrativas que correspondan conforme a la normativa interna vigente.

## 14. VIGENCIA

El presente estándar entra en vigencia a partir de su aprobación y permanecerá vigente hasta su modificación o derogación expresa.

# ANEXO A

## Tecnologías Preferentes de Desarrollo

| Componente | Tecnologías Preferentes |
|------------|------------------------|
| Backend | Java, Spring Boot |
| Frontend | Angular, React |
| Integración | API REST sobre HTTPS |
| Control de Versiones | Repositorio institucional |
| Autenticación | OAuth 2.0, OpenID Connect |

# ANEXO B

## Buenas Prácticas de Desarrollo

- Arquitectura por capas.
- Principios SOLID.
- Inyección de dependencias.
- Manejo centralizado de excepciones.
- Validación de datos de entrada.
- Componentes reutilizables.
- Trazabilidad de cambios.
- Documentación técnica mínima.
- Versionamiento del código fuente.

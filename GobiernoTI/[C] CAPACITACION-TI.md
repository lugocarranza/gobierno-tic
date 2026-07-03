# GUÍA DE CAPACITACIÓN SOBRE DIRECTIVAS Y LINEAMIENTOS TIC DEL FISE

## 1. Propósito de la Capacitación

Esta guía ayuda a comprender y aplicar el marco documental de Tecnologías de Información del FISE de forma práctica, simple y auditable.

El marco documental permite ordenar la gestión de TI mediante directivas, procedimientos, estándares, formatos y casos de ejemplo. Su objetivo no es crear burocracia, sino asegurar que las atenciones de TI puedan reconstruirse con evidencia suficiente: qué se solicitó, quién evaluó o aprobó, qué se ejecutó, cómo se validó y cuándo se cerró.

Esta guía es material de apoyo para capacitación. No reemplaza a las directivas, procedimientos, estándares, catálogo de servicios ni formatos vigentes.

## 2. A Quién Está Dirigida

| Público | Interés principal |
|---------|-------------------|
| Coordinación TIC o responsable designado de TIC | Supervisar la gestión operativa de TI, autorizar pases a producción cuando corresponda, gestionar excepciones asignadas y asegurar trazabilidad. |
| Desarrolladores | Registrar requerimientos, cambios, validaciones, código fuente, evidencias técnicas y despliegues. |
| Mesa de Servicios o soporte | Registrar solicitudes, incidentes, prioridades, responsables, evidencias y cierre. |
| Responsable de Base de Datos | Gestionar scripts, cambios de datos, validaciones, respaldos y mecanismos de reversa cuando corresponda. |
| Áreas usuarias | Solicitar necesidades, validar resultados y otorgar conformidad cuando corresponda. |
| Auditoría o Contraloría | Verificar que las atenciones puedan reconstruirse con evidencia suficiente y proporcional. |

## 3. Vista General del Marco Documental

El marco documental se organiza por niveles. Cada nivel cumple una función distinta:

| Nivel | Función | Documentos principales |
|------|---------|------------------------|
| Directivas | Definen lineamientos generales y responsabilidades marco. | DIR-GOB-TI, DIR-GST-TI, DIR-SEG-TI |
| Procedimientos | Indican cómo operar procesos específicos. | PRO-ACC-TI, PRO-CAM-TI, PRO-DES-TI, PRO-INC-MAY-TI, PRO-RES-TI |
| Estándares | Definen criterios técnicos mínimos. | EST-DES-TI, EST-BD-TI |
| Catálogo | Ordena servicios, tipos de atención y prioridades referenciales. | CAT-SER-TI |
| Formatos | Ayudan a registrar información cuando el ticket o Jira no contiene campos suficientes. | FOR-ACC-TI, FOR-CAM-TI, FOR-REQ-TI, FOR-PRU-TI, FOR-DES-TI |
| Casos de ejemplo | Muestran cómo aplicar el marco en situaciones realistas. | CASOS-EJEMPLO |

La lectura recomendada es por capas:

1. Revisar la portada del marco documental para entender el propósito general.
2. Revisar el mapa documental para identificar qué documento aplica.
3. Usar el procedimiento correspondiente al tipo de atención.
4. Aplicar estándares técnicos cuando exista desarrollo, base de datos o seguridad.
5. Usar formatos solo cuando aporten trazabilidad adicional.
6. Revisar casos de ejemplo para entender qué evidencia suele ser suficiente.

## 4. Lineamientos Marco y Catálogo de Servicios

Antes de revisar procedimientos específicos, conviene entender qué rol cumple cada directiva y el catálogo de servicios.

| Documento | Objetivo principal | Por qué es importante | Usuarios más interesados |
|-----------|--------------------|-----------------------|--------------------------|
| DIR-GOB-TI | Alinear las Tecnologías de Información con los objetivos institucionales, la generación de valor público, la gestión de riesgos y el cumplimiento normativo. | Importa porque orienta decisiones y prioridades de TI. Ejemplo: si hay varias iniciativas pendientes, ayuda a priorizar la que reduce mayor riesgo operativo o aporta más valor institucional, dejando evidencia de la decisión. | Dirección, Coordinación TIC, responsables de áreas, auditoría. |
| DIR-GST-TI | Ordenar la gestión de servicios tecnológicos, solicitudes, incidentes, cambios, activos y mejora continua. | Importa porque define cómo atender servicios TI con trazabilidad. Ejemplo: un usuario reporta que no puede ingresar a un sistema; se registra como incidente, se asigna responsable, se documenta la atención y se cierra con evidencia. | Mesa de Servicios, Coordinación TIC o responsable designado de TIC, usuarios solicitantes, proveedores. |
| DIR-SEG-TI | Proteger la información y los activos tecnológicos, preservando confidencialidad, integridad, disponibilidad y trazabilidad. | Importa porque establece controles mínimos de protección. Ejemplo: antes de otorgar acceso a un sistema, se verifica necesidad, aprobación, perfil adecuado y principio de mínimo privilegio. | Todo usuario con acceso a información o sistemas, Coordinación TIC, responsables funcionales, auditoría. |
| CAT-SER-TI | Identificar los servicios tecnológicos disponibles y los tipos de atención: consulta, solicitud, incidente o requerimiento. | Importa porque ayuda a clasificar correctamente la atención. Ejemplo: alta de usuario es solicitud; caída del sistema es incidente; una nueva funcionalidad es requerimiento. | Mesa de Servicios, usuarios, Coordinación TIC o responsable designado de TIC, responsables funcionales. |

### 4.1 Cómo se Relacionan

La Directiva de Gobierno de TI explica cómo se dirige y supervisa TI. La Directiva de Gestión de Servicios explica cómo se atienden las necesidades tecnológicas. La Directiva de Seguridad de la Información establece los controles mínimos para proteger información y servicios. El Catálogo de Servicios ayuda a identificar qué tipo de atención corresponde registrar.

Ejemplo práctico: si un usuario solicita un nuevo acceso, el catálogo ayuda a clasificarlo como solicitud; la directiva de servicios exige trazabilidad; la directiva de seguridad exige mínimo privilegio y autorización; y el procedimiento de accesos indica cómo atenderlo.

## 5. Cómo Navegar el Marco por Necesidad

| Necesidad | Documentos o formatos a revisar | Criterio práctico |
|----------|----------------------------------|------------------|
| Alta, modificación o baja de accesos | PRO-ACC-TI, FOR-ACC-TI, DIR-SEG-TI | El ticket puede reemplazar el formato si contiene datos, justificación, aprobación e implementación. |
| Desarrollo o mejora de software | PRO-DES-TI, EST-DES-TI, FOR-REQ-TI, FOR-PRU-TI | La evidencia debe cubrir requerimiento, desarrollo, validación, conformidad y despliegue cuando aplique. |
| Cambio tecnológico | PRO-CAM-TI, FOR-CAM-TI, FOR-DES-TI | Clasificar como menor, mayor o emergencia y conservar evidencia proporcional. |
| Base de datos | EST-BD-TI, PRO-CAM-TI, PRO-RES-TI cuando corresponda | Scripts, validación, respaldo o reversa deben conservarse según riesgo e impacto. |
| Cambio de emergencia | PRO-CAM-TI, PRO-DES-TI, PRO-INC-MAY-TI si escala | Se permite atención rápida y regularización posterior. |
| Respaldo o recuperación | PRO-RES-TI, EST-BD-TI, PRO-INC-MAY-TI cuando aplique | Conservar logs, verificaciones, solicitudes de restauración y pruebas de recuperación. |
| Incidente mayor | PRO-INC-MAY-TI, DIR-GST-TI, DIR-SEG-TI | Registrar declaración, comunicaciones, acciones, recuperación, validación y cierre. |

## 6. Evidencia Suficiente

La evidencia suficiente es aquella que permite reconstruir la atención sin exigir formatos innecesarios. Puede estar en Jira, Mesa de Servicios, correo institucional, comentarios, capturas, actas, reportes, logs, registros de despliegue o documentos equivalentes.

| Momento | Evidencia esperada | Ejemplos |
|---------|--------------------|----------|
| Inicio | Solicitud, necesidad o incidente. | Ticket, historia de usuario, correo, acta, solicitud de acceso. |
| Evaluación | Alcance, impacto, riesgo, tipo de cambio o validación de acceso. | Comentario técnico, FOR-CAM-TI, análisis en Jira, correo de coordinación. |
| Ejecución | Lo que se desarrolló, configuró o implementó. | Commit, enlace a repositorio, script, bitácora, comentario técnico. |
| Validación | Resultado técnico o funcional. | FOR-PRU-TI, captura, correo de conformidad, comentario del usuario, resultado de ejecución. |
| Pase | Autorización y preparación del pase. | Comentario de autorización, FOR-DES-TI, registro de despliegue o ticket agrupador. |
| Cierre | Resultado final, fecha real, conformidad y cierre. | Cierre del ticket, comentario de resultado, acta, correo o registro equivalente. |

Los formatos `FOR-*` son referenciales. No son obligatorios cuando el ticket, historia, correo o comentario contiene información mínima suficiente.

## 7. Profundización por Proceso

### 7.1 Gestión de Accesos

La gestión de accesos cubre altas, modificaciones, bajas, accesos temporales, accesos privilegiados y revisiones periódicas.

Evidencias importantes:

- Solicitud o ticket.
- Datos del usuario.
- Justificación.
- Aprobación del área responsable.
- Validación de vínculo laboral o contractual cuando corresponda.
- Evidencia de implementación o revocación.
- Cierre del ticket.

El `FOR-ACC-TI` puede usarse como apoyo, pero también puede reemplazarse por campos equivalentes en Mesa de Servicios o Jira.

### 7.2 Desarrollo y Mantenimiento de Software

El desarrollo debe iniciar con una necesidad formalmente registrada y conservar evidencia proporcional al tipo, riesgo e impacto.

Evidencias importantes:

- Requerimiento o historia de usuario.
- Especificación funcional cuando corresponda.
- Código fuente en repositorio.
- Evidencia de validación o pruebas.
- Manual, guía o instructivo actualizado si cambia la forma de uso.
- Conformidad funcional o técnica cuando corresponda.
- Autorización de pase a producción cuando aplique.
- Evidencia de despliegue y cierre.

El `FOR-REQ-TI` ayuda a formalizar requerimientos significativos. El `FOR-PRU-TI` ayuda a consolidar validaciones cuando hay varios escenarios o riesgo relevante.

### 7.3 Gestión de Cambios

Los cambios se clasifican como:

| Tipo | Criterio | Evidencia esperada |
|------|----------|--------------------|
| Cambio menor | Bajo riesgo, impacto limitado y complejidad reducida. | Registro, validación simple y autorización de pase si aplica. |
| Cambio mayor | Impacto funcional, operativo, técnico, contable, de seguridad o de datos relevante. | Evaluación, aprobación proporcional, validación, plan de reversión cuando corresponda y cierre. |
| Cambio de emergencia | Necesario para restablecer servicio crítico, atender incidente de seguridad o mitigar riesgo inmediato. | Autorización rápida, acciones ejecutadas, validación y regularización posterior. |

El `FOR-CAM-TI` sirve como registro inicial o evaluación del cambio. No reemplaza la aprobación del cambio ni la autorización del pase a producción.

### 7.4 Base de Datos

Cuando un cambio incluye base de datos, se debe prestar atención a:

- Scripts DDL o DML.
- Relación con ticket, requerimiento o cambio.
- Validación de ejecución.
- Respaldo previo o mecanismo de reversa cuando corresponda.
- Evidencia de despliegue.

La exigencia debe ser proporcional. Un ajuste menor no requiere el mismo nivel de evidencia que una modificación masiva de datos o un cambio estructural.

### 7.5 Respaldos e Incidentes

Los respaldos y restauraciones deben conservar evidencia de ejecución, verificación y recuperación cuando corresponda.

Un incidente se considera mayor cuando afecta servicios críticos, disponibilidad general, seguridad o continuidad operativa. Si un incidente genera un cambio posterior, debe revisarse también `PRO-CAM-TI`.

## 8. Caso Integral de Desarrollo Complejo

### Escenario

El área usuaria solicita implementar un nuevo módulo de gestión de subsidios que permita registrar solicitudes, validar reglas de elegibilidad, consultar información desde un sistema externo, generar reportes y administrar perfiles diferenciados para evaluación, aprobación y consulta.

El cambio incluye:

- Nuevas pantallas.
- Nuevas reglas funcionales.
- Nuevos perfiles.
- Cambios en base de datos.
- Integración con otro sistema.
- Reportes para seguimiento.
- Manual o guía de usuario.

### Clasificación

| Elemento | Valor |
|----------|-------|
| Tipo de atención | Requerimiento / desarrollo |
| Tipo de cambio | Cambio mayor |
| Procesos involucrados | Desarrollo, gestión de cambios, base de datos y despliegue |
| Riesgo referencial | Medio o alto, según criticidad e impacto |
| Evidencia esperada | Requerimiento, evaluación, aprobación, validación, despliegue y cierre |

### Recorrido Paso a Paso

| Paso | Acción | Evidencia sugerida | Responsable sugerido | Documento relacionado |
|------|--------|--------------------|----------------------|----------------------|
| 1 | Registrar solicitud o historia inicial. | Ticket, historia Jira, correo o acta. | Área usuaria / Mesa de Servicios | DIR-GST-TI / PRO-DES-TI |
| 2 | Formalizar alcance funcional. | FOR-REQ-TI o campos equivalentes. | Usuario responsable / Responsable TIC | PRO-DES-TI / EST-DES-TI |
| 3 | Evaluar impacto técnico y clasificar cambio. | Comentario técnico, evaluación o FOR-CAM-TI. | Responsable técnico / Coordinación TIC o responsable designado de TIC | PRO-CAM-TI |
| 4 | Aprobar cambio mayor. | Aprobación en ticket, correo, acta o documento interno. | Coordinación TIC o responsable designado de TIC y área usuaria | PRO-CAM-TI |
| 5 | Desarrollar componentes. | Commits, merge request, versión o enlace a repositorio. | Desarrollador | EST-DES-TI |
| 6 | Preparar scripts de base de datos. | Scripts versionados, validación y respaldo o reversa cuando corresponda. | Responsable BD / Desarrollador | EST-BD-TI / PRO-RES-TI |
| 7 | Actualizar documentación funcional. | Manual de usuario, guía breve, instructivo o material de capacitación. | Responsable funcional / TIC | EST-DES-TI / PRO-DES-TI |
| 8 | Ejecutar validación técnica y funcional. | FOR-PRU-TI, capturas, reportes, logs o comentarios. | Desarrollador / Usuario responsable | PRO-DES-TI |
| 9 | Autorizar pase a producción. | Comentario, correo, acta o aprobación en ticket. | Coordinación TIC o responsable designado de TIC | PRO-CAM-TI / PRO-DES-TI |
| 10 | Preparar despliegue. | FOR-DES-TI o registro equivalente si aporta trazabilidad. | Responsable técnico / Coordinación TIC o responsable designado de TIC | PRO-CAM-TI |
| 11 | Ejecutar pase y registrar resultado. | Fecha real, responsable, resultado, validación posterior y cierre en ticket. | Responsable técnico | PRO-DES-TI / PRO-CAM-TI |
| 12 | Cerrar atención. | Conformidad funcional o técnica y ticket cerrado. | Área usuaria / Coordinación TIC o responsable designado de TIC | DIR-GST-TI |

### Evidencia Mínima Consolidada del Caso

La tabla anterior muestra el recorrido completo. Como lista de verificación para auditoría, basta confirmar que el caso permita reconstruir lo siguiente:

| Pregunta de control | Evidencia mínima esperada |
|---------------------|---------------------------|
| ¿Qué se solicitó y por qué? | Solicitud, historia, requerimiento o `FOR-REQ-TI` con alcance y conformidad del área usuaria cuando corresponda. |
| ¿Cómo se evaluó el riesgo e impacto? | Evaluación técnica, clasificación como cambio mayor y `FOR-CAM-TI` o campos equivalentes. |
| ¿Quién autorizó lo que correspondía? | Aprobación del cambio y autorización del pase a producción, registradas en ticket, Jira, correo, acta o documento equivalente. |
| ¿Qué se construyó o modificó? | Commits, versión, merge request, componentes modificados, scripts o configuración aplicada. |
| ¿Cómo se validó? | `FOR-PRU-TI`, capturas, comentarios, reportes, logs o conformidad funcional/técnica. |
| ¿Cómo se preparó el pase? | `FOR-DES-TI` o registro equivalente solo si el despliegue requiere coordinación especial, varios cambios, scripts, respaldo o reversión. |
| ¿Cómo se cerró? | Fecha real del pase, resultado, validación posterior y cierre del ticket o registro principal. |

No es necesario duplicar esta evidencia en varios formatos si el ticket, Jira o registro equivalente contiene la información suficiente.

## 9. Buenas Prácticas para Auditoría

- No crear formatos innecesarios si Jira o el ticket contienen información suficiente.
- No confundir la aprobación del cambio con la autorización del pase a producción.
- No exigir pruebas unitarias obligatorias para todo cambio menor.
- No crear ticket separado de despliegue salvo que agrupe varios cambios o requiera coordinación especial.
- Documentar excepciones cuando exista una limitación técnica, operativa, presupuestal o contractual.
- Mantener evidencia proporcional al riesgo e impacto.
- Evitar comités o estructuras que el área no tiene.
- Registrar comentarios claros en tickets: una frase precisa puede ser mejor que un formato incompleto.

## 10. Preguntas de Repaso

| Pregunta | Respuesta esperada |
|----------|--------------------|
| ¿Un cambio menor requiere aprobación formal previa? | No. Debe quedar registrado y contar con validación o conformidad cuando corresponda, pero no requiere aprobación formal previa. |
| ¿Cuál es la diferencia entre aprobar un cambio y autorizar el pase a producción? | La aprobación del cambio confirma que el cambio puede ejecutarse. La autorización del pase confirma que uno o más cambios validados pueden implementarse en producción. |
| ¿Cuándo conviene usar `FOR-REQ-TI`? | Cuando se requiere formalizar la especificación de requerimientos, especialmente en desarrollos nuevos, mejoras significativas o cambios funcionales relevantes. Puede reemplazarse por campos equivalentes en Jira o ticket. |
| ¿Cuándo conviene usar `FOR-CAM-TI`? | Cuando se necesita registrar o evaluar un cambio tecnológico. Puede reemplazarse por campos equivalentes en ticket, Jira, correo o comentario estructurado. |
| ¿Cuándo conviene usar `FOR-DES-TI`? | Cuando el pase a producción requiere preparación especial, agrupa varios cambios, incluye scripts, respaldo, reversa, comunicación a usuarios o coordinación adicional. |
| ¿Dónde puede registrarse la conformidad del área usuaria? | En el ticket, Jira, correo, acta, comentario autorizado, documento de conformidad o formato referencial cuando corresponda. |
| ¿Qué evidencias pueden reemplazar un formato cuando el ticket contiene información suficiente? | Tickets, historias de usuario, correos, comentarios estructurados, capturas, logs, reportes, actas, registros de despliegue o enlaces a repositorio. |
| ¿Qué debe conservarse si un cambio incluye scripts de base de datos? | Los scripts, su relación con el ticket o cambio, evidencia de validación, resultado de ejecución y respaldo o mecanismo de reversa cuando corresponda. |
| ¿Qué evidencia debe regularizarse después de un cambio de emergencia? | La justificación, responsable, acciones ejecutadas, resultado obtenido, evidencia de validación y cierre del ticket o registro equivalente. |
| ¿Por qué los casos de ejemplo no crean obligaciones nuevas? | Porque son material orientador de capacitación. Las obligaciones provienen de las directivas, procedimientos, estándares, catálogo y formatos vigentes. |

## 11. Mensaje Final

El marco documental TIC del FISE busca que el trabajo sea trazable, entendible y defendible en auditoría, sin exigir más documentos de los necesarios.

La regla práctica es simple: si una persona externa revisa el caso, debe poder entender qué se pidió, qué se evaluó, quién autorizó cuando correspondía, qué se ejecutó, cómo se validó y cómo se cerró.

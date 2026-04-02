# IA como herramienta pedagógica en un curso de metodologías de producto
## Hallazgos, hipótesis y preguntas de investigación
### Clase DTLS — Maestría en Ingeniería de Software, Universidad de los Andes

> **Autor:** Daniel Fonseca
> **Estado:** Documento vivo — en construcción
> **Última actualización:** Marzo 2026

---

## Contexto del estudio

Este documento recoge observaciones, hipótesis y preguntas de investigación derivadas de la impartición 2025 del curso DTLS (Design Thinking y Lean Startup), en la que 100 estudiantes trabajaron individualmente en un proyecto transversal con IA como herramienta obligatoria. El objetivo es sistematizar esos hallazgos para informar el rediseño 2026 y, eventualmente, producir un artículo académico sobre la experiencia.

**Corpus disponible:**
- 100 proyectos individuales completos (8 semanas de trabajo)
- Transcripciones de conversaciones con IA (compartidas por los estudiantes como parte de la entrega)
- Entregables semana a semana (PDFs)
- Registros del TutorIA (feedback automático por correo)

---

## Preguntas de investigación

1. ¿En qué medida los estudiantes delegaron en la IA el pensamiento crítico que debía ser suyo (juicio, interpretación, decisión), vs. usarla como herramienta de producción y estructuración?
2. ¿Es posible detectar entrevistas de usuario simuladas por IA a partir del análisis de las conversaciones compartidas?
3. ¿Qué relación existe entre el nivel de delegación a la IA y la calidad (comprensión genuina) del proyecto final?
4. ¿Qué formatos de evaluación son más efectivos para distinguir comprensión real de producción delegada?

---

## Hallazgos y observaciones

### H1 — El link de conversación como evidencia forense

**Observación:** Los estudiantes tenían la instrucción de mantener una sola conversación con su IA a lo largo de cada semana y compartir el link de esa conversación como parte de la entrega. Esto genera un corpus de trazabilidad potencialmente muy valioso.

**Hipótesis de análisis:** Si las "entrevistas a usuarios" aparecen en el mismo hilo de conversación con la IA (en vez de ser datos traídos desde afuera para analizar), es un indicador fuerte de que las entrevistas fueron simuladas. La IA actuó como usuario y como analista en el mismo proceso.

**Pregunta derivada:** ¿Qué porcentaje de estudiantes muestra este patrón? ¿Hay correlación entre este patrón y otros indicadores de calidad del proyecto?

**Estado:** Pendiente de análisis del corpus.

---

### H2 — El exceso de IA no fue uniforme

**Observación:** Los pasos que Daniel deliberadamente diseñó para ser ejecutados con IA (PESTEL, Ansoff, proto-persona) no representan el "exceso". El problema emergió en los pasos que requerían juicio propio: selección de usuarios, interpretación de hallazgos de investigación, priorización de oportunidades, decisiones sobre qué idea seguir.

**Hipótesis:** El exceso de IA se manifiesta específicamente en los momentos de *decisión interpretativa* — cuando el método no da una respuesta correcta, sino que exige criterio situado. Ahí es donde el estudiante delegó en la IA en lugar de ejercer su propio juicio.

**Pregunta derivada:** ¿Se puede operacionalizar "decisión interpretativa delegada" como categoría de análisis en las transcripciones?

**Estado:** Hipótesis inicial, pendiente de validación con corpus.

---

### H3 — El formato "documento + preguntas" como hit de metacognición

**Observación:** El ejercicio en el que el TutorIA recibía el entregable del estudiante y luego le hacía preguntas al respecto fue percibido como particularmente efectivo. A diferencia de la corrección tradicional, este formato fuerza al estudiante a *dar cuenta* de lo que produjo.

**Hipótesis pedagógica:** Este formato opera como un "desempeño de comprensión" en el sentido de EpC: no evalúa si el documento está bien hecho, sino si el estudiante puede pensar y actuar flexiblemente con lo que dice haber aprendido. Es difícil responder bien si no comprendiste el proceso que generó el documento.

**Pregunta derivada:** ¿Qué tipo de preguntas son más discriminantes entre comprensión genuina y producción delegada? ¿Preguntas sobre el proceso de decisión? ¿Sobre counterfactuals ("¿qué habrías hecho si X resultado hubiera sido diferente?")? ¿Sobre aplicación a contextos nuevos?

**Estado:** Concepto validado informalmente. Requiere diseño más riguroso para 2026.

---

### H4 — La transición de individual a grupal cambia la naturaleza del proyecto

**Observación:** La impartición 2025 fue individual. Para 2026 se contempla volver a grupos.

**Hipótesis:** El trabajo grupal introduce una capa adicional de accountability interpersonal que puede reducir ciertos tipos de delegación a la IA (nadie quiere quedar como el que no aportó), pero puede también concentrar el uso de IA en una sola persona del grupo.

**Pregunta derivada:** ¿Cómo se diseña el proyecto grupal de forma que la IA no sea "la tercera persona del grupo que hace todo"? ¿Qué mecanismos de trazabilidad individual funcionan en un proyecto grupal?

**Estado:** Hipótesis inicial, pendiente de decisión de diseño.

---

## Ideas para el rediseño (semillas)

- **Puntos de quiebre explícitos:** Identificar en cada semana el momento de "decisión interpretativa" y diseñar una fricción que obligue al estudiante a ejercer su juicio antes de consultar la IA.
- **TutorIA evolucionado:** Mantener el formato "documento + preguntas" pero hacerlo más sofisticado: preguntas que varíen según el proyecto, que indaguen sobre el proceso de decisión, y que funcionen como evidencia para la evaluación formativa.
- **Trazabilidad del proceso:** Diseñar el proyecto de forma que el *proceso* sea tan visible como el *producto* — no solo "¿qué decidiste?" sino "¿por qué descartaste las otras opciones?"

---

## Teoría en construcción: ambigüedad e incertidumbre como variables centrales del PM

### La hipótesis

Todas las actividades de product management buscan reducir dos cosas, y solo dos:

- **Ambigüedad**: no saber cómo resolver el problema del usuario. La ambigüedad es del espacio de la solución — tiene que ver con el qué y el cómo. Se reduce a través del research, la ideación, el prototipado, el testeo.
- **Incertidumbre**: no saber si esa solución permite alcanzar un objetivo de negocio. La incertidumbre es del espacio del negocio — tiene que ver con la viabilidad, la escalabilidad, la monetización, la adopción. Se reduce a través de la validación, la experimentación, las métricas.

Un framework completo de product management se puede leer como la secuencia de actividades que reduce primero ambigüedad (entender el problema y la solución) y luego incertidumbre (validar que esa solución genera valor de negocio). Esto es, en esencia, lo que Design Thinking + Lean Startup hacen en combinación.

### La conexión con los niveles de abstracción del brief

En la sesión del 22 de marzo de 2026, en el contexto del rediseño de los briefs del proyecto transversal, emergió un framework sobre los niveles de abstracción posibles en un brief estratégico:

| Nivel | Qué se da | Qué queda abierto | Ambigüedad | Incertidumbre |
|---|---|---|---|---|
| 1 — Brief de solución | Qué + Cómo | Nada | Eliminada | Solo queda esta |
| 2 — Brief de pivote | Qué | Cómo | Parcial | Alta |
| 3 — Brief de oportunidad | Espacio del problema | Qué + Cómo | Alta | Alta |
| 4 — Brief de capacidad | Capacidad core | Todo | Máxima | Máxima |
| 5 — Brief abierto | Solo la empresa | Todo | Total | Total |

La elección del nivel de abstracción del brief determina cuánta ambigüedad y cuánta incertidumbre el equipo debe resolver por sí mismo. En un curso de 8 semanas, el Nivel 3 parece el punto de equilibrio óptimo: suficiente ancla estratégica para que el research sea enfocado, pero sin pre-resolver la pregunta que el research debería responder.

El riesgo del Nivel 2 (pivote declarado) es que los estudiantes lleguen al research con sesgo de confirmación: entrevistan para validar una solución que ya tienen, no para entender si existe el problema. Esto reproduce exactamente el error que The Mom Test intenta prevenir.

### La implicación para los roles de producto

Este framework sugiere que los roles de product management se diferencian no solo por seniority, sino por el nivel de abstracción en el que operan:

- **Associate PM**: trabaja principalmente en Nivel 1–2. Recibe una dirección de producto definida y gestiona la ejecución. Reduce ambigüedad sobre el *cómo* dentro de un *qué* dado.
- **Senior PM**: trabaja principalmente en Nivel 2–3. Define el *qué* dentro de un espacio de oportunidad, con base en research y evidencia. Reduce ambigüedad sobre el problema y la solución, con autonomía para decidir qué construir.
- **Head of Product / Group PM**: trabaja en Nivel 3–4. Define los espacios de oportunidad en los que el equipo de producto va a trabajar. Reduce incertidumbre sobre *si* ese espacio vale la pena explorar. La pregunta no es qué construir, sino dónde apostar.
- **CPO**: trabaja en Nivel 4–5. Define la apuesta estratégica de la empresa — la capacidad que se va a desplegar y en qué terreno. Gestiona el portafolio de apuestas. Las preguntas son: ¿en qué somos mejores? ¿Dónde eso importa más?

Esta progresión explica por qué es tan difícil crecer de Associate a Senior PM, o de Senior a Head: no es solo una diferencia de experiencia o habilidad técnica — es un cambio en el tipo de pregunta que uno debe ser capaz de formular y responder. El Associate reduce ambigüedad en un espacio predefinido. El CPO define el espacio.

### Conexión con Design Thinking y Lean Startup

Leído a través de este framework, el ciclo del curso tiene una lógica clara:

- **Empatizar → Definir** (S2–S3): reducir ambigüedad sobre el problema. ¿De qué problema estamos hablando realmente? ¿Para quién?
- **Idear → Validar supuestos** (S3–S4): reducir ambigüedad sobre la solución. ¿Qué podría resolver ese problema? ¿Qué tiene que ser verdad para que funcione?
- **Prototipo de marketing** (S6): reducir incertidumbre de mercado. ¿Hay demanda real? ¿El mensaje resuena?
- **Prototipo de producto** (S7): reducir incertidumbre de valor y usabilidad. ¿El producto produce el valor que prometimos?
- **Video final** (S8): comunicar la reducción de ambigüedad e incertidumbre lograda durante el proceso.

### Preguntas derivadas para investigación

- ¿Los estudiantes con mayor exceso de IA (según H2) se ubican principalmente en los momentos de alta ambigüedad (momentos interpretativos) o en los momentos de alta incertidumbre (momentos de validación)?
- ¿El TutorIA es más discriminante como herramienta de evaluación en los momentos de ambigüedad o en los de incertidumbre?
- ¿Existe una relación entre el nivel de abstracción del brief y la calidad del research resultante?

---

## Por explorar / preguntas abiertas

- ¿Cuál es la intervención mínima necesaria para que una entrevista de usuario sea "real"? ¿5 preguntas a una persona conocida cuentan? ¿O el rigor metodológico es el punto central?
- ¿Cómo se evalúa la comprensión de la metodología vs. la calidad del producto final en un mismo instrumento?
- ¿Qué hace que la semana 8 (reflexión contrafáctica) funcione bien como cierre? ¿Se puede introducir ese mecanismo de manera distribuida a lo largo del curso?

---

*Este documento se actualiza a medida que avanza el análisis del corpus y el rediseño del curso.*

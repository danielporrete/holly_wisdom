# El rol de la IA en la ensenanza de metodologias de producto: una propuesta pedagogica

> **Autor:** Daniel Fonseca
> **Contexto:** Clase DTLS, Maestria en Ingenieria de Software, Universidad de los Andes
> **Estado:** Borrador de trabajo — ideas en desarrollo

---

## 1. El punto de partida: que tipo de conocimiento produce la IA

Los modelos de lenguaje (LLMs) generan contenido a traves de prediccion estadistica. Su mecanismo fundamental es calcular, dado un contexto, cual es la siguiente palabra mas probable. Esto tiene una consecuencia epistemologica profunda: **para una IA, la "verdad" es un asunto probabilistico**. Lo que produce no es "correcto" en el sentido de correspondencia con la realidad, sino en el sentido de consistencia con los patrones del conocimiento humano documentado en sus datos de entrenamiento.

Esta naturaleza probabilistica no es una debilidad en si misma. Es una caracteristica que define donde la IA es confiable y donde no lo es.

### 1.1 Donde la verdad estadistica funciona: el conocimiento metodologico

Hay dominios donde la respuesta mas frecuente en la literatura **coincide con la respuesta correcta**. Esto ocurre en las ciencias puras, las ingenierias, y — de manera particularmente relevante para DTLS — en las **metodologias**.

Design thinking, lean startup, product management: estos campos tienen marcos bien documentados, con pasos definidos, herramientas consensuadas y criterios establecidos. Cuando le pedimos a una IA que nos explique como hacer un mapa de empatia, como disenar un experimento de validacion, o como priorizar un backlog, la respuesta que produce es confiable precisamente porque el consenso en la literatura es fuerte. La media estadistica del conocimiento sobre estos temas esta bien calibrada.

Esto hace de la IA una **herramienta natural para la ensenanza de metodo**. Si la clase trata sobre como ejecutar un proceso — y gran parte de DTLS trata exactamente sobre eso — la IA puede guiar, explicar, ejemplificar y acompanar con alta precision.

### 1.2 Donde la verdad estadistica no alcanza: el conocimiento interpretativo

Sin embargo, no todo el conocimiento humano opera por consenso. Hay dimensiones donde lo valioso no es la respuesta mas frecuente sino la **diversidad de posturas**. La filosofia, la historia, la antropologia, la sociologia, e incluso la psicologia — que aun debate si es ciencia natural o ciencia social — producen conocimiento que es fundamentalmente **interpretativo**. No buscan la respuesta correcta; buscan iluminar un fenomeno desde diferentes angulos.

Cuando la IA opera en estos dominios, tiende a producir lo que Luciano Floridi (2023) describe como un "promedio semantico": una sintesis que aplana la diversidad de perspectivas en favor de una respuesta aparentemente neutral. Es coherente, esta bien escrita, pero le falta postura. Le falta lo que un filosofo llamaria *perspectiva situacional*.

Floridi propone que los outputs de la IA no son propiamente "conocimiento" sino **artefactos semanticos**: significativos para quien los lee, pero producidos sin comprension. Murray Shanahan (2024) lo complementa: los LLMs no poseen un modelo del mundo; reconstruyen patrones lingüisticos sin referencia directa a la realidad que describen.

### 1.3 La implicacion para DTLS

DTLS opera mayormente en territorio metodologico, donde la IA es confiable. Pero las decisiones de producto — a quien investigar, que problema priorizar, como interpretar lo que dice un usuario, que solucion proponer — no son pura metodologia. Son actos de **juicio** que requieren contexto, empatia e interpretacion. Ahi, la IA puede informar pero no decidir.

---

## 2. Lo que Harari nos ensena: inteligencia no es conciencia

Yuval Noah Harari ha desarrollado a lo largo de tres libros (*Homo Deus*, *21 Lessons for the 21st Century*, *Nexus*) un argumento que resulta central para esta propuesta: **inteligencia y conciencia son fenomenos separados**.

La inteligencia es la capacidad de resolver problemas, procesar informacion, reconocer patrones y alcanzar objetivos. La conciencia es la capacidad de sentir — dolor, alegria, duda, responsabilidad. Durante toda la historia biologica, ambas viajaron juntas: todo ser inteligente era tambien consciente. La IA rompe ese patron por primera vez. Es inteligente sin ser consciente.

Harari lo sintetiza asi:

> "Tendemos a confundir inteligencia con conciencia porque en los humanos van de la mano. Pero son cosas muy diferentes."

La consecuencia educativa es directa: si la IA ya posee inteligencia (en el sentido funcional de resolver problemas), lo que debemos desarrollar en el estudiante no es mas inteligencia del mismo tipo, sino **conciencia** — la capacidad de:

1. **Visualizar matices** detras de una respuesta estadisticamente correcta.
2. **Evaluar** si esa respuesta es apropiada para el contexto especifico.
3. **Decidir** que hacer con ella.
4. **Asumir responsabilidad** por la decision.

Harari advierte que el riesgo no es que la IA se vuelva consciente y se rebele (el escenario de ciencia ficcion). El riesgo real es que **los humanos dejen de ejercer su conciencia** — que acepten los outputs de la IA sin cuestionarlos, delegando su juicio a un sistema que no entiende las consecuencias de lo que propone.

En un contexto educativo, esto se traduce en estudiantes que entregan trabajos sofisticados que no comprenden. Hicks, Humphries y Slater (2024) aplican el concepto de *bullshit* de Frankfurt (2005) a los LLMs: producen contenido sin relacion con la verdad, no porque mientan, sino porque no tienen capacidad de preocuparse por la verdad. Si el estudiante adopta esa misma relacion con su propio trabajo — producir sin preocuparse por comprender — el resultado es identico.

---

## 3. La respuesta pedagogica: Ensenanza para la Comprension

Si el problema es que la IA permite producir sin comprender, necesitamos un marco pedagogico que ponga la **comprension** en el centro. Ese marco existe y se llama **Ensenanza para la Comprension (EpC)**, desarrollado en Harvard Project Zero por David Perkins, Howard Gardner, Martha Stone Wiske y otros entre 1988 y 1998.

### 3.1 La definicion de comprension en EpC

EpC define comprension como:

> **"La capacidad de pensar y actuar flexiblemente con lo que uno sabe."** — David Perkins

Esta definicion es deliberadamente opuesta a dos concepciones comunes:

| Concepcion | Ejemplo | Por que es insuficiente |
|---|---|---|
| Conocimiento como posesion | "Se la definicion" | Tener informacion no garantiza poder usarla |
| Conocimiento como rutina | "Se seguir el procedimiento" | Ejecutar un proceso no garantiza entender por que funciona |
| **Comprension (EpC)** | "Puedo usar lo que se en situaciones nuevas" | Requiere explicar, adaptar, justificar, generalizar |

Lo radical de esta definicion es que **comprension y accion no son dos cosas separadas**. Comprender *es* poder actuar flexiblemente. Actuar con criterio *es* demostrar comprension. No se comprende primero y se actua despues — la comprension se construye y se demuestra *a traves de* la accion.

### 3.2 Los desempenos de comprension

EpC propone que la comprension se demuestra a traves de **desempenos**: actividades en las que el estudiante va mas alla de repetir informacion y la usa de manera flexible y novedosa. Un desempeno de comprension no es responder un quiz ni seguir instrucciones. Es explicar algo a una audiencia diferente, aplicar un concepto en un contexto nuevo, justificar una decision, adaptar un metodo a una restriccion inesperada.

Los desempenos se estructuran en tres fases:

1. **Exploracion:** el estudiante se acerca al tema, hace preguntas, conecta con lo que ya sabe.
2. **Investigacion guiada:** el estudiante trabaja de forma mas estructurada, con andamiaje del profesor.
3. **Proyecto de sintesis:** el estudiante demuestra comprension de manera independiente y publica.

### 3.3 La conexion con "entender y actuar"

La formula "entender y actuar" que propongo para DTLS no es un eslogan: es literalmente el nucleo de EpC. Perkins usa la analogia de la flexibilidad en gimnasia: no se puede "tener" flexibilidad en abstracto — solo existe cuando se ejecuta un movimiento flexible. Del mismo modo, no se puede "tener" comprension en la cabeza — solo existe cuando se demuestra en accion.

Esto tiene raices filosoficas profundas:
- **Dewey:** aprender haciendo, pero haciendo *reflexivo*.
- **Wittgenstein:** comprender un concepto es saber como usarlo en casos nuevos.
- **Ryle:** la distincion entre "saber que" (knowing that) y "saber como" (knowing how).

---

## 4. El rol de la IA en este marco: brujula, no piloto

Con estos tres elementos — la naturaleza estadistica de la IA, la distincion de Harari entre inteligencia y conciencia, y el marco EpC — se puede definir con precision el rol de la IA en DTLS:

### La IA como facilitadora de la comprension

La IA ayuda al estudiante a **entender** que esta haciendo y que exige la metodologia en cada etapa. Puede:

- Explicar un concepto de multiples maneras.
- Proporcionar ejemplos contextualizados.
- Senalar que paso sigue segun la metodologia.
- Ofrecer retroalimentacion sobre un avance.
- Hacer visible la estructura de un proceso complejo.

### El estudiante como agente de la accion

El estudiante es quien **decide y actua**. Esto implica:

- Interpretar los hallazgos de su research.
- Decidir que problema priorizar y por que.
- Disenar su solucion y defenderla.
- Evaluar si la sugerencia de la IA aplica a su contexto.
- Asumir responsabilidad por el resultado.

### La linea roja: delegacion sin comprension

Lo que no se permite es lo que la investigacion en factores humanos llama "automation complacency" (Parasuraman & Riley, 1997): la tendencia a sobre-confiar en sistemas automatizados y perder la capacidad de actuar sin ellos. En el contexto educativo, Dreyfus (1986) advierte que si el estudiante puede saltarse las etapas de esfuerzo cognitivo, nunca desarrolla competencia genuina, incluso si sus outputs lo aparentan.

La investigacion en ciencia cognitiva respalda esto: el "efecto de generacion" (Slamecka & Graf, 1978) demuestra consistentemente que el acto de generar una respuesta — incluso incorrecta — produce aprendizaje mas fuerte que recibir pasivamente la respuesta correcta. Delegar a la IA elimina el proceso de generacion.

---

## 5. Sintesis: la propuesta

| Dimension | Para entender | Para actuar |
|---|---|---|
| Marco pedagogico | Ensenanza para la Comprension (EpC) | Continuous Discovery Habits + Lean Product Playbook |
| Rol de la IA | Facilitar comprension, explicar metodo, dar retroalimentacion | Informar decisiones, no tomarlas |
| Rol del estudiante | Demostrar comprension a traves de desempenos | Ejecutar, decidir, iterar, defender |
| Evaluacion | Desempenos de comprension (explicar, justificar, adaptar) | Calidad del proceso y del producto |
| Riesgo a mitigar | Producir sin comprender | Actuar sin entender por que |

---

## 6. Lineas de profundizacion pendientes

1. **Diseno detallado de las 8 lecciones** con objetivos de comprension, desempenos y actividades especificas.
2. **Taxonomia de usos de IA por etapa del proyecto** — donde es util, donde es riesgosa, donde esta prohibida.
3. **Sistema de evaluacion** que distinga comprension de produccion.
4. **Analisis de resultados de la imparticion anterior** — que funciono, que no, que ajustar.
5. **Articulos academicos** sobre la experiencia de integrar IA obligatoria en una clase de maestria.

---

## Referencias

- Bender, E.M., Gebru, T., et al. (2021). "On the Dangers of Stochastic Parrots." *FAccT 2021*.
- Dreyfus, H. & Dreyfus, S. (1986). *Mind over Machine*. Free Press.
- Floridi, L. (2023). "AI as Agency Without Intelligence." *Philosophy & Technology*.
- Frankfurt, H. (2005). *On Bullshit*. Princeton University Press.
- Harari, Y.N. (2016). *Homo Deus: A Brief History of Tomorrow*.
- Harari, Y.N. (2018). *21 Lessons for the 21st Century*.
- Harari, Y.N. (2024). *Nexus: A Brief History of Information Networks*.
- Hicks, M.T., Humphries, J., & Slater, J. (2024). "ChatGPT is Bullshit." *Ethics and Information Technology*.
- Mollick, E. (2024). *Co-Intelligence: Living and Working with AI*. Portfolio/Penguin.
- Olsen, D. (2015). *The Lean Product Playbook*. Wiley.
- Parasuraman, R. & Riley, V. (1997). "Humans and Automation." *Human Factors*.
- Perkins, D. (1998). "What is Understanding?" en Wiske (Ed.), *Teaching for Understanding*. Jossey-Bass.
- Shanahan, M. (2024). "Talking About Large Language Models." *Communications of the ACM*.
- Slamecka, N.J. & Graf, P. (1978). "The Generation Effect." *Journal of Experimental Psychology*.
- Torres, T. (2021). *Continuous Discovery Habits*. Product Talk.
- UNESCO (2023). "Guidance for Generative AI in Education and Research."
- Wiske, M.S. (Ed.). (1998). *Teaching for Understanding: Linking Research with Practice*. Jossey-Bass.

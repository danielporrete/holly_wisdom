# Pautas: Enriquecimiento de ideas capturadas desde redes sociales

> Este documento define el protocolo para transformar contenido breve de redes sociales
> (reels, shorts, podcasts, artículos) en documentos de lectura profunda listos para Kindle.

---

## El ejercicio

Un video corto en redes sociales condensa ideas que tienen raíces más profundas: filósofos,
investigadores, teorías científicas, distinciones conceptuales. El objetivo es capturar esa idea
y construir el contexto que el formato breve no permite dar.

El resultado es un documento que se puede leer en el Kindle como si fuera un ensayo o capítulo
de libro: tiene la idea original como punto de partida, pero la desarrolla con rigor.

---

## Flujo de trabajo

```
1. Recibir link (Instagram, YouTube, web, etc.)
2. Extraer transcripción o contenido principal
3. Identificar ideas, autores y teorías mencionadas
4. Investigar cada elemento con profundidad
5. Generar documento enriquecido en markdown
6. Convertir a EPUB y enviar al Kindle
```

---

## Estructura del documento enriquecido

Todo documento debe tener estas secciones, en este orden:

### 1. Transcripción original (o resumen del contenido fuente)
- Limpia, sin timestamps salvo que sean relevantes
- Fiel al contenido original, sin editar el argumento
- Indica la fuente y fecha de captura

### 2. Secciones de contexto por autor/teoría
Una sección por cada autor o teoría mencionada, con:
- **Datos bibliográficos**: obra, año, publicación. Nunca inventar.
- **Ideas centrales**: desarrolladas con profundidad, no con superficialidad
- **Citas textuales**: solo si están verificadas. Si se parafrasea, indicarlo explícitamente.
- **Conexión con la idea original**: por qué esta teoría importa para entender el contenido fuente

### 3. Tabla comparativa o síntesis (cuando aplique)
- Útil cuando hay múltiples autores o teorías que se pueden contrastar
- Formato tabla para facilitar la lectura en Kindle

### 4. Síntesis final
- Integra todos los marcos en una imagen coherente
- Responde implícitamente: ¿qué aporta cada nivel de análisis a la idea central?
- Niveles típicos: biológico, psicológico, filosófico, cultural/social

---

## Principios de calidad

**Sobre las fuentes:**
- Investigar con rigor: títulos, años y autores deben ser verificados
- No fabricar citas. Si no se encuentra la cita textual exacta, parafrasear e indicarlo
- Preferir fuentes primarias (el libro o paper original) sobre divulgación
- Incluir lista de fuentes al final del documento

**Sobre el tono:**
- Lenguaje accesible pero sin sacrificar precisión conceptual
- No sobreexplicar lo que el lector puede inferir
- No subestimar al lector — este material es para lectura seria, no divulgación superficial

**Sobre la profundidad:**
- Ir más allá de la Wikipedia. El objetivo es el nivel de un capítulo de libro, no de una entrada enciclopédica
- Incluir distinciones que el formato original no tuvo espacio para desarrollar
- Cuando una idea tiene implicaciones contraintuitivas, destacarlas

**Sobre el formato Kindle:**
- Encabezados claros (H2, H3) para navegación por capítulos
- Tablas para comparaciones
- Sin elementos visuales que no se rendericen en e-ink
- Extensión ideal: 1500–4000 palabras. Suficiente para una sesión de lectura.

---

## Capas de enriquecimiento (según el contenido fuente)

Dependiendo del tipo de idea, las capas de contexto varían:

| Tipo de idea | Capas recomendadas |
|---|---|
| Filosófica / humanística | Obra original del autor · Contexto histórico · Críticas o continuadores |
| Científica / psicológica | Paper original · Experimentos clave · Desarrollos posteriores · Implicaciones prácticas |
| Práctica / de negocio | Marco teórico subyacente · Casos reales · Limitaciones del modelo |
| Histórica | Contexto de época · Fuentes primarias · Revisionismo posterior |
| Interdisciplinaria | Un marco por disciplina · Síntesis de convergencias y tensiones |

---

## Ejemplos de preguntas guía para el enriquecimiento

Al recibir un contenido, hacerse estas preguntas:

- ¿Qué autores o teorías se mencionan explícitamente? ¿Cuál es la obra original?
- ¿Qué afirmaciones quedan sin explicar por falta de tiempo en el formato original?
- ¿Hay distinciones conceptuales importantes que el video simplifica?
- ¿Existe investigación científica que fundamente o cuestione la idea?
- ¿Qué implicaciones prácticas tiene esta idea que no se mencionaron?
- ¿Hay pensadores que hayan argumentado lo contrario? ¿Vale la pena incluirlos?

---

## Nombrado de archivos

```
[tema-principal]-[autor-central].md
```

Ejemplos:
- `coleccionismo-benjamin.md`
- `sesgos-cognitivos-kahneman.md`
- `productividad-newport.md`
- `creatividad-csikszentmihalyi.md`

Guardar en: `tareas-varias/` (o en el proyecto correspondiente si el tema es específico de un proyecto)

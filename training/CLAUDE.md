# Training - Daniel Fonseca

## Perfil
- **Estatura:** 1.72m
- **Peso:** 62kg
- **Corredor desde:** 2016 (dominical), 2019 (estructurado)
- **Frecuencia actual:** 5-6x/semana
- **Lesiones:** Sin lesiones recurrentes
- **Datos:** Garmin (archivos .fit, explorar exportación a CSV)
- **Otra actividad:** Calistenia (secundaria)

## PRs
- **Maratón:** 3:14 (segunda maratón, 2024. Primera: 3:24)
- **Media maratón:** 1:36

## Objetivo actual
Mejorar tiempo en media maratón. Sin carrera agendada en los próximos 6 meses. Temporada de construcción de base y velocidad.

## Plan semanal actual
| Día | Tipo | Zona |
|-----|------|------|
| Lunes | Lenta continua | Z2 |
| Martes | Lenta continua | Z2 |
| Miércoles | Velocidad | (por definir) |
| Jueves | Lenta continua | Z2 |
| Viernes | Velocidad | (por definir) |
| Sábado | ¿Sesión larga Z3? | Por decidir |
| Domingo | Descanso / Calistenia? | - |

## Zonas de Frecuencia Cardiaca

FC Maxima real: 187 bpm (observada en series Apr 2026)

| Zona | FC | Descripcion | Uso |
|------|-----|-------------|-----|
| Z1 | <140 | Muy facil | Recuperacion, calentamiento |
| Z2 | 140-155 | Facil, conversacional | Fondos, base aerobica |
| Z3 | 155-168 | Moderado / Tempo | Ritmo maraton, umbral |
| Z4 | 168-180 | Umbral alto / Series | Media maraton, intervalos |
| Z5 | >180 | Maximo | VO2max, series cortas |

## Paces por Tipo de Sesion

| Sesion | Pace | FC Objetivo | Notas |
|--------|------|-------------|-------|
| Fondos (24-28 km) | 5:40-6:00/km | 140-150 | Conversacional, sin prisa |
| Z2 facil | 5:40-6:00/km | 140-150 | Base aerobica |
| Ritmo maraton | 4:36-4:45/km | 155-165 | Solo en sesiones especificas |
| Tempo/Umbral | 4:30-4:45/km | 165-172 | 20-30 min sostenido |
| Intervalos | 4:00-4:20/km | 170-180 | Recuperacion completa entre reps |

## Fondos

- **Distancia:** 24-28 km (por gusto a larga distancia)
- **Pace:** 5:40-6:00/km
- **FC:** 140-150 bpm (Z2)
- **Sensacion:** Puedes hablar frases completas
- **Frecuencia:** 1x semana
- **Dia sugerido:** Sabado

**Clave:** Si la FC sube de 150, bajar el ritmo. El fondo es para volumen y adaptacion aerobica, no para sufrir.

## MCP Garmin Connect

**Paquete:** `@nicolasvegam/garmin-connect-mcp` v1.1.1 (90+ tools)

Con el MCP activo, Claude puede consultar directamente Garmin sin necesidad de exportar CSVs.

### Capacidades disponibles
- Actividades: historial, detalles, splits, zonas HR, clima, splits tipados
- Salud: sueño, HRV, estrés, body battery, SpO2, hidratación
- Rendimiento: VO2max, training readiness, training status, predicciones de carrera
- Escritura limitada: crear actividad manual, registrar peso/hidratación, renombrar actividades

### Limitación importante
**No puede crear ni enviar entrenamientos estructurados al reloj.** Solo `get_workout` / `get_workouts` para lectura. Para eso hay que hacerlo directamente en Garmin Connect (web/app).

### GPS y precisión de datos
El lugar de entrenamiento tiene **zonas con pérdida de GPS por árboles**. Regla de análisis:
- **Entrenos continuos** (Z2, tempo, largo): asumir velocidad constante = usar el pace promedio. Ignorar variaciones de ritmo en la data.
- **Series/intervalos**: las variaciones son intencionales, no artefacto de GPS.

## Archivos del Proyecto

| Archivo | Descripción |
|---------|-------------|
| `CLAUDE.md` | Este archivo - perfil del corredor |
| `TRAINING_LOG.md` | Registro de entrenamientos plan vs ejecutado |
| `running-marzo-2026.md` | Plan mensual activo |

## Flujo de Trabajo

1. **Consultar:** Usar MCP Garmin para revisar actividades recientes
2. **Planificar:** Diseñar sesión con base en datos reales de FC, VO2max y carga
3. **Registrar:** Actualizar TRAINING_LOG.md con plan vs ejecutado
4. **Ajustar:** Modificar próximas sesiones según respuesta

## Semana 9–13 marzo 2026 (datos reales MCP)

| Día | Distancia | Pace real | FC prom | FC máx | Zonas | TE aeróbico | VO2Max |
|-----|-----------|-----------|---------|--------|-------|-------------|--------|
| Lun 9 | 4.45 km | 6:21/km | 138 | 149 | Z2 80% | 2.5 mantener | 53 |
| Mar 10 | 9.80 km | 5:48/km | 149 | 163 | Z3 37% + Z4 34% | 3.5 mejorar | 53 |
| Mié 11 | 5.87 km | 4:57/km | 165 | 176 | Z5 69% + Z4 18% | 3.7 tempo | 54 |

Volumen acumulado al mié: **20.1 km**. VO2Max actual estimado por Garmin: **54**.

## Flujo de trabajo semanal

### Skill `/training-semanal`
Skill local en `~/.claude/skills/training-semanal/SKILL.md`. Se invoca cada domingo en la noche para cerrar la semana y planear la siguiente.

**Flujo completo:**
1. Lee actividades de la semana via MCP Garmin Workouts (`list_activities`, `get_calendar`)
2. Analiza FC vs pace vs zonas target
3. Presenta resumen semana pasada + plan próxima semana → pide aprobación
4. Tras aprobación: sube 6 workouts con `upload_workout` + los agenda con `schedule_workout`
5. Actualiza `TRAINING_LOG.md` (histórico plan vs ejecutado)
6. Notifica a Kipchoge (Telegram) con resumen

**Notas del MCP disponible:**
- Solo está disponible `mcp__garmin-workouts__*` (workouts, actividades, calendario)
- HRV, sueño, body battery y training readiness requieren `@nicolasvegam/garmin-connect-mcp` — no disponible en esta sesión, omitir o señalar ausencia
- Kipchoge bot token: `~/.garmin_telegram_token` | Chat ID: `8605832565`

**Lógica de progresión:**
- Long run: +2km/semana desde 24km hasta 34km, luego negative splits (60% Z2 + 40% Z3)
- Martes alterna cada semana: Series Z4 ↔ Tempo Z3
- Jueves: estímulo opuesto al martes
- Si long run no ejecutado: mantener distancia (no progresar)

**TRAINING_LOG.md:** Histórico de semanas ejecutadas. El plan de la semana entrante no se registra — queda en Garmin y se registra en la sync siguiente.

## Notas
- Mejoró 10 min entre maratón 1 y 2 (3:24 → 3:14)
- Pace maratón ~4:36/km, pace media ~4:32/km → hay margen de mejora en media maratón
- Base aeróbica sólida con 7 años de entrenamiento consistente
- En trotadora: datos de distancia/cadencia no confiables, usar FC
- Con GPS exterior: pérdida de cobertura por árboles → usar pace promedio como referencia

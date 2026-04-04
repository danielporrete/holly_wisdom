# MCPs de Garmin Connect en Claude Code

Este documento describe los dos servidores MCP disponibles para interactuar con Garmin Connect desde Claude Code.

---

## 1. `mcp__garmin` — Garmin Connect (datos de salud y actividades)

El MCP principal de Garmin. Permite leer y escribir datos de salud, actividades, dispositivos y métricas de entrenamiento desde Garmin Connect.

### Categorías de herramientas

#### Actividades
| Herramienta | Descripción |
|---|---|
| `get_activities` | Lista actividades recientes |
| `get_activity` | Detalle de una actividad por ID |
| `get_activity_details` | Detalle extendido (splits, zonas, etc.) |
| `get_activity_splits` | Splits de una actividad |
| `get_activity_typed_splits` | Splits por tipo (carrera, ciclismo, etc.) |
| `get_activity_split_summaries` | Resumen de splits |
| `get_activity_hr_zones` | Zonas de frecuencia cardíaca por actividad |
| `get_activity_power_in_timezones` | Potencia en zonas de tiempo |
| `get_activity_exercise_sets` | Series de ejercicio (fuerza) |
| `get_activity_weather` | Condiciones climáticas durante la actividad |
| `get_activity_gear` | Equipamiento usado en la actividad |
| `get_activity_types` | Tipos de actividad disponibles |
| `get_activities_by_date` | Actividades filtradas por fecha |
| `get_last_activity` | Última actividad registrada |
| `count_activities` | Conteo de actividades |
| `create_manual_activity` | Crear actividad manual |
| `delete_activity` | Eliminar actividad |
| `set_activity_name` | Renombrar actividad |

#### Métricas de salud diaria
| Herramienta | Descripción |
|---|---|
| `get_daily_summary` | Resumen diario de salud |
| `get_daily_health_snapshot` | Snapshot completo de salud del día |
| `get_daily_steps_range` | Pasos en un rango de fechas |
| `get_daily_events` | Eventos del día |
| `get_steps` | Pasos del día |
| `get_steps_chart` | Gráfica de pasos |
| `get_weekly_steps` | Pasos semanales |
| `get_floors` | Pisos subidos |
| `get_hydration` | Hidratación |
| `set_hydration` | Registrar hidratación |

#### Frecuencia cardíaca y HRV
| Herramienta | Descripción |
|---|---|
| `get_heart_rate` | Frecuencia cardíaca |
| `get_resting_heart_rate` | Frecuencia cardíaca en reposo |
| `get_hrv` | Variabilidad de frecuencia cardíaca (HRV) |
| `get_hrv_range` | HRV en rango de fechas |

#### Sueño
| Herramienta | Descripción |
|---|---|
| `get_sleep_data` | Datos de sueño |
| `get_sleep_data_range` | Sueño en rango de fechas |
| `get_sleep_data_raw` | Datos crudos de sueño |

#### Estrés y recuperación
| Herramienta | Descripción |
|---|---|
| `get_stress` | Nivel de estrés del día |
| `get_stress_range` | Estrés en rango de fechas |
| `get_weekly_stress` | Estrés semanal |
| `get_body_battery` | Body Battery |
| `get_body_battery_events` | Eventos de carga/descarga del Body Battery |
| `get_training_readiness` | Preparación para entrenar |
| `get_training_readiness_range` | Preparación en rango de fechas |

#### Métricas de rendimiento
| Herramienta | Descripción |
|---|---|
| `get_vo2max` | VO2 máximo estimado |
| `get_vo2max_range` | VO2 máximo en rango de fechas |
| `get_training_status` | Estado de entrenamiento (carga, tendencia) |
| `get_endurance_score` | Puntuación de resistencia |
| `get_hill_score` | Puntuación en colinas |
| `get_lactate_threshold` | Umbral de lactato |
| `get_cycling_ftp` | FTP de ciclismo |
| `get_race_predictions` | Predicciones de carrera |
| `get_personal_records` | Récords personales |
| `get_intensity_minutes` | Minutos de intensidad |
| `get_weekly_intensity_minutes` | Minutos de intensidad semanales |
| `get_training_plans` | Planes de entrenamiento disponibles |
| `get_training_plan_by_id` | Plan de entrenamiento por ID |
| `get_adaptive_training_plan_by_id` | Plan adaptativo por ID |

#### Composición corporal y peso
| Herramienta | Descripción |
|---|---|
| `get_body_composition` | Composición corporal |
| `get_weigh_ins` | Registros de peso |
| `get_daily_weigh_ins` | Pesos del día |
| `get_latest_weight` | Último peso registrado |
| `add_weigh_in` | Agregar peso |
| `get_fitness_age` | Edad de fitness |

#### Fisiología
| Herramienta | Descripción |
|---|---|
| `get_spo2` | Saturación de oxígeno (SpO2) |
| `get_spo2_range` | SpO2 en rango de fechas |
| `get_respiration` | Frecuencia respiratoria |
| `get_respiration_range` | Respiración en rango de fechas |
| `get_blood_pressure` | Presión arterial |
| `set_blood_pressure` | Registrar presión arterial |

#### Dispositivos y equipo
| Herramienta | Descripción |
|---|---|
| `get_devices` | Lista de dispositivos Garmin vinculados |
| `get_device_last_used` | Último dispositivo usado |
| `get_device_settings` | Configuración del dispositivo |
| `get_device_solar_data` | Datos de carga solar (dispositivos compatibles) |
| `get_gear` | Equipamiento registrado |
| `get_gear_activities` | Actividades asociadas a un equipo |
| `get_gear_defaults` | Equipamiento predeterminado por actividad |
| `get_gear_stats` | Estadísticas de uso del equipo |
| `add_gear_to_activity` | Asociar equipo a actividad |
| `remove_gear_from_activity` | Desasociar equipo de actividad |

#### Perfil y configuración
| Herramienta | Descripción |
|---|---|
| `get_user_profile` | Perfil del usuario |
| `get_user_settings` | Configuración del usuario |
| `get_goals` | Metas del usuario |
| `get_progress_summary` | Resumen de progreso |
| `get_lifestyle_logging_data` | Datos de registro de estilo de vida |
| `get_primary_training_device` | Dispositivo de entrenamiento principal |

#### Insignias y retos
| Herramienta | Descripción |
|---|---|
| `get_available_badges` | Insignias disponibles |
| `get_earned_badges` | Insignias ganadas |
| `get_available_badge_challenges` | Retos de insignias disponibles |
| `get_badge_challenges` | Retos de insignias activos |
| `get_non_completed_badge_challenges` | Retos no completados |
| `get_adhoc_challenges` | Retos ad-hoc |
| `get_inprogress_virtual_challenges` | Retos virtuales en curso |

#### Salud femenina
| Herramienta | Descripción |
|---|---|
| `get_menstrual_data_for_date` | Datos del ciclo menstrual por fecha |
| `get_menstrual_calendar_data` | Calendario menstrual |
| `get_pregnancy_summary` | Resumen de embarazo |

#### Entrenamientos
| Herramienta | Descripción |
|---|---|
| `get_workout` | Detalle de un workout por ID |
| `get_workouts` | Lista de workouts guardados |
| `get_scheduled_workout_by_id` | Workout programado por ID |

---

## 2. `mcp__garmin-workouts` — Garmin Workouts (gestión de entrenamientos)

MCP especializado en la creación, gestión y programación de entrenamientos estructurados en Garmin Connect.

### Herramientas disponibles

| Herramienta | Descripción |
|---|---|
| `list_workouts` | Lista todos los workouts guardados en Garmin Connect |
| `get_workout` | Obtiene el detalle completo de un workout por ID |
| `upload_workout` | Sube un workout nuevo a Garmin Connect |
| `delete_workout` | Elimina un workout de Garmin Connect |
| `schedule_workout` | Programa un workout en una fecha específica del calendario |
| `list_activities` | Lista actividades recientes |
| `get_activity` | Obtiene el detalle de una actividad por ID |
| `get_activity_weather` | Condiciones climáticas durante una actividad |
| `get_calendar` | Obtiene el calendario de Garmin (entrenamientos programados, carreras, etc.) |
| `generate_workout_data_prompt` | Genera un prompt con contexto de actividades recientes para que un LLM diseñe un workout |

### Caso de uso principal

Este MCP está pensado para la **creación y gestión de entrenamientos estructurados** (intervalos, series, ritmo, potencia). El flujo típico es:

1. Usar `generate_workout_data_prompt` para obtener contexto del atleta (actividades recientes, fitness actual).
2. Con ese contexto, diseñar un workout estructurado (steps, targets, repeticiones).
3. Usar `upload_workout` para subirlo a Garmin Connect.
4. Usar `schedule_workout` para programarlo en el calendario.

---

## Diferencias clave entre ambos MCPs

| Aspecto | `mcp__garmin` | `mcp__garmin-workouts` |
|---|---|---|
| **Enfoque** | Lectura y análisis de datos de salud | Creación y gestión de entrenamientos |
| **Datos de salud** | Completo (sueño, HRV, SpO2, estrés, etc.) | No disponible |
| **Actividades** | Lectura detallada | Lectura básica |
| **Workouts estructurados** | Solo lectura | Crear, subir, programar, eliminar |
| **Calendario** | No disponible | Disponible |
| **Ideal para** | Análisis de rendimiento y salud | Planificación de entrenamientos |

---

*Documento generado el 2026-04-04*

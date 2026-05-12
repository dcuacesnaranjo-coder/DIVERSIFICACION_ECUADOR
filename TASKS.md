# TASKS.md — Registro de tareas

## Estados permitidos
`pendiente` | `en_curso` | `bloqueada` | `completada` | `requiere_revision`

## Fase 0 — Configuración del proyecto
| ID | Tarea | Responsable | Estado | Evidencia |
|---|---|---|---|---|
| TASK-000 | Crear estructura base del proyecto | Coordinador | completada | Carpetas y archivos iniciales |
| TASK-001 | Registrar tema, línea y sublíneas | Coordinador | completada | README y CUADERNO_GENERAL |
| TASK-002 | Incorporar paper base | Investigador | completada | README y literatura |

## Fase 1 — Literatura y marco teórico
| ID | Tarea | Responsable | Estado | Evidencia |
|---|---|---|---|---|
| TASK-003 | Crear matriz de literatura sobre HHI y diversificación | Investigador de Literatura | pendiente | 01_literatura/matriz_literatura.md |
| TASK-004 | Buscar papers ARDL sobre diversificación y crecimiento | Investigador de Literatura | pendiente | 01_literatura/papers_ardl.md |
| TASK-005 | Buscar papers VECM/cointegración sobre diversificación | Investigador de Literatura | pendiente | 01_literatura/papers_vecm.md |
| TASK-006 | Buscar papers sobre quiebres estructurales aplicados | Investigador de Literatura | pendiente | 01_literatura/papers_quiebres.md |

## Fase 2 — Datos
| ID | Tarea | Responsable | Estado | Evidencia |
|---|---|---|---|---|
| TASK-007 | Identificar fuentes BCE para PIB trimestral real | Agente de Datos | pendiente | metadata/fuentes_bce.md |
| TASK-008 | Identificar exportaciones trimestrales por sector/producto | Agente de Datos | pendiente | metadata/fuentes_exportaciones.md |
| TASK-009 | Identificar FBKF trimestral real | Agente de Datos | pendiente | metadata/fuentes_fbkf.md |
| TASK-010 | Construir diccionario de datos | Agente de Datos | pendiente | metadata/diccionario_datos.md |

## Fase 3 — Cálculo del IHH
| ID | Tarea | Responsable | Estado | Evidencia |
|---|---|---|---|---|
| TASK-011 | Definir sectores para IHH exportador | Constructor IHH | pendiente | 03_codigo/03_indices/definicion_sectores.md |
| TASK-012 | Programar cálculo del HHI trimestral | Constructor IHH | pendiente | calcular_hhi.py |
| TASK-013 | Generar serie HHI 2000-I a 2024-IV | Constructor IHH | pendiente | processed/hhi_trimestral.csv |
| TASK-014 | Graficar evolución del HHI | Constructor IHH | pendiente | figuras/hhi_evolucion.png |

## Fase 4 — Econometría
| ID | Tarea | Responsable | Estado | Evidencia |
|---|---|---|---|---|
| TASK-015 | Pruebas ADF, PP, KPSS | Econometrista | pendiente | modelos/estacionariedad.md |
| TASK-016 | Pruebas de quiebre estructural | Econometrista | pendiente | modelos/quiebres.md |
| TASK-017 | Estimar ARDL Bounds Test | Econometrista | pendiente | modelos/ardl_resultados.md |
| TASK-018 | Evaluar VECM si procede | Econometrista | pendiente | modelos/vecm_resultados.md |
| TASK-019 | Diagnósticos del modelo final | Econometrista | pendiente | modelos/diagnosticos.md |

## Fase 5 — Robustez
| ID | Tarea | Responsable | Estado | Evidencia |
|---|---|---|---|---|
| TASK-020 | Robustez con dummies de shock | Agente Robustez | pendiente | robustez_dummies.md |
| TASK-021 | Robustez con variable dependiente alternativa | Agente Robustez | pendiente | robustez_pib_percapita.md |
| TASK-022 | Robustez con IHH alternativo | Agente Robustez | pendiente | robustez_hhi_alternativo.md |

## Fase 6 — Manuscrito
| ID | Tarea | Responsable | Estado | Evidencia |
|---|---|---|---|---|
| TASK-023 | Redactar introducción | Redactor | pendiente | 05_manuscrito/01_introduccion.md |
| TASK-024 | Redactar literatura | Redactor | pendiente | 05_manuscrito/02_literatura.md |
| TASK-025 | Redactar metodología | Redactor | pendiente | 05_manuscrito/03_metodologia.md |
| TASK-026 | Redactar resultados | Redactor | pendiente | 05_manuscrito/04_resultados.md |
| TASK-027 | Redactar discusión | Redactor | pendiente | 05_manuscrito/05_discusion.md |
| TASK-028 | Redactar conclusiones | Redactor | pendiente | 05_manuscrito/06_conclusiones.md |

## Fase 7 — Revisión
| ID | Tarea | Responsable | Estado | Evidencia |
|---|---|---|---|---|
| TASK-029 | Revisión metodológica crítica | Revisor | pendiente | 09_revision/revision_metodologica.md |
| TASK-030 | Revisión APA 7 | Revisor | pendiente | 09_revision/revision_apa.md |
| TASK-031 | Revisión de reproducibilidad | Revisor | pendiente | 09_revision/checklist_reproducibilidad.md |

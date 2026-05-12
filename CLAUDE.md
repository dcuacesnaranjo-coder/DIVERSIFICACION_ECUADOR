# CLAUDE.md — Instrucciones para Claude Code / Claude Design

## Contexto del proyecto
Este repositorio contiene el sistema de trabajo para desarrollar un paper académico sobre diversificación productiva, crecimiento económico y desarrollo sostenible en Ecuador bajo dolarización. La metodología replica parcialmente el paper base de Siddiqui y Afzal (2022), adaptando el uso del índice Herfindahl-Hirschman al caso ecuatoriano con datos trimestrales.

## Objetivo de Claude
Ayudar a construir, revisar y mantener código, documentación, prompts, manuscrito y evidencias del proyecto sin romper la reproducibilidad.

## Prioridades
1. Reproducibilidad.
2. Claridad metodológica.
3. Coherencia con línea de investigación.
4. Código limpio y modular.
5. Manuscrito académico en español, con posibilidad de traducción al inglés.

## Stack sugerido
- Python 3.11+
- pandas, numpy, matplotlib
- statsmodels
- arch o ruptures si se usan pruebas/quiebres disponibles
- openpyxl para Excel
- Quarto opcional para manuscrito final
- Stata opcional si el equipo desea replicar modelos ARDL/VECM allí

## Estilo de código
- Usar rutas relativas con `pathlib`.
- Crear funciones pequeñas.
- Guardar salidas en carpetas correspondientes.
- No escribir archivos fuera del proyecto.
- Incluir logs básicos.
- No hardcodear rutas tipo `C:\Users\...`.

## Estructura obligatoria
Claude debe respetar esta estructura:

```text
00_prompts/
01_literatura/
02_datos/
03_codigo/
04_resultados/
05_manuscrito/
06_template_revista/
07_evidencia/
08_presentacion/
09_revision/
```

## Tareas típicas para Claude
- Crear scripts para descargar datos del BCE o leer archivos Excel/CSV.
- Crear función para calcular HHI trimestral.
- Crear script de análisis descriptivo.
- Crear script econométrico ARDL/VECM.
- Generar tablas limpias en CSV, Excel o Markdown.
- Revisar el manuscrito y detectar incoherencias.

## Prompt de inicio recomendado
```text
Lee AGENTS.md, CUADERNO_GENERAL.md, TASKS.md y CHANGELOG.md. Luego identifica el estado actual del proyecto y propone el siguiente paso sin modificar archivos todavía. Respeta el tema: Diversificación productiva, crecimiento económico y desarrollo sostenible en Ecuador bajo dolarización, 2000-2024.
```

## Reglas de edición
Antes de modificar archivos:
1. Leer `TASKS.md`.
2. Verificar si la tarea está `en_curso` o `pendiente`.
3. Registrar modificación propuesta.
4. Hacer cambios mínimos y trazables.
5. Actualizar `CHANGELOG.md`.

## Advertencias metodológicas
- El HHI no es diversificación; es concentración. La diversificación se interpreta como el inverso conceptual del HHI.
- Si se usa `1 - HHI`, debe llamarse índice de diversificación transformado.
- ARDL no acepta variables I(2).
- VECM exige cointegración.
- Las dummies de quiebre deben justificarse histórica y estadísticamente.

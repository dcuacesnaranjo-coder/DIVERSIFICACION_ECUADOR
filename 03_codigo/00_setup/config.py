from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = ROOT / "02_datos" / "raw"
DATA_INTERIM = ROOT / "02_datos" / "interim"
DATA_PROCESSED = ROOT / "02_datos" / "processed"
RESULTS = ROOT / "04_resultados"
FIGURES = RESULTS / "figuras"
TABLES = RESULTS / "tablas"
MODELS = RESULTS / "modelos"

for path in [DATA_RAW, DATA_INTERIM, DATA_PROCESSED, RESULTS, FIGURES, TABLES, MODELS]:
    path.mkdir(parents=True, exist_ok=True)

"""Plantilla para estimar ARDL.

Uso: completar nombres de variables cuando exista base final.
Regla: verificar que ninguna variable sea I(2) antes de usar ARDL Bounds Test.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "02_datos" / "processed" / "base_modelo_trimestral.csv"
OUT = ROOT / "04_resultados" / "modelos" / "ardl_resultados.txt"


def main():
    if not DATA.exists():
        raise FileNotFoundError(f"No existe {DATA}. Primero construya la base del modelo.")

    df = pd.read_csv(DATA)
    # TODO: definir variable dependiente y regresores.
    # Ejemplo conceptual:
    # y = df["g_pib"]
    # x = df[["hhi", "fbkf_real_log", "oil_price_log", "apertura"]]
    # statsmodels.tsa.ardl permite estimar ARDL y bounds test según versión instalada.

    OUT.write_text("Plantilla ARDL creada. Pendiente estimación con datos reales.\n", encoding="utf-8")
    print(f"Resultado inicial: {OUT}")


if __name__ == "__main__":
    main()

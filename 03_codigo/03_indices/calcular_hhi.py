"""Calcular el índice Herfindahl-Hirschman trimestral.

Entrada esperada:
- Archivo CSV/Excel con una columna de trimestre y columnas sectoriales.
- Las columnas sectoriales deben contener valores de exportaciones o VAB sectorial.

Salida:
- CSV con trimestre, HHI, número de sectores y clasificación.
"""

from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "02_datos" / "interim" / "sectores_trimestrales.csv"
OUTPUT = ROOT / "02_datos" / "processed" / "hhi_trimestral.csv"


def clasificar_hhi(hhi: float) -> str:
    if pd.isna(hhi):
        return "sin_dato"
    if hhi < 0.15:
        return "diversificada"
    if hhi < 0.25:
        return "moderadamente_diversificada"
    return "concentrada"


def calcular_hhi(df: pd.DataFrame, time_col: str = "trimestre") -> pd.DataFrame:
    sector_cols = [c for c in df.columns if c != time_col]
    valores = df[sector_cols].apply(pd.to_numeric, errors="coerce")
    total = valores.sum(axis=1)
    shares = valores.div(total, axis=0)
    hhi = (shares ** 2).sum(axis=1)
    out = pd.DataFrame({
        "trimestre": df[time_col],
        "hhi": hhi,
        "n_sectores": len(sector_cols),
        "clasificacion": hhi.apply(clasificar_hhi),
    })
    return out


if __name__ == "__main__":
    if not INPUT.exists():
        raise FileNotFoundError(f"No existe {INPUT}. Cree primero la base sectorial trimestral.")
    df = pd.read_csv(INPUT)
    hhi = calcular_hhi(df)
    hhi.to_csv(OUTPUT, index=False, encoding="utf-8")
    print(f"Archivo generado: {OUTPUT}")

"""Plantilla para pruebas de estacionariedad ADF/KPSS.

Completar cuando exista base final.
"""

from pathlib import Path
import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "02_datos" / "processed" / "base_modelo_trimestral.csv"
OUT = ROOT / "04_resultados" / "modelos" / "estacionariedad.csv"


def adf_test(series):
    s = series.dropna()
    stat, pvalue, lags, nobs, crit, icbest = adfuller(s, autolag="AIC")
    return {"adf_stat": stat, "adf_pvalue": pvalue, "adf_lags": lags, "nobs": nobs}


def kpss_test(series):
    s = series.dropna()
    stat, pvalue, lags, crit = kpss(s, regression="c", nlags="auto")
    return {"kpss_stat": stat, "kpss_pvalue": pvalue, "kpss_lags": lags}


def main():
    if not DATA.exists():
        raise FileNotFoundError(f"No existe {DATA}.")
    df = pd.read_csv(DATA)
    rows = []
    for col in df.columns:
        if col.lower() in ["trimestre", "fecha", "date"]:
            continue
        try:
            row = {"variable": col}
            row.update(adf_test(df[col]))
            row.update(kpss_test(df[col]))
            rows.append(row)
        except Exception as e:
            rows.append({"variable": col, "error": str(e)})
    pd.DataFrame(rows).to_csv(OUT, index=False, encoding="utf-8")
    print(f"Generado: {OUT}")


if __name__ == "__main__":
    main()

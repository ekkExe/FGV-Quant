import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller, kpss

df = pd.read_excel("dados_ambev.xlsx", header=3)
df.columns = ["Data", "PETR4", "ABEV3"]
df["Data"] = pd.to_datetime(df["Data"])
for c in ["PETR4", "ABEV3"]:
    df[c] = pd.to_numeric(df[c].replace("-", pd.NA), errors="coerce")
df = df.set_index("Data").sort_index().dropna()

def adf_print(serie, nome):
    stat, p, lags, nobs, crit, _ = adfuller(serie, regression="c", autolag="AIC")
    print(f"{nome:22s} t = {stat:8.3f} | p = {p:.4f} | lags = {lags} | "
          f"crít. 5% = {crit['5%']:.3f}")

adf_print(df['ABEV3'], f"{'ABEV3'} (nível)")
adf_print(df['ABEV3'].diff().dropna(), f"{'ABEV3'} (1ª diferença)")

# Confirmação com KPSS (H0: estacionária) – útil para a ABEV3 em nível
stat, p, *_ = kpss(df['ABEV3'], regression="c", nlags="auto")
print(f"KPSS {'ABEV3'} (nível): estat = {stat:.3f} | p = {p:.4f}")
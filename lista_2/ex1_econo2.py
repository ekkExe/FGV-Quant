import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.graphics.tsaplots import plot_acf

df = pd.read_excel("dados_ambev.xlsx", header=3)
df.columns = ["Data", "PETR4", "ABEV3"]
df["Data"] = pd.to_datetime(df["Data"])
for c in ["PETR4", "ABEV3"]:
    df[c] = pd.to_numeric(df[c].replace("-", pd.NA), errors="coerce")
df = df.set_index("Data").sort_index().dropna()

ativo = "ABEV3"
preco = df[ativo]

#grafico + FAC
fig, ax = plt.subplots(2, 1, figsize=(13, 8))

ax[0].plot(preco); ax[0].set_title(f"{ativo} – preço (nível)")

plot_acf(preco, lags=40, ax=ax[1]); ax[1].set_title("FAC do preço")

fig.savefig('preços-ambev+fac')
plt.tight_layout()
plt.show()

#teste de estacionariedade
def testes(serie, nome, reg="c"):
    adf_stat, adf_p, *_ = adfuller(serie, regression=reg, autolag="AIC")
    kpss_stat, kpss_p, *_ = kpss(serie, regression=reg, nlags="auto")
    print(f"\n{nome}")
    print(f"  ADF  : estat = {adf_stat:8.3f} | p-valor = {adf_p:.4f}  (H0: raiz unitária)")
    print(f"  KPSS : estat = {kpss_stat:8.3f} | p-valor = {kpss_p:.4f}  (H0: estacionária)")
    if adf_p < 0.05 and kpss_p > 0.05:
        print("ESTACIONÁRIA")
    elif adf_p >= 0.05 and kpss_p <= 0.05:
        print("NÃO estacionária")
    else:
        print("Testes divergem (inconclusivo)")

testes(preco, f"{ativo} – preço (nível)")
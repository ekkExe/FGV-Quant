import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

df = pd.read_excel("dados_ambev.xlsx", header=3)
df.columns = ["Data", "PETR4", "ABEV3"]
df["Data"] = pd.to_datetime(df["Data"])
for c in ["PETR4", "ABEV3"]:
    df[c] = pd.to_numeric(df[c].replace("-", pd.NA), errors="coerce")
df = df.set_index("Data").sort_index().dropna()



ativo = "ABEV3"
preco = df[ativo]

diferença1 = df[ativo].diff().dropna()

#grafico + FAC
fig, ax = plt.subplots(3, 2, figsize=(13, 8))

ax[0, 0].plot(preco); ax[0, 0].set_title(f"{ativo} – preço (nível)")

plot_acf(preco, lags=40, ax=ax[1, 0]); ax[1, 0].set_title("FAC do preço")

plot_pacf(preco, lags=40, ax=ax[2, 0]); ax[2, 0].set_title("FACP do preço")

ax[0, 1].plot(diferença1); ax[0, 1].set_title(f"{ativo} - 1a diferença")
plot_acf(preco, lags=40, ax=ax[1, 1]); ax[1, 1].set_title("FAC da 1a diferença")
plot_pacf(preco, lags=40, ax=ax[2, 1]); ax[2, 1].set_title("FACP da 1a diferença")


fig.savefig('fac+facp')
plt.tight_layout()
plt.show()
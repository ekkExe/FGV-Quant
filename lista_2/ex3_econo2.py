import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose, STL 

df = pd.read_excel("dados_ambev.xlsx", header=3)
df.columns = ["Data", "PETR4", "ABEV3"]
df["Data"] = pd.to_datetime(df["Data"])
for c in ["PETR4", "ABEV3"]:
    df[c] = pd.to_numeric(df[c].replace("-", pd.NA), errors="coerce")
df = df.set_index("Data").sort_index().dropna()

ativo = "ABEV3"

#série diária
diaria = df[ativo].asfreq("B").ffill()            # dias úteis, feriados preenchidos
stl = STL(diaria, period=252, robust=True).fit()

fig = stl.plot()
fig.set_size_inches(11, 8)
fig.suptitle(f"{ativo} – STL sobre log(preço) (diária)", y=1.02)
plt.tight_layout()
plt.show()

#gráfico
fig, ax = plt.subplots(4, 1, figsize=(11, 9), sharex=True)
ax[0].plot(stl.observed);  ax[0].set_ylabel("Preço")
ax[1].plot(stl.trend);     ax[1].set_ylabel("Tendência")
ax[2].plot(stl.seasonal);  ax[2].set_ylabel("Sazonal")
ax[3].plot(stl.resid, lw=0.6); ax[3].axhline(0, c="k", lw=0.5); ax[3].set_ylabel("Resíduo")
plt.tight_layout()
plt.show()
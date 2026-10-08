import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox

df = pd.read_excel("dados_ambev.xlsx", header=3)
df.columns = ["Data", "PETR4", "ABEV3"]
df["Data"] = pd.to_datetime(df["Data"])
for c in ["PETR4", "ABEV3"]:
    df[c] = pd.to_numeric(df[c].replace("-", pd.NA), errors="coerce")
df = df.set_index("Data").sort_index().dropna()

ativo = "ABEV3"
y = df[ativo]

# AR(1) e MA(1) sobre o preço em nível

ar1 = ARIMA(y.values, order=(1, 0, 0), trend="c").fit()
ma1 = ARIMA(y.values, order=(0, 0, 1), trend="c").fit()

print(ar1.summary())
print(ma1.summary())

# Valores previstos (um passo à frente, dentro da amostra)
prev = pd.DataFrame({
    "Observado": y.values,
    "AR(1)": ar1.fittedvalues,
    "MA(1)": ma1.fittedvalues,
}, index=y.index)

# Comparação numérica

def rmse(a, b): return np.sqrt(np.mean((a - b) ** 2))

resumo = pd.DataFrame({
    "AIC": [ar1.aic, ma1.aic],
    "BIC": [ar1.bic, ma1.bic],
    "RMSE": [rmse(prev["Observado"], prev["AR(1)"]),
             rmse(prev["Observado"], prev["MA(1)"])],
}, index=["AR(1)", "MA(1)"])
print(resumo)

print("\nphi (AR1):  ", ar1.params[1])
print("theta (MA1):", ma1.params[1])

for nome, m in [("AR(1)", ar1), ("MA(1)", ma1)]:
    lb = acorr_ljungbox(m.resid, lags=[10, 20], return_df=True)
    print(f"\nLjung-Box resíduos {nome}:\n", lb)


#plots
fig, ax = plt.subplots(2, 1, figsize=(13, 9))

ax[0].plot(prev["Observado"], label="Observado", color="black", lw=1)
ax[0].plot(prev["AR(1)"], label="AR(1)", alpha=0.8, lw=0.9)
ax[0].plot(prev["MA(1)"], label="MA(1)", alpha=0.8, lw=0.9)
ax[0].set_title(f"{ativo} – série completa")
ax[0].legend()

# Zoom no último ano, onde as diferenças ficam visíveis
z = prev.iloc[-250:]
ax[1].plot(z["Observado"], label="Observado", color="black", lw=1.3)
ax[1].plot(z["AR(1)"], label="AR(1)", lw=1.1)
ax[1].plot(z["MA(1)"], label="MA(1)", lw=1.1)
ax[1].set_title("Zoom: últimos 250 pregões")
ax[1].legend()

plt.tight_layout()
plt.savefig("ar1_ma1.png", dpi=110)
plt.show()
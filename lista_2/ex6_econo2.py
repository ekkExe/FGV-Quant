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

print(ar1.summary())
print(ma1.summary())
print(f"AIC AR(1): {ar1.aic:.2f} | AIC MA(1): {ma1.aic:.2f}")
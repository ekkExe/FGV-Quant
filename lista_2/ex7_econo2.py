import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Leitura
df = pd.read_excel("dados_ambev.xlsx", header=3)
df.columns = ["Data", "PETR4", "ABEV3"]
df["Data"] = pd.to_datetime(df["Data"])
for c in ["PETR4", "ABEV3"]:
    df[c] = pd.to_numeric(df[c].replace("-", pd.NA), errors="coerce")
df = df.set_index("Data").sort_index().dropna()

y = df["ABEV3"]
H = 30
treino, teste = y.iloc[:-H], y.iloc[-H:]

# Estimação no treino e previsão de H passos
ar1 = ARIMA(treino.values, order=(1, 0, 0), trend="c").fit()
ma1 = ARIMA(treino.values, order=(0, 0, 1), trend="c").fit()

prev_ar = pd.Series(ar1.forecast(H), index=teste.index)
prev_ma = pd.Series(ma1.forecast(H), index=teste.index)
prev_rw = pd.Series(treino.iloc[-1], index=teste.index) #passeio aleatório para referência

# Avaliação (MSE)
def mse(real, prev):
    return np.mean((real.values - prev.values) ** 2)

res = pd.DataFrame({
    "MSE":  [mse(teste, prev_ar), mse(teste, prev_ma), mse(teste, prev_rw)],
    "RMSE": [np.sqrt(mse(teste, p)) for p in (prev_ar, prev_ma, prev_rw)],
}, index=["AR(1)", "MA(1)", "Passeio aleatório"])
print(res)

# Gráficos: treino, teste e previsões
fig, ax = plt.subplots(2, 2, figsize=(14, 9))
for j, (nome, prev) in enumerate([("AR(1)", prev_ar), ("MA(1)", prev_ma)]):
    a = ax[0, j]
    a.plot(treino, label="Treino", color="tab:blue", lw=0.9)
    a.plot(teste, label="Teste", color="black", lw=1.5)
    a.plot(prev, label=f"Previsão {nome}", color="tab:red", lw=1.5)
    a.set_title(f"{nome} – série completa")
    a.legend()

    a = ax[1, j]
    a.plot(treino.iloc[-90:], label="Treino", color="tab:blue", lw=1.2)
    a.plot(teste, label="Teste", color="black", lw=1.8)
    a.plot(prev, label=f"Previsão {nome}", color="tab:red", lw=1.8)
    a.set_title(f"{nome} – zoom | MSE = {mse(teste, prev):.4f}")
    a.legend()

plt.tight_layout()
plt.savefig("previsao_ar1_ma1.png", dpi=110)
plt.show()
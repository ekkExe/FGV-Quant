import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.optimize import minimize
import matplotlib.pyplot as plt

#define a taxa livre de risco (SELIC)
selic_spot = 0.1375
data_inicio = "01/01/2017"
data_fim = "21/09/2026" #data que os dados foram retirados do economática
codigo = 11

api = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json&dataInicial={data_inicio}&dataFinal={data_fim}'

selic = pd.read_json(api)
selic['data'] = pd.to_datetime(selic["data"], format="%d/%m/%Y")
selic['valor'] = selic['valor']/100
selic.set_index('data', inplace=True)

#copiado do ex1
data = pd.read_excel('dados.xlsx')
data = data.rename(columns={
    data.columns[0]: "Data",
    data.columns[2]: "BBDC4",
    data.columns[3]: "BPAC11",
    data.columns[4]: "ITUB4",
    data.columns[5]: "PETR4",
    data.columns[6]: "VALE3",
    data.columns[7]: "IBOV",
})

data = data[["Data", "BBDC4", "BPAC11", "ITUB4", "PETR4", "VALE3", "IBOV"]]

for col in data.columns[1:]:
    data[col] = pd.to_numeric(data[col].replace("-", pd.NA), errors="coerce")


data["Data"] = pd.to_datetime(data["Data"])
data = data.set_index("Data").sort_index()

#ativo escolhido = Bradesco
ativos = ['BBDC4']

r_simp = data[ativos].pct_change().dropna()

mean_anual = r_simp.mean() * 252

cov_anual = r_simp.cov() * 252

n = len(ativos)
w0 = np.repeat(1/n, n)
limites = tuple((0, 1) for _ in range(n))

def max_sharpe(w):
    retorno = w @ mean_anual.values
    risco = np.sqrt(w @ cov_anual.values @ w)
    return -(retorno - selic_spot) / risco

ans_sharpe = minimize(max_sharpe, w0, method="SLSQP", bounds=limites, constraints={"type": "eq", "fun": lambda w: np.sum(w) - 1})
w_sharpe = ans_sharpe.x

r_portfolio = r_simp[ativos] @ w_sharpe

selic_d = selic['valor'].reindex(index=r_portfolio.index, method='ffill')

x = selic_d.diff().dropna()

y = r_portfolio.loc[x.index]

intercepto = sm.add_constant(x)
model = sm.OLS(y, intercepto).fit()

beta0, beta1 = model.params.iloc[0], model.params.iloc[1]

#grafico
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x, y, alpha=0.4, s=15, color='steelblue', label='Observações Diárias')

x_lin = np.linspace(x.min(), x.max(), 100)
y_lin = beta0 + beta1*x_lin

ax.plot(x_lin, y_lin, color='crimson', linewidth=2, label='Regressão Linear')

ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_title("Regressão Linear da BBDC4 em Relação à Selic")
ax.set_xlabel("Variação da Selic")
ax.set_ylabel("Retorno Diário da Ação")
ax.legend()
fig.tight_layout()
fig.savefig("regressao_linear_bradesco+selic.png", dpi=150)
plt.show()
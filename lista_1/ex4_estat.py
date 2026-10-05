import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#define a taxa livre de risco (SELIC)
selic = 0.1375

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

#copiado do ex4
ativos = ['BBDC4', 'BPAC11', 'ITUB4', 'PETR4', 'VALE3']

r_simp = data[ativos].pct_change().dropna()

mean_anual = r_simp.mean() * 252

cov_anual = r_simp.cov() * 252

n = len(ativos)
w0 = np.repeat(1/n, n)
limites = tuple((0, 1) for _ in range(n))

def max_sharpe(w):
    retorno = w @ mean_anual.values
    risco = np.sqrt(w @ cov_anual.values @ w)
    return -(retorno - selic) / risco

ans_sharpe = minimize(max_sharpe, w0, method="SLSQP", bounds=limites, constraints={"type": "eq", "fun": lambda w: np.sum(w) - 1})
w_sharpe = ans_sharpe.x

r_portfolio = r_simp[ativos] @ w_sharpe
r_portfolio_log = np.log(1 + r_portfolio)

mean = r_portfolio_log.mean()
std = r_portfolio_log.std()
z = (r_portfolio_log - mean) / std

df_fit, loc_fit, scale_fit = stats.t.fit(r_portfolio_log)
x = np.linspace(r_portfolio_log.min(), r_portfolio_log.max(), 1000)

#pdf
pdf_t = stats.t.pdf(x, df_fit, loc = loc_fit, scale = scale_fit)
pdf_normal = stats.norm.pdf(x, loc=mean, scale=std)

#cdf
cdf_t = stats.t.cdf(x, df_fit, loc = loc_fit, scale = scale_fit) 
cdf_normal = stats.norm.cdf(x, loc=mean, scale = std)

dados_ord = np.sort(r_portfolio_log.values)
cdf_real = np.arange(1, len(dados_ord) + 1)/len(dados_ord)

#Gráficos

fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(14, 5.5))

axis1.hist(r_portfolio_log, bins=80, density=True, alpha=0.6, color='blue', label='Z-score dos log-retornos')
axis1.plot(x, pdf_t, color="crimson", linewidth=2, label=f"T-Student")
axis1.plot(x, pdf_normal, color="orange", linewidth=1.5, linestyle="--", label="Normal")
axis1.set_title("PDF dos log-retornos")
axis1.set_xlabel("Log-retorno diário")
axis1.set_ylabel("Densidade")
axis1.legend()

axis2.plot(dados_ord, cdf_real, color="steelblue", linewidth=1.5, label="Real")
axis2.plot(x, cdf_t, color="orange", linewidth=2, linestyle="--", label="T-student")
axis2.plot(x, cdf_normal, color="crimson", linewidth=1.5, linestyle=":", label="Normal")
axis2.axvline(0.03, color="green", linewidth=1, linestyle="-.", alpha=0.7, label="x = 3%")
axis2.set_title("CDF dos log-retornos")
axis2.set_xlabel("Log-retorno diário")
axis2.set_ylabel("Probabilidade acumulada")
axis2.legend()


fig.tight_layout()
fig.savefig("pdf_e_cdf_portfolio.png", dpi=150)
plt.show()
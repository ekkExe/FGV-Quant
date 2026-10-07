import pandas as pd
import numpy as np
from scipy.optimize import minimize
from scipy import stats


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

#TESTES DE HIPÓTESE T-STUDENT

#teste comparando com a média = 0
t_stat, p_value = stats.ttest_1samp(r_portfolio, popmean=0.0)

#significancia
alpha = 0.01

if p_value < alpha:
    print()
    print("Rejeitamos H0: A média dos retornos do portfólio é estatisticamente diferente de 0")
else:
    print()
    print("Não Rejeitamos H0: Não há significância estatística o bastante para afirmarmos que a média dos retornos é diferente de 0")

#teste t-student comparando com o IBOV
r_ibov = data["IBOV"].pct_change().dropna()

#alinhando os dados (para manter o mesmo número de dados para ambos)
df_alinhado = pd.concat([r_portfolio, r_ibov], axis=1).dropna()
df_alinhado.columns = ['portfolio', 'ibov']

t_stat, p_value = stats.ttest_rel(df_alinhado['portfolio'], df_alinhado['ibov'])

if p_value < alpha:
    print()
    print("Rejeitamos H0: A média dos retornos é estatisticamente diferente do IBOVESPA")
else:
    print()
    print("Não Rejeitamos H0: Não há significância estatística o bastante para afirmarmos que a média dos retornos é diferente do IBOVESPA")


import time
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

#selic
selic_spot = 0.1375
data_inicio = "21/09/2021"
data_fim = "21/09/2026"

dt_inicio = pd.to_datetime(data_inicio, format="%d/%m/%Y")
dt_fim = pd.to_datetime(data_fim, format="%d/%m/%Y")


def baixar_sgs(codigo, inicio, fim, passo_anos=1, tentativas=3):
    inicio = pd.to_datetime(inicio, format="%d/%m/%Y")
    fim = pd.to_datetime(fim, format="%d/%m/%Y")
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"
    partes = []
    ini = inicio

    while ini <= fim:
        fim_janela = min(ini + pd.DateOffset(years=passo_anos) - pd.Timedelta(days=1), fim)
        params = {
            "formato": "json",
            "dataInicial": ini.strftime("%d/%m/%Y"),
            "dataFinal": fim_janela.strftime("%d/%m/%Y"),
        }

        for t in range(tentativas):
            r = requests.get(url, params=params, headers=headers, timeout=60)
            texto = r.text.strip()
            if r.status_code == 200 and texto.startswith("["):
                if texto != "[]":
                    partes.append(pd.DataFrame(r.json()))
                break
            print(f"[{codigo}] {params['dataInicial']}–{params['dataFinal']} "
                  f"tentativa {t+1}: status {r.status_code}, resposta: {texto[:200]!r}")
            time.sleep(2 * (t + 1))
        else:
            raise RuntimeError(f"Falha ao baixar série {codigo} em {params}")

        ini = fim_janela + pd.Timedelta(days=1)
        time.sleep(0.5)

    df = pd.concat(partes, ignore_index=True)
    df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
    df["valor"] = pd.to_numeric(df["valor"])
    return df.drop_duplicates("data").set_index("data").sort_index()

# Selic meta
selic = baixar_sgs(11, data_inicio, data_fim)
selic["valor"] = selic["valor"] / 100

# Dólar comercial
cambio = baixar_sgs(1, data_inicio, data_fim).rename(columns={"valor": "usd_brl"})


data = pd.read_excel("dados.xlsx")
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


data = data.loc[dt_inicio:dt_fim]
print(f"Ativo: {data.index.min().date()} a {data.index.max().date()} ({len(data)} pregões)")


ativos = ["BBDC4"]

r_simp = data[ativos].pct_change().dropna()
mean_anual = r_simp.mean() * 252
cov_anual = r_simp.cov() * 252

n = len(ativos)
w0 = np.repeat(1 / n, n)
limites = tuple((0, 1) for _ in range(n))

def max_sharpe(w):
    retorno = w @ mean_anual.values
    risco = np.sqrt(w @ cov_anual.values @ w)
    return -(retorno - selic_spot) / risco

ans_sharpe = minimize(
    max_sharpe, w0, method="SLSQP", bounds=limites,
    constraints={"type": "eq", "fun": lambda w: np.sum(w) - 1},
)
w_sharpe = ans_sharpe.x

r_portfolio = r_simp[ativos] @ w_sharpe


selic_d = selic["valor"].reindex(r_portfolio.index, method="ffill")
cambio_d = cambio["usd_brl"].reindex(r_portfolio.index, method="ffill")

x1 = selic_d.diff()
x2 = cambio_d.pct_change() 

df_reg = pd.concat(
    [r_portfolio.rename("y"), x1.rename("d_selic"), x2.rename("ret_usd")],
    axis=1,
).dropna()

y = df_reg["y"]
X = sm.add_constant(df_reg[["d_selic", "ret_usd"]])

model = sm.OLS(y, X).fit(cov_type="HC3")
print(model.summary())

beta0, beta1, beta2 = model.params["const"], model.params["d_selic"], model.params["ret_usd"]

print()
print(f"alfa (beta0)   = {beta0:.6f}")
print(f"beta Selic     = {beta1:.4f}")
print(f"beta USD/BRL   = {beta2:.4f}")
print(f"R²             = {model.rsquared:.4f}")
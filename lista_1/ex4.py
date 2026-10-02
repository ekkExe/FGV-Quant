import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

data = data.dropna()
ativos = ['BBDC4', 'BPAC11', 'ITUB4', 'PETR4', 'VALE3', 'IBOV']

r_simp = data[ativos].pct_change()
r_log = np.log(data[ativos] / data[ativos].shift(1))

ans = pd.DataFrame(index = ativos)

#aqui foi usado a média da variação percentual para calcular os retornos, mas isso insere viés pela volatilidade dos preços --> superestimação da média

ans["Retorno Simples Diário Médio"] = r_simp.mean()
ans["Retorno Simples Diário Anualizado"] = (1+r_simp.mean())**252 - 1

ans["Retorno Logarítmico Diário Médio"] = r_log.mean()
ans["Retorno Logarítmico Diário Anualizado"] = r_log.mean() * 252

pd.set_option("display.float_format", lambda x: f"{x:.4%}")
print(ans)
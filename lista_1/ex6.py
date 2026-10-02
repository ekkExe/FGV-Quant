import pandas as pd
import numpy as np

import pandas as pd
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

#copiado do ex4
data = data.dropna()
ativos = ['BBDC4', 'BPAC11', 'ITUB4', 'PETR4', 'VALE3', 'IBOV']

r_log = np.log(data[ativos] / data[ativos].shift(1))

matriz = pd.DataFrame(columns=ativos, index=ativos)

for ativo in ativos:
    corr = r_log.corr()[ativo]
    corr = corr.to_numpy()
    matriz.loc[ativo] = corr
print("Matriz de Correlação:")
print(matriz)
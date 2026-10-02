import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

corr = r_log.corr()

graf, axis = plt.subplots(figsize=(7, 6))
im = axis.imshow(corr.to_numpy(), cmap='RdYlGn', vmin=-1, vmax=1)

axis.set_xticks(np.arange(len(ativos)))
axis.set_yticks(np.arange(len(ativos)))
axis.set_xticklabels(ativos)
axis.set_yticklabels(ativos)

for i in range(len(ativos)):
    for j in range(len(ativos)):
        text = axis.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", fontsize=9)

axis.set_title("Matriz Correlação dos Log-Retornos")
graf.colorbar(im, ax=axis, label="Correlação")
graf.tight_layout()
graf.savefig("matriz_correlacao.png", dpi=150)
plt.show()
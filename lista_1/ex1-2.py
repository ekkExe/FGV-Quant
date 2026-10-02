import pandas as pd
import matplotlib.pyplot as plt

#ações escolhidas: Vale, Itau, Banco Bradesco, Petrobrás e BTG Pactual
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

#**FIM DA SOLUÇÃO DO EX1 + COMEÇO DA SOLUÇÃO DO EX2**

#grafico com a base original
graf1, axis = plt.subplots(figsize=(12, 6))
data.plot(ax=axis)
axis.set_title("Fechamento ajustado por proventos — escala original")
axis.set_xlabel("Data")
axis.set_ylabel("Preço (R$) / pontos (IBOV)")
axis.legend(title="Ativo")
graf1.tight_layout()
graf1.savefig("fechamento_escala_original.png", dpi=150)

#grafico com a base indexada
graf2, axis2 = plt.subplots(figsize=(12, 6))
base = data / data.bfill().iloc[0] * 100
axis2.plot(base)
axis2.set_title("Performance comparada (base 100 no início da série)")
axis2.set_xlabel("Data")
axis2.set_ylabel("Índice (base 100)")
axis2.legend(title="Ativo")
graf2.tight_layout()
graf2.savefig("fechamento_base.png", dpi=150)

plt.show()

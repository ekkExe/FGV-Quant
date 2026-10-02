import pandas as pd
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

#ativo escolhido: Petrobrás (dropna = remove os valores nulos para não ter erro nas contas)
data = data.dropna(subset=['PETR4'])

#cálculo das médias móveis de 5 e 20 dias
data['MM5'] = data['PETR4'].rolling(window=5).mean()
data['MM20'] = data['PETR4'].rolling(window=20).mean()

#gráfico com o fechamento ajustado e as médias móveis
graf, axis = plt.subplots(figsize=(12, 6))
axis.plot(data.index, data['PETR4'], label='Fechamento Ajustado PETR4', color='blue', linewidth=1, alpha=0.7)
axis.plot(data.index, data['MM5'], label='Média Móvel 5 dias', color='orange', linewidth=1.5)
axis.plot(data.index, data['MM20'], label='Média Móvel 20 dias', color='red', linewidth=1.5)
axis.set_xlabel("Data")
axis.set_ylabel("Preço (R$)")
axis.set_title("Gráfico - Exercício 2: Fechamento Ajustado PETR4 e Médias Móveis")
axis.legend()
plt.show()
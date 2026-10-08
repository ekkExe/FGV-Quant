#set text(
  font:"New Computer Modern Math"
)
#set par(
  justify: true
)
#set rect(
  width:100%,
  height:100%,
  inset:4pt,
)
#text()[= LISTA DE EXERCÍCIOS 2: RESPOSTAS]
#linebreak()

#emph(text(red)[=== EXERCÍCIOS DE ECONO I])
#text(blue)[1)] O ativo escolhido foi o do Bradesco e foi regredido em relação à taxa selic. Evidentemente, por se tratar de um banco, o Bradesco provavelmente possui consideráveis títulos pós-fixados indexados à Selic. Assim, é justificável a sensibilidade de 198.47, já que, um aumento da taxa implica maior resultado para o Bradesco.

#text(blue)[2)] A dispersão do gráfico apresentou uma grande concentração do valor da variação da selic (eixo x) em 0. Isso se deve porque a variação da selic acontece apenas em reuniões do COPOM que não acontecem diariamente, mas a cada 45 dias. Além disso, é visualmente justificável a alta sensibilidade encontrada por causa da relação positiva (reta para cima) mesmo com minúsculas alterações na selic (obs: eixo x na escala 10#super[-5])

#text(blue)[3)] Como feito no ex 1, o valor do coeficiente é positivo, correspondendo com a ideia de que o Bradesco possuiria títulos pós-fixados na Selic. Entretanto, ele não é significativo a 5 ($alpha$ < P-value).

Por definição, o R#super[2] é o quadrado da correlação. Assim, ele aponta diretamente a variabilidade percentual que a Selic causa na ação da Bradesco. O valor extremamente pequeno (0.1%) mostra que a BBDC4 possui outros fatores que explicam os outros 99.9% da variação do preço que não foram incluídos no modelo.

#text(blue)[5)] O principal problema de considerar apenas uma variável para modelar a sua previsão são as variáveis omitidas. Isso pode gerar outros problemas relacionados, como o Paradoxo de Simpson.

Entre os coeficientes, o $beta$#sub[0] quase não se alterou (0.000448 para 0.000493), o $beta$#sub[Selic] se alterou minimamente, de 198 para 193. Já o R#super[2] saiu de 1% para 6.6%.

A alteração no coeficiente da Selic se deu por dois motivos: o código teve que ter o seu período alterado pela impossibilidade de leitura do cambio para um momento maior que 5 anos. Ademais, mesmo que isso não tivesse ocorrido, ainda haveriam alterações no beta pelo fato de que as variáveis escolhidas não serem estritamente não correlacionadas (correl $!=$ 0).

Já o R#super[2] aumentou, já que agora não há apenas 1 fator tentando explicar as alterações na ação, mas 2, a Selic e o câmbio dólar-real.

#text(blue)[6)] A regressão encontrou $beta$#sub[IBOV] = 0.6199. Esse coeficiente, por ser da relação entre um ativo com o mercado, representa o $beta$ de mercado. Esse índica é simplesmente uma medição do risco sistemático e da volatilidade de um ativo com o mercado como um todo. Como $beta$#sub[IBOV] < 1, o portfólio tem volatilidade menor que a do mercado, sendo portanto, uma possível operação defensiva.

#linebreak()
#emph(text(red)[=== EXERCÍCIOS DE ECONO II])

#text(blue)[1)] A série é estacionária. Isso pois não só foi testado a estacionariedade, mas também porque pelo gráfico da FAC, é evidente que o aumento de lags causa uma queda gradual e lenta da autocorrelação.

#text(blue)[2)] Após o teste Dickey-Fuller, é evidente que a primeira diferença (p-value = 0.01%) é uma série estacionária. Entretanto, a série original possui p-value = 1.1%, isso significa que para a significância convencional (5), os preços são estacionários, mas caso seja considerado apenas 1% como significância, então a série não é estacionária.

#text(blue)[3)]
- Tendência: crescente por aproximadamente metade do período. Após a pandemia a tendência passou a ser descrescente.
- Sazonalidade: apesar de uma sazonalidade diária aparentemente inconsistente, anualmente há um crescimento forte durante o ano que decai nos meses finais. Assim, há um ciclo anual do preço da ação, mas não diário.
- Resíduo: persistência considerável, já que os desvios ficam presentes por meses. Além disso, o agrupamento desses desvios mostra um agrupamento das volatilidades da ação (a depender do recorte temporal, a volatilidade se altera drasticamente)

#text(blue)[4)]
- FAC: autocorrelação. Por definição, é a relação linear entre o Y#sub[t] com o Y#sub[t-n], onde n é qualquer valor entre o momento inicial e o final. Logo, ela inclui tanto a relação direta entre dois momentos, quanto a relação indireta dos momentos entre o início e o fim. No caso da AMBEV, a FAC dos preços em nível foi 0,989 caindo gradualmente, enquanto na primeira diferença foi novamente próxima de 0.

- FACP: autocorrelação parcial. Semelhantemente à FAC, a FACP analisa a relação linear de Y#sub[t] com Y#sub[t-k], entretanto, ela disconsidera os impactos indiretos dos momentos entre o início e o fim. Na ação, a FACP tem pico em lag = 1 mas logo em seguida desaparece para o preço em nível, enquanto para a primeira diferença ela é próxima de 0 por todo o período.

#text(blue)[5)]
- O modelo de autorregressão (AR(p)) usa um conjunto de períodos passados p fixo para prever os valores futuros da série.
- O modelo de média-móvel (MA(q)) também usa um conjunto de períodos passados q para prever os valores futuros da série, mas ele é móvel, assim, conforme os períodos vão passando, os lags usados na previsão vão acompanhando.

#text(blue)[6)] Pelo teste AIC, o modelo AR teve AIC = -1109.10, enquanto o AIC do modelo MA foi de 5293.21. Logo, o modelo AR teve menos perda de informação e, portanto, é o mais adequado para o contexto em questão.

A importância dos critérios de informação se dá pela possibilidade de avaliar o quão próximo as previsões feitas estavam da realidade. Especificamente, o AIC mede o quanto de informação foi perdida pelo modelo. Logo, menor AIC significa menor quantidade de informação perdida e portanto uma melhor qualidade do testado.

#text(blue)[7)] Pelo teste MSE, o modelo AR foi bem melhor que o modelo MA (0.08 < 2.73), mostrando o mesmo que o AIC. Isso porque, para mais de 2 passos, o modelo MA, ao usar apenas um choque como fator para prever o preço, torna-se aproximadamente constante, errando por mais de R\$1.50 durante quase todo o treino. Já o AR, ao partir do último valor observado, vai lentamente voltando à média (justamente pelo parâmetro de memória ser 0.99).
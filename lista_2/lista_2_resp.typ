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
#text()[= LISTA DE EXERCÍCIOS 1: RESPOSTAS]
#linebreak()

#emph(text(red)[=== EXERCÍCIOS DE ECONO I])
#text(blue)[1)] O ativo escolhido foi o do Bradesco e foi regredido em relação à taxa selic. Evidentemente, por se tratar de um banco, o Bradesco provavelmente possui consideráveis títulos pós-fixados indexados à Selic. Assim, é justificável a sensibilidade de 198.47, já que, um aumento da taxa implica maior resultado para o Bradesco.

#text(blue)[2)] A dispersão do gráfico apresentou uma grande concentração do valor da variação da selic (eixo x) em 0. Isso se deve porque a variação da selic acontece apenas em reuniões do COPOM que não acontecem diariamente, mas a cada 45 dias. Além disso, é visualmente justificável a alta sensibilidade encontrada por causa da relação positiva (reta para cima) mesmo com minúsculas alterações na selic (obs: eixo x na escala 10#super[-5])

#text(blue)[3)] Como feito no ex 1, o valor do coeficiente é positivo, correspondendo com a ideia de que o Bradesco possuiria títulos pós-fixados na Selic. Entretanto, ele não é significativo a 5 ($alpha$ < P-value).

Por definição, o R#super[2] é o quadrado da correlação. Assim, ele aponta diretamente a variabilidade percentual que a Selic causa na ação da Bradesco. O valor extremamente pequeno (0.1%) mostra que a BBDC4 possui outros fatores que explicam os outros 99.9% da variação do preço que não foram incluídos no modelo.

#text(blue)[5)] O principal problema de considerar apenas uma variável para modelar a sua previsão são as variáveis omitidas. Isso pode gerar outros problemas relacionados, como o Paradoxo de Simpson.

#text(blue)[6)] Entre os coeficientes, o $beta$#sub[0] quase não se alterou (0.000448 para 0.000493), o $beta$#sub[Selic] se alterou minimamente, de 198 para 193. Já o R#super[2] saiu de 1% para 6.6%.

A alteração no coeficiente da Selic se deu por dois motivos: o código teve que ter o seu período alterado pela impossibilidade de leitura do cambio para um momento maior que 5 anos. Ademais, mesmo que isso não tivesse ocorrido, ainda haveriam alterações no beta pelo fato de que as variáveis escolhidas não serem estritamente não correlacionadas (correl $!=$ 0).

Já o R#super[2] aumentou, já que agora não há apenas 1 fator tentando explicar as alterações na ação, mas 2, a Selic e o câmbio dólar-real.
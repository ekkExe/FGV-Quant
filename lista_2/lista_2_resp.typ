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
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
#set par(

)
#text()[= LISTA DE EXERCÍCIOS 1: RESPOSTAS]
#linebreak()

#emph(text(red)[=== EXERCÍCIOS DE PYTHON])


#text(blue)[1)]  O fechamento ajustado, diferentemente do fechamento nominal, "desconta" efeitos de ventos corporativos (dividendos, JCP, bonificações...),fazendo com que ele reflita somente o "ganho/perda" do capital real.

#text(blue)[4)] Os retornos simples e logarítmicos são distintos intuitivamente e matematicamente. Quanto à intuição financeira, enquanto o retorno simples mostra
literalmente ganhos ou perdas do investimento, o retorno logarítmico mostra o ritmo de crescimento/decrescimento do ativo (justamente pela simetria do ln).
Matematicamente, os retornos logarítmicos são mais simples de computar que o retorno simples para períodos longos, pois pela formula:
#align(center, $ln(P_t/P_(t-1)) = ln(P_t) - ln(P_(t-1))$) o cálculo logarítmico é uma soma, enquanto o simples é uma multiplicação.

#text(blue)[5)] O ativo com melhor desempenho (segundo o índice sharpe): BPAC11 (0.053). Ou seja, o Banco BTG teve a melhor premiação sobre o risco dentre os ativos.

#text(blue)[6)] A Matriz de Correlação mostra em cada célula a correlação entre o ativo da linha com o ativo da coluna.

Como resultado, as ações do Bradesco e do Itaú tiveram a maior correlação (83%) justamente por se tratarem de dois grandes bancos privados, sendo afetados por fatores quase idênticos. Todas as ações tiveram correlação média-alta com o IBOVESPA, já que o próprio benchmark é constituído também por essas ações.

Apesar da Petrobras e da Vale serem de commodities, a correlação é baixa (38%) pelas diferenças estruturais entre o mercado do petróleo e do ferro. A mesma lógica se aplica para o BTG. Mesmo com o Itaú e o Bradesco, a correlação se manteve em aproximadamente 55% por se tratar de um banco de investimentos, sendo estruturalmente diferente de bancos de varejo tradicionais.

No quesito da diversificação, a ação da Vale seria a melhor opção por ter a menor correlação média com os demais ativos.

#text(blue)[7)] Os pesos usados para a alocação foram definidos a partir da maximização do índice sharpe. Isso não teve um motivo financeiro por trás, mas que como foi trabalhado com o sharpe na questão 5, apenas reutilizei o código e adaptei para encontrar a alocação ótima. A alocação ótima foi: 0.0% BBDC4, 61.36%BPAC11, 0.0% ITUB4, 29.20% PETR4, 9.44% VALE3, com média 0.4098 e desvio padrão 0.3426.

#text(blue)[8)] A carteira montada atingiu retorno acumulado de 2184.40% no período analisado, enquanto o IBOVESPA atingiu 154.38%. Isso significa que o portfólio bateu o benchmark. Por lógica, isso aconteceu pois a alocação foi feita com base no índice sharpe, que mede o retorno adicional ao risco. Como os ativos com peso diferente de 0% tiveram melhor desempenho que o IBOVESPA (pelos exercícios anteriores), a carteira bateu o benchmark.

#linebreak()
#emph(text(red)[=== EXERCÍCIOS DE ESTATÍSTICA])

#text(blue)[1)] O Z-score, por definição, mede a quantos desvios padrões um determinado valor está da média. Numa interpretação geométrica, estamos calculando a distância do ponto em relação à média no eixo X. Assim, graficamente, o Z-score é uma curva normalizada, com média 0 e desvio padrão 1, de forma que, seja possível transformar os dados para uma mesma escala ("normalizar"), permitindo comparações entre diferentes distribuições.

#text(blue)[2)] Por definição, como as fórmulas são:
#linebreak()
#align(center, text()[ = $z = (macron(x) - mu)/(sigma/sqrt(n))$ $t = (macron(x) - mu)/(s/sqrt(n))$])

Asssim, a curva gaussiana possui apenas o numerador dependente de x, enquanto a t-student tem ambos o numerador e o denominador (já que s é uma função de x). Logo, quanto menor a amostra (n), maior a variação de s entre amostras, aumentando a chance de ocorrerem eventos mais distantes da média em relação à curva normal.

Portanto, é evidente que a curtose da curva t-student seja maior que a curva z-score (caudas mais grossas). 

#text(blue)[5)] No sentido estatístico, a assimetria e a curtose de uma distribuição medem, respectivamente, o grau de simetria em relação à média e a espessura da cauda dessa distribuição. Elas podem ser entendidas também como os 3o e 4o momentos da curva de distribuição.

Para uma curva normal, os valores padrão são: skewness = 0 (perfeitamente simétrica em relação à média) e kurtosis = 3.

No caso do portfólio, os valores foram -1.11 para o skewness e 28.44 para a kurtosis. O skewness negativo significa que, diferentemetne de uma curva normal, os eventos extremos negativos são mais frequentes/intensos que eventos extremos positivos. A diferença significativa da curtose aponta justamente que, num caso perfeito (de curva normal), os eventos extremos deveriam ser extremamente raros, mas que no portfólio, eles ocorrem com maior frequência que o previsto pela normal.

#text(blue)[7)] Máximo Drawdown mede a queda máxima percentual de um ativo ou portfólio em um período entre um pico e um vale.

No portfólio, o MDD foi de -60.16% no dia 23/03/2020. Isso significa que, durante todo o período, a pior queda sofrida no portfólio seria de -60.16%. Esse valor está relacionado com a assimetria e a curtose definidas anteriormente, em que, estatisticamente, as quedas deveriam ser mais acentuadas e mais frequentes.

#text(blue)[8)] Para o exercício, o alpha determinado foi de 1%. Isso pois, uma vez que a série dos retornos (tanto do portfólio quanto do IBOV) foi feito de forma diária, ao longo de 8 a 9 anos (2017-2026), a amostra passou de 2000 dados coletados. Assim, o erro padrão (denominador do teste t-student):
#linebreak()
#align(center, text()[$#text()[EP] = s/sqrt(n)$])

se aproxima de 0. Portanto, mínimos desvios passam a ter maior impacto no valor do t-student, aproximando cada vez mais os p-values de 0.

Logo a decisão final foi de diminuir o alpha para 1%, diferente do convencional 5%

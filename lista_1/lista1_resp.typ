#set text(font:"New Computer Modern Math")
#text()[= LISTA DE EXERCÍCIOS 1: RESPOSTAS - FGV QUANT]

1)  O fechamento ajustado, diferentemente do fechamento nominal, "desconta" efeitos de ventos corporativos (dividendos, JCP, bonificações...),fazendo com que ele reflita somente o "ganho/perda" do capital real.

4) Os retornos simples e logarítmicos são distintos intuitivamente e matematicamente. Quanto à intuição financeira, enquanto o retorno simples mostra
literalmente ganhos ou perdas do investimento, o retorno logarítmico mostra o ritmo de crescimento/decrescimento do ativo (justamente pela simetria do ln).
Matematicamente, os retornos logarítmicos são mais simples de computar que o retorno simples para períodos longos, pois pela formula:
#align(center, $ln(P_t/P_(t-1)) = ln(P_t) - ln(P_(t-1))$) o cálculo logarítmico é uma soma, enquanto o simples é uma multiplicação.

5) O ativo com melhor desempenho (segundo o índice sharpe): BPAC11 (0.053). Ou seja, o Banco BTG teve a melhor premiação sobre o risco dentre os ativos.

6) A Matriz de Correlação mostra em cada célula a correlação entre o ativo da linha com o ativo da coluna.
Como resultado, as ações do Bradesco e do Itaú tiveram a maior correlação (83%) justamente por se tratarem de dois grandes bancos privados, sendo afetados por fatores quase idênticos.
Todas as ações tiveram correlação média-alta com o IBOVESPA, já que o próprio benchmark é constituído também por essas ações.
Apesar da Petrobras e da Vale serem de commodities, a correlação é baixa (38%) pelas diferenças estruturais entre o mercado do petróleo e do ferro.
A mesma lógica se aplica para o BTG. Mesmo com o Itaú e o Bradesco, a correlação se manteve em ~55% por se tratar de um banco de investimentos, sendo estruturalmente diferente de bancos de varejo tradicionais.
No quesito da diversificação, a ação da Vale seria a melhor opção por ter a menor correlação média com os demais ativos.

7) Os pesos usados para a alocação foram definidos a partir da maximização do índice sharpe. Isso não teve um motivo financeiro por trás, mas que como foi trabalhado com o sharpe na questão 5, apenas reutilizei o código e adaptei para encontrar a alocação ótima. A alocação ótima foi: 0.0% BBDC4, 75.83% BPAC11, 0.0% ITUB4, 23.81% PETR4, 0.36% VALE3.

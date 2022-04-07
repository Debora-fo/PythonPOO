'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha


- Calcule a idade de uma pessoa. Para isso, obtenha a data atual completa (hoje)
e a data de nascimento completa, ou seja, considere dia, mês e ano.
Teste 1: Entre com a sua data de nascimento.
Teste 2: Nascimento: Dia 11, mês 10, ano 2000       Resposta: 19 anos
Teste 3: Nascimento: Dia 11, mês 6 , ano 2000       Resposta: 20 anos
Teste 4; Nascimento: Dia 30, mês  8, ano 2000       Resposta: 19 anos
Teste 5: Nascimento: Dia 10, mês  8, ano 2000       Resposta: 20 anos

a. Refaça sem digitar a data atual.
b. Refaça sem usar a variável dataatual.
c. Acrescente esta mensagem no final do programa, entre com seus dados:
Sintaxe: Nome Pessoa hoje (dd/mm/aaaa) você tem xx anos.
Exemplo: Paulo hoje (25/08/2020) você tem 27 anos.
d. Verifique se a pessoa digitou o ano de nascimento maior que o ano atual'''

dia_n = (int(input('Digite o dia do seu aniversário: ')))
mes_n = (int(input('Digite o mês do seu aniversário: ')))
ano_n = (int(input('Digite o ano em que você nasceu: ')))
dia = (int(input('Digite o dia de hoje: ')))
mes = (int(input('Digite o mês atual: ')))
ano = (int(input('Digite o ano atual: ')))

if mes_n > mes:
    idade = ano - ano_n -1
    print('Idade atual: ', idade)
elif mes_n == mes and dia_n > dia:
    idade = ano - ano_n -1
    print('Idade atual: ', idade)
else:
    idade = ano - ano_n
    print('Idade atual: ', idade)

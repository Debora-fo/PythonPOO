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

# b, c, d:

from datetime import date

nome = (str(input('Qual é o seu nome? ')))
dia_n = (int(input('Digite o dia do seu aniversário: ')))
mes_n = (int(input('Digite o mês do seu aniversário: ')))
ano_n = (int(input('Digite o ano em que você nasceu: ')))
if (ano_n > date.today().year):
    print('O ano de nascimento é maior que o ano atual')
else:
    if mes_n > date.today().month :
        idade = date.today().year - ano_n -1
        print('Idade atual: ', idade)
    elif mes_n == date.today().month and dia_n > date.today().day:
        idade = date.today().year - ano_n -1
        print('Idade atual: ', idade)
    else:
        idade = date.today().year - ano_n
        print('Idade atual: ', idade)

    print(nome,' hoje (', date.today().day, '/', date.today().month ,'/', date.today().year, ') você tem ', idade, ' anos.')
'''- Escreva o programa que leia o salário dos funcionários de uma empresa e calcule quantos
ganham:

-menos que cinco salários mínimos,
-na faixa de cinco (inclusive) até dez (exclusive)
-dez ou mais salários mínimos.

O valor do salário mínimo será fornecido pelo usuário. Na tela de saída, além da quantidade de funcionários em
cada faixa salarial, informe também o valor total da folha de pagamento da empresa.

Teste 1: 2000, 6000, 12000     Saída: Menos 5: 1, Meio: 1, Mais 10:1, Folha: 20000'''

ct_menos_5_sm = 0
ct_5_a_10_sm = 0
ct_mais_10_sm = 0
total = 0

salario_minimo = float(input("Digite o valor do salário mínimo: "))

print('Digite [0] para finalizar')

while True:
    salario = float(input("Digite o salario do funcionário: "))

    if salario == 0:
        break

    if salario < 5 * salario_minimo:
        ct_menos_5_sm += 1
    elif salario < 10 * salario_minimo:
        ct_5_a_10_sm += 1
    else:
        ct_mais_10_sm += 1

    total = total + salario

if total == 0:
    print("Nenhum dado digitado")
else:
    print("Ganham menos que cinco salários mínimos:", ct_menos_5_sm)
    print("Estão na faixa de cinco até dez salários mínimos:", ct_5_a_10_sm)
    print("Ganham dez ou mais salários mínimos", ct_mais_10_sm)
    print("Folha de pagamento: R$", total)

'''ALTERAÇÕES
a. Digite a condição de saída de primeira e mostre a mensagem:
   "Nenhum dados digitado."
b. Elimine a redundânacia no if ... elif ... else. Fica ais simples e mais rápido.'''
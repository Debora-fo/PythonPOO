# Avaliação 1 - Lógica de Programação
# Aluna: Débora Ferreira de Oliveira
# RA: 22051517

# Questão 1
'''
while True:
    numero = int(input("Digite o número da conta: "))
    saldo = int(input("Digite o saldo atual: "))
    operacao = str(input("Digite o tipo da operação a ser realizada [d] ou [r] (depósito ou retirada): "))
    valor = int(input("Digite o valor da operação: "))

    if operacao == 'd':                 #Se for operação de depósito
        total = saldo + valor           #Adiciona o valor para a conta
    else:                               #Se for operação de retirada
        total = saldo - valor           #Retira o valor da conta

    break

print("Número da conta bancária: ", numero)
print("Novo saldo: ",total)
'''

# Questão 2
'''
soma = 0
ct = 0
maior = 0
menor = 10

print('Digite [ -1 ] para sair')

while True:
    nota = float(input("Digite a nota do aluno " + str (ct + 1) + ": "))

    if nota == -1:
        break

    if nota > maior:
        maior = nota

    if nota < menor:
        menor = nota

    ct = ct + 1
    soma = soma + nota

if ct != 0:
    media = soma / ct
    print("Média da turma de ",ct, " alunos é  %.2f" %(media))
    print("A menor nota foi: ", menor)
    print("A maior nota foi: ", maior)

else:
    print("ZeroDivisionError: division by zero")
'''

# Questão 3
'''
ct = 0
soma = 0
mais_velho= 0

print('Digite [ -1 ] para sair')

while True:
    idade = float(input("Digite a idade da pessoa " + str (ct + 1) + ": "))
    
    if idade == -1:
        break

    peso = float(input("Digite o peso da pessoa " + str (ct + 1) + ": "))

    if idade > mais_velho:
        mais_velho = idade

    ct = ct + 1
    soma = soma + peso

print("Quantidade de pessoas analisadas: ", ct)
print("Soma do peso das pessoas: ", soma)
print("Idade da pessoa mais velha: ", mais_velho)
'''




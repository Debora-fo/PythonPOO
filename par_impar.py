'''- Elabore o programa que verifique se o valor inteiro fornecido pelo usuário é
par ou ímpar.
Analise o problema e verifique quais são os dados que o usuário precisa fornecer.

Teste 1: valor = 7              Saída: "Número ímpar."
Teste 2: valor = 8              Saída: "Número par."
'''
valor = int(input("Digite um valor: "))
resto = valor % 2

if valor % 2 == 0:
    print("O número ", valor, " é par")
else:
    print("O número ", valor, " é ímpar")

print("Resto =", resto)

if valor % 5 ==0:
    print("O número ", valor, " é divisível por 5")
else:
    print("O número ", valor, " não é divisível por 5")



'''Alterações:
a. Acrescente na tela de saída o número digitado e o valor do resto da divisão por 2.    
b. Acrescente também se o valor fornecido é divisível por cinco. '''
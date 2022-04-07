'''- Construa o programa que leia dois valores quaisquer e mostre
o maior deles ou mostre a mensagem “Os valores são iguais.”

Teste 1: Entrada: 5 e 10                        Saída: O maior valor é 10
Teste 2: Entrada: 5 e 5                         Saída: “Os valores são iguais.”
'''
valor1 = int(input("Digite o primeiro número:"))
valor2 = int(input("Digite o segundo número:"))

if valor1 > valor2:
    print("O número ", valor1, " é maior que o número", valor2)
elif valor2 > valor1:
    print("O número ", valor2, " é maior que o número", valor1)
else:
    print("Os valores são iguais.", valor1, " e ", valor2)

'''ALTERAÇÕES:
a. Se eles forem diferentes, mostre os valores digitados na ordem decrescente.
b. Se eles forem iguais, mostre a mensagem e o valor digitado.
'''
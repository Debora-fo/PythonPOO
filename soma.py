'''- Elabore o programa que calcule a soma de dois valores inteiros que serão fornecidos pelo usuário.
Teste: Entrada: valores 1 e 2.      Saída: 3
- Passos:
Entrada de dados
Processamento
Saída
'''

#Entrada de dados

valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))

#Processamento

soma = valor1 + valor2

#Saída

print("O resultado da soma é: ", soma)

'''
ALTERAÇÕES:
a. No final do método, acrescente a subtração dos valores
   lidos e mostre o resultado.
b. No final do método, acrescente a multiplicação dos dois valores lidos e mostre o resultado.
c. No final do método, leia mais um valor inteiro, ou seja, o terceiro valor inteiro.
d. No final do método, acrescente a soma dos três valores lidos e mostre o resultado.
'''

# Alteração a
subtracao = valor1 - valor2
print("O resultado da subtração é: ", subtracao)

# Alteração b
multiplicacao = valor1 * valor2
print("O resultado da multiplicação é: ", multiplicacao)

# Alteração c
valor3 = int(input("Insira o terceiro valor: "))

# Alteração d
soma2 = valor1 + valor2 + valor3
print("O resultado da soma dos 3 valores é: ", soma2)


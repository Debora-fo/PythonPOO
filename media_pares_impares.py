'''- Construa o programa que calcule a média aritmética dos números pares e
a média aritmética dos números ímpares. O usuário fornecerá os valores
de entrada que pode ser um número qualquer par ou ímpar.
A condição de saída será o número -1.

Teste 1:   Entrada: 1, 2 e -1.          Saída: Média pares: 2
                                               Média ímpares: 1
Teste 2:   Entrada: 1, 2, 5 e -1.       Saída: Média pares: 2
                                               Média ímpares: 3
Teste 3:   Entrada: 1, 5 e 1-.          Saída: Não tem número par
                                               Média ímpares: 3
Teste 4:   entrada: 2, 4 e -1.          Saída: Média pares: 3
                                               Não tem número ímpar
Teste 5:   Entrada: -1                  Saída: Não tem número par
                                               Não tem número ímpar '''

soma_par = 0
soma_impar = 0

ct_par = 0
ct_impar = 0

print('Digite ( -1 ) para sair')

while True:
    numero = int(input("Digite um número: "))

    if numero == -1:
        break

    if numero % 2 == 0:
        soma_par = soma_par + numero
        ct_par = ct_par + 1
    else:
        soma_impar = soma_impar + numero
        ct_impar = ct_impar + 1

if ct_par != 0:
    media_par = soma_par/ct_par
    print("Média dos pares: %.2f" % media_par)
    print("Existem ", ct_par, " números pares")
    print("Porcentagem de números pares: ", (ct_par * 100)/(ct_par+ct_impar), "%" )
else:
    print("Não existem números pares")

if ct_impar != 0:
    media_impar = soma_impar/ct_impar
    print("Média dos ímpares: %.2f" % media_impar)
    print("Existem ", ct_impar, " números ímpares")
    print("Porcentagem de números ímpares: ", (ct_impar * 100) / (ct_par + ct_impar), "%")

else:
    print("Não existem números ímpares")

print("Quantidade de números digitados: ", ct_par +ct_impar)
'''
a. Mostre também a quantidade de números pares.
b. Mostre também a quantidade de números ímpares.
c. Mostre também a quantidade de números digitados.
d. Calcule e mostre a porcentagem dos números pares.
e. Calcule e mostre a porcentagem dos números ímpares.'''
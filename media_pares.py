'''- Construa o programa que calcule a média aritmética dos números pares.
O usuário fornecerá os valores de entrada que pode ser um número qualquer par ou ímpar.
A condição de saída será o número 0 (zero).

Teste 1:    valor: 1, 2 e 0.            Resposta: Média 2
Teste 2:    valor: 1, 2, 3, 4 e 0.      Resposta: Média 3
Teste 3:    valor: 1, 3 e 0.            Resposta: Não pode ser dividido por 0 (zero)'''

soma = 0
ct = 0

print("Digite [ 0 ] para sair")

while True:
    numero = int(input("Digite um número: "))

    if numero == 0:
        break

    if numero % 2 == 0:
        soma = soma + numero
        ct = ct + 1


if ct != 0:                                                     # a.
    media = soma / ct
    print("A media de todos os pares recebidos é: %.4f" % (media))
    print("Quantidade de números digitados: ", soma-1 )
else:
    print ('Não posso dividir por zero')





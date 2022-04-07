"""
- Construa o programa que encontre o menor valor e o maior valor de um
conjunto de valores inteiros digitados pelo usuário. A condição de saída
será o valor -1 que não será considerado na pesquisa.

Teste 1:    entrada: 1, 3, 2, -1         Saída: Menor: 1      Maior: 3
Teste 2:    entrada: 1, 2, 3, -1         Saída: Menor: 1      Maior: 3
Teste 3:    entrada: 3, 2, 1, -1         Saída: Menor: 1      Maior: 3 """

menor = 999999
maior = -999999
ct = 0
soma = 0

print('Digite [ -1 ] para sair')

while True:
    valor = int(input("Digite um valor: "))
    soma = valor + soma

    if valor == -1:
        break

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

    ct = ct + 1


if ct == 00 and valor == -1:
    print("Nenhum valor válido recebido")
else:
    print("Menor:", menor)
    print("Maior:", maior)
    print("Quantidade de valores digitados", ct )
    print("Soma dos valores digitados: ", soma + 1)
    print("Média dos valores digitados: ", (soma + 1)/ct)


''' ALTERAÇÕES:
a. Mostre também a quantidade de valores digitados.
b. Mostre também a soma de valores digitados.    
c. Digite o valor -1 de primeira e mostre somente esta mensagem: 
    "Não foi digitado nenhum valor."          
d. Calcule e mostre a média dos valores digitados -----  DICAS ABAIXO:
ct = 0                              # Antes do while            # a.
    ct = ct + 1                     # Dentro do while
print ('Quantidade: ', ct)          # Depois do while           # a.
soma = 0                            # Antes do while            # b.
    soma = soma + valor             # Dentro do while
print ('Soma: ', soma)              # Depois do while           # b.
if ct != 0:                                                     # c.
    print("Menor: ", menor)
    print("Maior:" , maior)
else:
    print ("Não foi digitado nenhum valor.")                    # c.
if ct != 0:                                                     # d.
    print("Menor: ", menor)
    print("Maior:" , maior)
    media = soma / ct
    print("Média:" , media)                                     # d.
else:
    print ("Não foi digitado nenhum valor.")  

'''
'''- Construa o programa que encontre o menor valor de um conjunto de valores inteiros
digitados pelo usuário. Use o valor 0 (zero) na condição de saída que não será
considerado na pesquisa.

Teste 1: Entrada: valor: 2, 1, 3, 0         Resposta: Menor = 1

Teste 2: Entrada: valor: 1, 3, 2, 0         Resposta: Menor = 1  '''

ct = 0
menor_valor = 99999999
soma = 0

print('Digite 0 (zero) para sair')



while True:
    valor = int(input("Digite um valor: "))
    soma = valor + soma

    if valor == 0:
        break
    if valor < menor_valor:
        menor_valor = valor

    ct = ct + 1


if ct == 0:
    print("Nenhum valor válido recebido")
else:
    print("O menor valor é: ", menor_valor)
    print("Quantidade de valores digitados", ct )
    print("Soma dos valores digitados: ", soma)




'''     ALTERAÇÕES:
a. Mostre também a quantidade de valores foram digitado, no final.
    "Não foi digitado nenhum valor."
c. Mostre a soma dos valoes digitados.         

----- DICA:
ct = 0                                              # Antes do while        # a.
ct = ct + 1                                         # Dentro do while, no final
print('Quantidade de valores digitados: ', ct)     # Depois do while  
if ct == 0:                     # Mostra o resultado apropriado           # b.
    print("Nenhum valor válido recebido")
else:
    print("O menor valor é: ", menor_valor)                                     
    print ('Quantidade de valores digitados: ', ct)                        
soma = 0                                                                   # c.
soma = soma + valor      # Dentro do while
    print ('Soma dos valores digitados: ', soma)                           
'''
'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

-- Desenvolva o programa que leia vários números, armazene-os numa lista e
mostre estas informações:
- Quantidade de elementos armazenados na lista;
- Soma dos valores da lista;
- Maior valor da lista;
- Menor valor da lista;
- Leia um valor e verificar se ele está na lista;
- No item anterior, mostre também a posição (índice) do valor encontrado na pesquisa;
- Mostre a lista na ordem crescente. Teste;
- Insira (acrescente) o valor 33 na posição (índice) 1 da lista. Teste;
- Mostre a lista na ordem decrescente. Teste;
- Média dos valores da lista;
- Porcentagem dos números maiores que dez na lista.                      '''

lista=[]

print('Quando desejar parar de inserir números digite 0')

while True:
    l = (int(input('Digite um número: ')))
    lista.append(l)
    if l == 0:
        break

lista.remove(0)

print(lista)
print('Quantidade de números na lista:',len(lista))
print('Soma dos valores da lista:',sum(lista))
print('Maior valor da lista:',max(lista))
print('Menor valor da lista:',min(lista))

num = (int(input('Qual número você quer pesquisar? ')))
if num in lista:
    print('Número encontrado')
    print('O número',num, 'está na posição',lista.index(num))
else:
    print('Esse número não está na lista.')

lista.sort()
print('Lista na ordem crescente:',lista)

lista.insert(0,33)
print(lista)

lista.sort(reverse=True)
print('Lista na ordem decrescente:',lista)

media = sum(lista)/len(lista)
print('Média dos valores da lista:',media)

maiorq10 = []
for y in lista:
    if y > 10:
        maiorq10.append(y)

porcentagem = len(maiorq10)/len(lista)*100

print('Porcentagem dos números maiores que dez na lista:', porcentagem)



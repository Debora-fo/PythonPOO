'''
#Questão 1

lista=[]
pares = []
impares = []

print('Quando desejar parar de inserir números digite 0')

while True:
    l = (int(input('Digite um número: ')))
    lista.append(l)
    if l == 0:
        break
    if l % 2 == 0:
        pares.append(l)
    else:
        impares.append(l)

lista.remove(0)

print(lista)
media = sum(lista)/len(lista)

print('Média dos valores da lista:',media)
print('Quantidade de valores pares:',len(pares))
print('Porcentagem de valores impares:', (len(impares)*100/len(lista)),'%')
'''

'''
#Questão 2

lista = []

n = int(input('Quantos números deseja inserir?'))
while True:
    l = (int(input('Digite um número: ')))
    print(l * 2)
    lista.append(l)
    if len(lista) == n:
        break
print('Maior valor da lista:',max(lista))
print('Menor valor da lista:',min(lista))
'''

'''
#Questão 3

- Desenvolva o programa que leia vários números, armazene-os numa lista e
mostre estas informações:
- Quantidade de elementos armazenados na lista;
- Soma dos valores da lista;
- Maior valor da lista;
- Menor valor da lista;
- Leia um valor e verificar se ele está na lista;
'''

'''
#Desenvolvimento do enunciado criado na questão 3

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
'''
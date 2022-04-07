'''
#Questão 1:

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if __name__ == '__main__':
    def maximo():
        if num1 == num2 == num3:
            print('Os 3 números são iguais')
        elif num1 >= num2 and num1 >= num3:
            print('O maior número é',num1)
        elif num2 >= num1 and num2 >= num3:
            print('O maior número é',num2)
        else:
            print('O maior núumero é: ',num3)

maximo()
'''
#---------------------------------------------------------------------------------------------------------
'''
#Questão 2:

lista=[]

print('Quando desejar parar de inserir números digite 0')

while True:
    l = (int(input('Digite um número: ')))
    lista.append(l)
    if l == 0:
        break

lista.remove(0)

print(lista)

num = (int(input('Qual número você quer pesquisar? ')))
if num in lista:
    print('Número encontrado')
    print('O número',num, 'está na posição',lista.index(num))
else:
    print('Esse número não está na lista.')

lista.sort()
print('Lista na ordem crescente:',lista)

lista.insert(1,33)
print(lista)

lista.sort(reverse=True)
print('Lista na ordem decrescente:',lista)

media = sum(lista)/len(lista)
print('Média dos valores da lista:',media)

maior10 = []
for y in lista:
    if y > 10:
        maior10.append(y)

porcentagem = len(maior10)/len(lista)*100

print('Porcentagem dos números maiores que dez na lista:', porcentagem)


#Questão 1 G: Receba e exclua um valor da lista, se o valor indicado não se encontra na lista informe ao usuário.

print(lista)

ex = (int(input('Qual número você deseja excluir da lista?')))
if ex in lista:
    lista.remove(ex)
    print('Número excluído')
    print(lista)
else:
    print('Esse número não está na lista.')
'''
#---------------------------------------------------------------------------------------------------------
#Questão 3

class Livro:
    def __init__(self, titulo, autor, paginas, preco=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.preco = preco

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_paginas(self):
        return self.paginas

    def set_preco(self):
        return self.preco

    def mostra_dados(self):
        print('Título', self.titulo)
        print('Autor', self.autor)
        print('Páginas', self.paginas)
        print('Preço', self.preco)

    def retorna_dados(self):
        dados = str(self.titulo) + ' - ' + str(self.autor) + ' - ' + int(self.paginas) + ' - ' + float(self.preco)
        return dados

    def aumento_preco(self):
        self.preco += self.preco* pct / 100

if __name__ == '__main__':
    livro1 = Livro('Titulo','Nome', 100, 50)
    print('Livro 1: ')
    print('Título: ',livro1.titulo)
    print('Autor: ', livro1.autor)
    print('Páginas: ', livro1.paginas)
    print('Preço: ', livro1.preco)

    livro1.mostra_dados()

    print(livro1.retorna_dados())

    print('Preço: ', livro1.set_preco('Novo preço'))

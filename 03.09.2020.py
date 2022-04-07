'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha
- CRUD
- CRUD (acrônimo do inglês Create, Read, Update and Delete) são as quatro
operações básicas (inclui, consulta, atualiza e apaga os dados) utilizadas
em bases de dados relacionais (RDBMS) fornecidas aos usuários do sistema.
- Desenvolva o programa usando lista com as funções main com repetição, menu,
create, read, update e delete para simular um CRUD. Neste exercício, use nomes.
- A função main gerencia o programa usando uma estrutura de repetição,
ou seja, todas as funções serão chamadas da função main.
- A função menu não recebe nada, apresenta as quatro operações do CRUD,
lê a opção do usuário e retorna a opção digitada pra função main:
    [c] - Create (inserir um item)
    [r] - Read (mostrar toda a lista)
    [u] - Update (substituir um item)
    [d] - Delete  (remover um item)
    [e] - Exit (sair)
    Opção:
- A função create não recebe nada e não retorna nada. Lê um nome e insere na lista.
- A função read não recebe nada e não retorna nada. Mostra todos os itens da lista.
- A função update não recebe nada e não retorna nada. Lê os dados necessários
(índice e o novo nome) e substitui (altera) um item da lista.
- A função delete não recebe nada e não retorna nada. Lê o item (nome) que será
excluído e apaga da lista.                                                          '''

def menu():
    print('Menu: ')
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - Delete')
    print('[e] - Exit')
    opcao = input('Opção: ').lower()
    return opcao

def create():
    nome = input('Nome: ')
    lista.append(nome)

def read():
    if len(lista) != 0:
        print(lista)
    else:
        print('Lista vazia.')

def update():
    if len(lista) == 0:
         print('Lista vazia.')
    elif len(lista) != 0 :
        x = int(input('Qual posição? '))
        if x <= len(lista):
            novo = input('Novo nome: ')
            lista.pop(x)
            lista.insert(x, novo)
            print('Nome atualizado')
        else:
            print('Posição não existe')

def delete():
    if len(lista) == 0:
         print('Lista vazia.')
    elif len(lista) != 0:
        print(lista)
        y = input('Que nome deseja deletar?')
        if y not in lista:
            print('Esse nome não está na lista')
        else:
            lista.remove(y)
            print('Nome deletado')

if __name__ == '__main__':
    lista = []
    while True:
        m = menu()
        if m == 'c':
            create()
        elif m == 'r':
            read()
        elif m == 'u':
            update()
        elif m == 'd':
            delete()
        else:
            break

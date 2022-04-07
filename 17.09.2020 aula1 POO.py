'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha

- Sintaxe:       POO em Python
class NomeClasse:                                    # class NomeClasse (object):
    def __init__ (self, p_1, p_2, ...):              # Método construtor
        self.nome_atributo1 = p_1                    # Atributos
        self.nome_atributo2 = p_2
        . . .
    def nome_metodo (self):                          # Outros métodos da classe
        # script
        [return]
if __name__ == '__main__':                            # mai <tab>
    nome_objeto1 = NomeClasse(a_1, a_2, ...)        # Cria (instancia) o primeiro objeto da classe
    nome_objeto2 = NomeClasse(a_1, a_2, ...)        # Cria (instancia) o segundo objeto da classe
    . . .
    print ("Valor do atributo x: ", nome_objeto1.x)  # nome_objeto.nome_atributo
    nome_objeto1.nome_atributo = novo_valor          # alterar valor do atributo
    nome_objeto1.nome_metodo()                       # Modelo pra chamar método da classe
    nome_objeto2.nome_metodo()                       # Modelo pra chamar método da classe
----------------------- Com base no modelo acima, implemente estes itens:
1- Crie a classe Aluno
2- Crie o construtor da classe com  os atributos: nome, mensalidade, idade
3- No main, crie um objeto (instância) da classe
4- Mostre os dados do objeto da classe, aluno1. Não use o método get
5- No main, crie mais um objeto (instância) da classe, aluno2
6- Mostre os dados do objeto da classe, aluno2
7- Altere a mensalidade do aluno1 para 850 reais e teste.
8- Crie o método mostra_dados, mostre os atributos nome e idade.
9- Testes o método para os dois objetos.
10- Crie o método retorna_dados, retorne os atributos nome e idade concatenados.
11- Testes o método para os dois objetos.
12- Crie o método pode_cnh, verifica se tem 18 anos ou mais. Mostre mensagem "Pode." ou "Não pode.".
13- No main, crie mais um objeto (instância) da classe, aluno3 com menos de 18 anos.
14- Testes o método pode_cnh para os três objetos (instâncias) da classe.
15- Crie o método aumento, ele recebe um valor que será acrescido a mensalidade.
16- Teste o método para pelo menos uma instância, um aluno
17- Crie o método aumento_2, ele não recebe nada e lê o valor do aumento dentro do método. Teste '''



class Aluno:
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def mostra_dados(self):
        print(f'Nome: {self.nome} - Idade: {self.idade}')

    def retorna_dados(self):
        dados = self.nome + ' - ' + str(self.mensalidade) + ' - ' + str(self.idade)
        return dados

    def pode_cnh(self):
        if self.idade>= 18:
            print('Pode tirar CNH')
        else:
            print('Não pode tirar CNH')

    def aumento(self, valor):
        self.mensalidade += valor

    def aumento_2(self):
        valor_aumento = int(input('Valor do aumento: '))
        self.mensalidade += valor_aumento



if __name__ == '__main__':
    aluno1 = Aluno ('Maria', 600, 18)
    print(f'Nome: {aluno1.nome} - Mensalidade: {aluno1.mensalidade} - Idade: {aluno1.idade}')

    aluno2 = Aluno ('Paulo', 400, 16)
    print(f'Nome: {aluno2.nome} - Mensalidade: {aluno2.mensalidade} - Idade: {aluno2.idade}')

    aluno3 = Aluno ('Rita', 500, 12)

    aluno1.mensalidade = 850
    print('Mensalidade: ', aluno1.mensalidade)

    aluno1.mostra_dados()
    aluno2.mostra_dados()

    print(aluno1.retorna_dados())
    print(aluno2.retorna_dados())

    aluno1.pode_cnh()
    aluno2.pode_cnh()
    aluno3.pode_cnh()

    aluno1.aumento(100)
    print(aluno1.retorna_dados())

    aluno2.aumento_2()
    print(aluno2.retorna_dados())





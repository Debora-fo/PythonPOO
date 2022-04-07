'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha

Sintaxe:    POO em Python com gets e sets
class NomeClasse (object):
    def __init__ (self, p_1, p_2, ...):     # Método construtor
        self.nome_atributo1 = p_1           # Atributos
        self.nome_atributo2 = p_2
        ...
    def get_nome_atributo1 (self):          # Modelo do método get (retorna valor do atributo)
        return self.nome_atributo1
    def set_nome_atributo1 (self, valor):   # Modelo do método set (altera valor do atributo)
        self.nome_atributo1 = valor
    def outro_metodo (self):                # Outros métodos da classe (métodos fundionais)
        ...
        [return ...]
if __name__ == '__main__':                      # mai <tab>
    nome_objeto1 = NomeClasse(a_1, a_2, ...)    # Cria (instancia) o primeiro objeto da classe
    nome_objeto2 = NomeClasse(a_1, a_2, ...)    # Cria (instancia) o segundo objeto da classe
    . . .
    r = nome_objeto1.get_nome_atributo1()       # Consulta um atributo
    print(r)
    nome_objeto1.set_nome_atributo1(novo_valor) # Altera um atributo
------------------------------- Com base no modelo acima, implemente estes itens:
1- Crie a classe Aluno.
- Crie o construtor da classe com os atributos: nome, mensalidade, idade
- Crie os métodos gets e sets
- No main, crie pelo menos dois objetos da classe Aluno. Teste
5- Use os métodos gets e sets para os objetos criados
- Crie o método mostra_dados. Mostra os dados (atrigutos) dentro do método. Teste.
- Refaça o anterior sem usar o nome do atributo, crie o método mostra_dados_2. Teste
- Crie o método retorna_dados, retorne todos os dados (atributos) concatenados.Teste
- Crie o método aumento_mensalidade_valor, ele recebe o valor do aumento. Teste
10- Crie o método aumento_mensalidade_porcentagem (Recebe: 10%, 15% etc.). Teste
---
11- Altere o construtor com estes valor default: Mensalidade = 1000 e idade = 0.
- No main, crie o objeto aluno3 da classe Aluno passando apenas o nome. Teste
- No main, crie o objeto aluno4 da classe Aluno passando o nome e a mensalidade. Teste
14- No main, crie o objeto aluno5 da classe Aluno passando somente o nome e a idade.
    não passe o argumento mensalidade. Teste                                           ----- '''

class Aluno:
    def __init__(self, nome, mensalidade=1000, idade=0):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_mensalidade(self):
        return self.mensalidade

    def get_idade(self):
        return self.idade

    def set_nome(self, n):
        self.nome = n

    def set_mensalidade(self,valor):
        self.mensalidade = valor

    def set_idade(self,i):
        self.idade = i

    def mostra_dados(self):
        print('\nNome: ', self.nome)
        print('Mensalidade: ', self.mensalidade)
        print('Idade: ', self.idade)

    def mostra_dados_2(self):
        print('\nNome: ', self.get_nome())
        print('Mensalidade: ', self.get_mensalidade())
        print('Idade: ', self.get_idade())

    def retorna_dados(self):
        dados = self.nome + ' - ' + str(self.mensalidade) + ' - ' + str(self.idade)
        return dados

    def aumento_mensalidade_valor(self, v):
        self.mensalidade += v

    def aumento_mensalidade_porcentagem(self, pct):
        self.mensalidade += self.mensalidade * pct / 100


if __name__ == '__main__':
    aluno1 = Aluno('Paulo', 1000, 21)
    aluno2 = Aluno('Carla', 900, 20)

    print("Aluno 1:")
    print('Nome: ', aluno1.get_nome())
    print('Idade: ', aluno1.get_idade())
    print('Mensalidade: ', aluno1.get_mensalidade())

    print("\nAluno 2:")
    print('Nome: ', aluno2.get_nome())
    print('Idade: ', aluno2.get_idade())
    print('Mensalidade: ', aluno2.get_mensalidade())

    aluno1.set_idade(18)
    print('\nIdade: ', aluno1.get_idade())

    aluno1.mostra_dados()
    aluno2.mostra_dados()

    aluno1.mostra_dados_2()
    aluno2.mostra_dados_2()

    print('Dados concatenados: ', aluno1.retorna_dados())
    print('Dados concatenados: ', aluno2.retorna_dados())

    aluno1.aumento_mensalidade_valor(110)
    print('Nova mensalidade', aluno1.get_mensalidade())
    aluno1.mostra_dados_2()

    aluno2.aumento_mensalidade_porcentagem(10)
    aluno2.mostra_dados_2()
    print('Nova mensalidade', aluno2.get_mensalidade())

    aluno3 = Aluno('Ailton')
    aluno3.mostra_dados()

    aluno4 = Aluno('Ana', 800)
    aluno4.mostra_dados()

    aluno5 = Aluno('Rogério', idade=31)
    aluno5.mostra_dados()

    aluno6 = Aluno(idade=30, nome='Vinicius')
    aluno6.mostra_dados()








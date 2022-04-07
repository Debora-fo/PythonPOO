'''
#1:
lista=[]

print('Quando desejar parar de inserir números digite 0')

while True:
    l = (int(input('Digite um número: ')))
    lista.append(l)
    if l == 0:
        break

lista.remove(0)

print(lista)

media = sum(lista)/len(lista)
print('Média dos valores da lista:',media)

lista.insert(1,media)
print(lista)

#método 1
#lista.insert(1,77)
#print(lista)

#método 2
lista.pop(1)
lista[1] = 77
print(lista)
'''

'''
#2:
class TimeDeFutebol:
    qtd_times = 0

    @classmethod
    def mostra_qtd_times(cls):
        print(f'{cls.qtd_times} times')

    @classmethod
    def get_qtd_times(cls):
        s = f'{cls.qtd_times} times'
        return s

    def __init__(self, nome = 0, estado = 0, títulos = 0 ,valor = 0):
        self.nome = nome
        self.estado = estado
        self.titulos = títulos
        self.valor = valor

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def mostra_dados(self):
        print('\nNome: ', self.nome)
        print('Estado: ', self.estado)
        print('Títulos: ', self.titulos)
        print('Valor: ', self.valor)

    def set_valor(self, novo_valor):
        if novo_valor > 0:
            self.valor = novo_valor
        else:
            print("Valor inconsistente, valor negativo")

if __name__ == '__main__':
    time1 = TimeDeFutebol('Vila', 'Goiás', 2, 10000)
    time2 = TimeDeFutebol('Flamengo', 'São Paulo', 6, 20000)
    time3 = TimeDeFutebol('São Paulo', 'São Paulo', 10, 30000)

    time1.mostra_dados()

    time1.set_nome('Goiás')
    print('Novo nome:', time1.get_nome())

    time1.mostra_dados()

    TimeDeFutebol.mostra_qtd_times()
    print('Quantidade:', TimeDeFutebol.get_qtd_times())

    time4 = TimeDeFutebol('Santos')
    time4.mostra_dados()

    time5 = TimeDeFutebol('Bahia', títulos=4)
    time5.mostra_dados()

    time6 = TimeDeFutebol('Brasiliense', valor=8000)
    time6.mostra_dados()
 '''

'''3. Desenvolva um sistema usando POO com herança para trabalhar com as classes Veiculo e Carro. 
Na superclasse use pelo menos dois atributos e na subclasse use os dois atributos comuns da superclasse mais pelo
menos um atributo específico da subclasse.
Crie os construtores com valores default e crie os métodos gets e sets nas duas classes necessários fazer os seus
testes.
Crie um método funcional na superclasse que pode ser usado também pelos objetos da subclasse.
Crie outro método funcional na superclasse que será usado pelos objetos da superclasse e um método sobrescrito
na subclasse que será usado pelo objeto da subclasse.
No método main, instancie pelo menos um objeto da superclasse e um objeto da subclasse e teste os métodos desenvolvidos.'''

#3:

class Veiculo:
    def __init__(self, nome, ano = 0):
        self.nome = nome.title()
        self.ano = ano

    def __str__(self):
        s=self.nome + " " + str(self.ano)
        return s

class Carro(Veiculo):
    def __init__(self, nome, ano = 0, km = 0):
        super().__init__(nome, ano)
        self.km = km

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_ano(self):
        return self.ano
    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def get_km(self):
        return self.km
    def set_km(self, novo_km):
        self.km = novo_km

    def mostra_dados(self):
        print('\nNome: ', self.nome)
        print('Ano: ', self.ano)
        print('Quilometragem: ', self.km)

if __name__ == '__main__':

    carro1 = Carro('Megane', 2019, 2000 )
    carro2 = Carro('Astra', 2010)
    print(Veiculo.__str__(carro1))
    print(Veiculo.__str__(carro2))
    carro1.mostra_dados()
    carro2.mostra_dados()
    veiculo1 = Veiculo('Biz', 2020, )
    veiculo1.mostra_dados()
    print(Veiculo.__str__(veiculo1))

























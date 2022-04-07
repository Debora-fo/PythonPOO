'''   UniCEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha
       POO em Python
class NomeClasse (object):
    def __init__ (self, p_1="nome1", p_2=valor2):   # Método construtor
        self.nome_atributo1 = p_1                   # Atributos da classe
        self.nome_atributo2 = p_2
    def get_nome_atributo1 (self):                  # Modelo do método get (retorna valor do atributo)
        return self.nome_atributo1
    def set_nome_atributo1 (self, valor):           # Modelo do método set (altera valor do atributo)
        self.nome_atributo1 = valor
    def outro_metodo (self):                        # Outros métodos da classe
        . . .
        [return ...]
if __name__ == '__main__':                      # main <tab>
    nome_objeto1 = NomeClasse(a_1, a_2)         # Cria (instancia) o primeiro objeto da classe
    nome_objeto2 = NomeClasse(a_1, a_2)         # Cria (instancia) o segundo objeto da classe
    nome_objeto3 = NomeClasse()                 # Cria (instancia) o terceiro objeto da classe
    print ("Valor do atributo x: ", nome_objeto1.x) # nome_objeto . nome_atributo
------ Com base no modelo acima, implemente estes itens:
1- Crie a classe Produto
- Crie o construtor da classe com os atributos: nome, vlr_compra, vlr_venda, qtd_estoque, qtd_minima
3- No main, crie o primeiro objeto da classe com estes dados: Arroz, 15.00, 19.50, 67, 20. Teste
- Crie os métodos gets e sets dos atributos: nome, qtd_estoque e qtd_minima.  Teste.
5- No main, consulte os dados do objeto criado.
- Altere a quantidade minima para um valor digitado.
7- Verifique se a alteração anterior foi bem-sucedida. Consulte o atributo (teste)
- Sobreescrever o método especial __str__ . Ele não recebe nada e retorna todos os atributos. Teste.
- Crie o método lucro. Não recebe nada e retorna o valor do lucro do produto. Teste
10- Método atualiza_qtd. Ele recebe a quantidade vendida de produtos e atualiza. E não retorna nada, Teste
11- Crie o método alerta_estoque. Não recebe nada e retorna um valor booleano (True ou False).
  Retorna True, se a quantidade em estoque for menor que a quantidade mínima. Caso contrário, retorna False. Teste
12- Método repor_produto. Recebe a quantidade adquirida de produtos e atualiza na memória. Teste.
13- No main, crie o segundo objeto da classe com o nome digitado pelo usuário, apenas o nome. Teste
14- No main, crie mais um objeto da classe passando como argumento apenas o nome e a quantidade em estoque. Teste
15- Crie o método maior_qtd, ele compara dois produtos quaisquer e mostra o produto que tem a maior qtd em estoque. Teste
16- Crie o método maior_lucro, ele compara dois produtos quaisquer e mostra o produto que tem mais lucro. '''

class Produto (object):
    def __init__(self, nome, vlr_compra=0.0, vlr_venda=0.0, qtd_estoque=0, qtd_minima=0):
        self.nome = nome
        self.vlr_compra = vlr_compra
        self.vlr_venda = vlr_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima= qtd_minima

    def get_nome(self):
        return self.nome

    def set_nome(self, p_nome):
        self.nome = p_nome

    def get_qtd_minima(self):
        return self.qtd_minima

    def set_qtd_minima(self, vlr):
        self.qtd_minima = vlr

    def get_qtd_estoque(self):
        return self.qtd_estoque

    def set_qtd_estoque(self, novo_vlr):
        self.qtd_estoque = novo_vlr

    def __str__(self):
        s = f"{self.nome}, {self.vlr_compra}, {self.vlr_venda}, {self.qtd_estoque}, {self.qtd_minima}"
        return s

    def lucro(self):
        vlr_lucro = self.vlr_venda - self.vlr_compra
        return vlr_lucro

    def atualiza_qtd(self, qtd):
        self.qtd_estoque -= qtd

    def alerta_estoque(self):
        if self.qtd_estoque < self.qtd_minima:
            ret = True
        else:
            ret = False
        return ret

    def repor_produto(self, qtd):
        self.qtd_estoque += qtd

    def maior_qtd(self, objeto2):
        if self.qtd_estoque > objeto2.qtd_estoque:
            print("Maior qtd:", self.get_nome())
        elif objeto2.qtd_estoque > self.qtd_estoque:
            print("Maior qtd:", objeto2.get_nome())
        else:
            print('Valores iguais.')

    def maior_quantidade(self, produto):
        if self.get_qtd_estoque() > produto.get_qtd_estoque():
            print("\nO produto com maior estoque é: ", self.get_nome(), "Com o estoque de: ", self.get_qtd_estoque())
        elif produto.get_qtd_estoque() > self.get_qtd_estoque():
            print("\nO produto com maior estoque é: ", produto.get_nome(), "Com o estoque de : ", produto.get_qtd_estoque())
        else:
            print("O mesmo preço")

    def maior_lucro(self, objeto):
        if self.lucro() > objeto.lucro():
            print(self.get_nome(), ', lucro de: ', self.lucro())
        elif obejto.lucro() > self.lucro():
            print(objeto.get_nome(), ', lucro de: ', objeto.lucro())
        else:
            print('Lucros iguais')

if __name__ == '__main__':
    prod_1 = Produto("Arroz", 15.00, 19.50, 67, 20)
    print(prod_1)
    print(prod_1.__str__())
    print(prod_1.get_nome())
    print(prod_1.get_qtd_estoque())

    qtd_m = 2
    prod_1.set_qtd_minima(qtd_m)
    print('Qtd. mínima: ', prod_1.get_qtd_minima())

    print(prod_1.__str__())
    print(prod_1)

    print("Lucro: ", prod_1.lucro())

    prod_1.atualiza_qtd(12)
    print(prod_1)

    print(prod_1.get_qtd_estoque())
    if prod_1.alerta_estoque():
        print("Precisa comprar")
    else:
        print("Não precisa comprar")

    print("Comprar") if prod_1.alerta_estoque() else print("Não")

    prod_1.repor_produto(11)

    prod_2 = Produto("Feijão")

    new_nome = input("Insira o nome desse novo produto: ")
    produto3 = Produto(new_nome)
    produto3.set_qtd_estoque(20)

    produto3 = Produto(new_nome, {}, {}, 20)

    prod_3 = Produto('Farinha', 0, 0, 20, 0)

    prod_4 = Produto('Farinha', qtd_estoque=20)

    prod_1.maior_qtd(prod_2)
    prod_2.maior_qtd(prod_1)
    prod_2.maior_qtd(prod_3)

    prod_1.maior_lucro(prod_2)
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

class Produto(object):
    def __init__(self, nome, vlr_compra, vlr_venda, qtd_estoque, qtd_minima):
        self.nome = nome
        self.vlr_compra = vlr_compra
        self.vlr_venda = vlr_venda
        self.qtd_estoque = qtd_estoque
        self.qtd_minima = qtd_minima

if __name__ == '__main__':
    Produto1 = Produto('Arroz', 15.00, 19.50, 67, 20)
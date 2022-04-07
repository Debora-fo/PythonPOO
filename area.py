'''
- Projete o programa para calcular a área de um triângulo. O usuário informará os dados
  necessários para o cálculo, ou seja, a base e a altura do triângulo.
  Onde:     área = base . altura
                       2

Teste: Entrada: base: 1.5 e altura: 2.6         Resposta: 1.95

- Passos:
Entrada de dados
Processamento
Saída
'''

#Entrada de dados
base = float(input("Qual é a medida da base do triângulo? "))
altura = float(input("Qual é a altura do triângulo? "))

#Processamento
area = (base * altura) / 2

#Saída
print("O triângulo mede ", base, " de base e ", altura," de altura. ")
print("A área do triângulo é igual a ",("%.2f" % area))

'''
Alterações:
a. Mostre o valor da área com duas casas decimais.
b. Na tela de saída de dados, mostre também o valor da base e da altura.
'''

'''- Construa o programa que calcule a raiz ( x ) de uma equação do primeiro grau.
Expressão de uma equação do 1º grau: a x + b = 0.
x = - b
      a
Teste 1: a = 2 e b = 3.         Resposta: Raiz = -1.5

Teste 2: a = 0 e b = 1.         Resposta: Não posso dividir por zero.'''

a = int(input("Digite o valor de A: "))


if a == 0:
    print("Não posso dividir por zero")
else:
    b = int(input("Valor de B: "))
    x = ((-b) / a)
    print('Raiz = ', x)
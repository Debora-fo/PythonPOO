'''
- Construa o programa que calcule a raiz de uma equação do 1º grau.
Calcule a raiz sem fazer crítica de divisão por zero.
Equação do 1º grau:	a x + b = 0,		onde:	x = - b
                                                      a

Teste 1: Entrada: a =  2 e b = 5                Saída: x = - 2.5

Teste 2: Entrada: a = -2 e b = 5                Saída: x =  2.5

Teste 3: Entrada: a =  0  e b = 5               Saída: ?
'''

print("Equação do primeiro grau:   Ax + B = 0")

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
x = ((-b) / a)

print("A raíz é: {}". format(x))

'''
O 17_03 3 vai dá erro de divisão por zero, vamos completar este exercício na próxima aula
com o comando if ... else
'''

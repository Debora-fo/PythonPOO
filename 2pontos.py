'''
- Construa o programa que, tendo como dados de entrada dois pontos quaisquer do
  plano, P(x1,y1) e Q(x2,y2), calcule a distância entre eles. Use a seguinte fórmula:
  distância = raiz quadrada ( (x2 - x1)2 + (y2 - y1)2 )      (elevado a 2)

Teste 1: Entrada: P (1, 2) e Q (1, 2)               Resposta: distância = 0

Teste 2: Entrada: P (1, 2) e Q (5, 7)               Resposta: distância = 6.4031242374328485

'''
import math

x1 = float(input("Digite a coordenada x do ponto p "))
y1 = float(input("Digite a coordenada y do ponto p "))

x2 = float(input("Digite a coordenada x do ponto q "))
y2 = float(input("Digite a coordenada y do ponto q "))

d = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

# Potência:    pow (base, expoente)                 Raiz quadrada:    sqrt (a)

print("O ponto P possui as coordenadas x1 = ", x1, "e y1 = ", y1)
print("O ponto Q possui as coordenadas x2 = ", x2, "e y2 = ", y2)

print("A distância entre os dois pontos é {:.3f}" .format(d))

'''     - ALTERAÇÕES:
a. Mostre o resultado com três casas decimais.
b. Mostre o layout de saída com as coordenadas dos dois pontos e o
valor da distância.  
'''
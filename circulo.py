'''
- Construa o programa que calcule a área de um círculo.
O usuário fornecerá o dado necessário.

Onde:	área = pi . raio2       (raio2 = raio ao quadrado)

Teste:       raio = 2            Resposta: area = 12.56636
'''

import math

raio = float(input("Digite o raio do círculo: "))

#area = 3.14 * raio * raio
area = math.pi * pow (raio, 2)

diametro = 2 * math.pi * raio

print("A área é igual a ", area)
print("Pi = ", math.pi)
print("Diâmetro = ", diametro)

''' Alterações:
# bliblioteca de funcões matemáticas
import math                # Importando os métodos de math, colocar no início do programa
area = math.pi * pow (raio, 2)
area = math.pi * raio** 2
a. mostre o valor da constante pi
b. Calcule e mostre o valor do diâmetro. diametro = 2*r    

'''
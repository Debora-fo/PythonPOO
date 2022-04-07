'''- Projete o programa que calcule as raízes de uma equação do 2° grau, levando em
consideração a análise da existência de raízes reais. Se o valor de delta for menor que
zero, não existem raízes nos reais; se delta for igual a zero, existem duas raízes iguais
e se delta for maior que zero, existem duas raízes diferentes.
Expressão: ax^2 + bx + c = 0
x = - b +-  raiz_quadrada ( b^2 - 4 a c )                 delta = b^2 - 4 a c
                         2a
Teste 1: a = 3, b = 9 e c = 2.  Resposta: Raízes diferentes: x1=-0.24169426078820835 e x2=-2.758305739211792
Teste 2: a = 0, b = 2 e c = 3.  Resposta: Não posso dividir por zero.
Teste 3: a = 2, b = 2 e c = 3.  Resposta: Não existem raízes nos reais.
Teste 4: a = 2, b = 4 e c = 2.  Resposta: Duas raízes iguais: x = -1'''

import math

print("Cálculo de raízes de equação do segundo grau ax^2 + bx + c = 0")

a = float(input("Valor de a: "))

if a == 0:
    print('Não posso dividir por zero')
else:
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))
    delta = pow(b, 2) - 4 * a * c
    if delta < 0:
        print("A equação não possui raízes no conjunto dos reais")
    elif delta == 0:
        x = -b / (2 * a)
        print("A equação possui duas raízes iguais a ", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A equação possui raízes diferentes:\nx1 =", x1, "e x2 =", x2)

 '''ALTERAÇÕES:
a. Mostre com quatro casas decimais. De três formas diferentes.
b. Refaça sem usar a função pow. De duas formas diferentes.
c. Refaça sem usar a função sqrt. De duas formas diferentes.  '''

'''----- DICAS ABAIXO:
print("A equação possui raízes diferentes:\nx1 = %.4f e x2 = %.4f" %(x1, x2))            # a.
print("A equação possui raízes diferentes:\nx1 = {:.4f} e x2 = {:.4f}" .format(x1, x2))
print(f"A equação possui raízes diferentes:\nx1 = {x1:.4f} e x2 = {x2:.4f}")
delta = b * b - 4 * a * c             # Cálculo de delta                                    # b.
delta = b ** 2 - 4 * a * c            # Cálculo de delta
x1 = (-b + delta ** 0.5) / (2 * a) # Parênteses obrigatório no numerador e denominador      # c.
x1 = (-b + delta ** (1/2)) / (2 * a) # Parênteses obrigatório no numerador e denominador      # c.'''
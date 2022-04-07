'''- Dado o comprimento das três retas a, b e c.
Verifique se eles podem ser o comprimento dos lados de um triângulo.
Se forem, verifique se compõem um triângulo equilátero, isósceles ou escaleno.
Informe se não compuserem nenhum triângulo.

Relembre as seguintes definições:
- No plano, triângulo (também aceito como trilátero) é a figura geométrica que ocupa o espaço
interno limitado por três linhas retas que concorrem, duas a duas, em três pontos diferentes
formando três lados e três ângulos internos.
Para ser triângulo, qualquer lado tem medida menor que a soma das medidas dos outros dois lados.

- Triângulo equilátero: possui três lados iguais;
- Triângulo isósceles: possui dois lados iguais;
- Triângulo escaleno: tem todos os lados diferentes.

Obs.: verifique primeiro se os lados formam um triângulo

Teste 1: Entrada: 1, 2 e 3   Resposta: Não é um triângulo.
Teste 2: Entrada: 2, 3 e 4   Resposta: É um triângulo escaleno.
Teste 3: Entrada: 3, 3 e 3   Resposta: É um triângulo equilátero.
Teste 4: Entrada: 2, 3 e 3   Resposta: É um triângulo isósceles.
'''

a = int(input("Insita o comprimento de a: "))
b = int(input("Insita o comprimento de b: "))
c = int(input("Insita o comprimento de c: "))

if a < (b+c) or b < (a+c) or c < (a+b) :
    if a == b == c:
        print("É um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")

else:
    print("Não é um triângulo")
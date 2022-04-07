'''
- A água é um nutriente essencial. Sem ela, o corpo não pode funcionar com perfeição.
Cada pessoa precisa de uma quantidade diferente de água para hidratar o corpo.
A dose ideal, ou seja, a necessidade diária em litros é calculada através desta fórmula:
massa (em kg) vezes 0,03. Elabore o programa que realize esse cálculo.

- Os operadores aritméticos utilizados em Python:
    +   → soma
    –   → subtração
    *   → multiplicação
    /   → divisão
    //  → divisão de inteiros (quociente da divisão)
    **  → potenciação
    %   → módulo (resto da divisão)

Teste 1: Entrada: massa = 71               Resposta: qtd_ideal = 2.13

Teste 2: Entrada: massa = 60               Resposta: qtd_ideal = 1.7999999
'''

massa = float(input("Massa = "))

calculo = massa * 0.03

print("Você pesa ",massa , "kg, portanto sua dose ideal de água é de %.1f" % calculo, "litros por dia.")

'''
ALTERAÇÕES:
a. Na tela de saída, mostre também o valor da massa.
b. Mostre o resultado com uma casa decimal.  
'''
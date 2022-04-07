'''
- Elabore o programa que faça a conversão de graus Fahrenheit (ºF)
para graus Celsius (ºC).
     Onde:     C = 5 . ( F - 32 )
                   9
Teste 1: Entrada: Fahrenheit = 32          Resposta: Celsius = 0

Teste 2: Entrada: Fahrenheit = 55          Resposta: Celsius = 12.77777777777779

'''
farenheit = float(input("Temperatura em Fahrenheit = "))

celsius = (5 * (farenheit - 32)) / 9

print("Valor em Fahrenheit: {:.2f}" .format(farenheit))
print("Valor em Celsius: {:.3f}" .format(celsius))
'''   Alterações:
a. Mostre o valor celsius com três casas decimais.
b. Altere o leiaute da mensagem de saída:
Valor em Fahrenheit: x.xx  (Mostrar com duas casas decimais).
Valor em Celsius: x.xxxx   (Mostrar com quatro casas decimais).  

'''
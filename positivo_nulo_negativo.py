'''- Elabore o programa que leia um número qualquer e verifique
se ele é positivo, negativo ou nulo.
Teste 1: numero = 4             Saída: positivo
Teste 2: numero = 0             Saída: nulo
Teste 3: numero = -4            Saída: negativo'''

numero = int(input("Digite um número: "))

if numero > 0:
    print("O número", numero, " é positivo")
    print("Dobro =", (numero * 2))
elif numero < 0:
    print("O número", numero, " é negativo")
    print("Triplo =", (numero * 3))
else:
    print("O número", numero, " é nulo")


'''ALTERAÇÕES:
a. Além da mensagem, mostre também o número digitado pelo usuário.
b. Se o número for positivo, mostre a mensagem, a variável numero e o dobro;
    se negativo, mostre a mensagem, a variável numero e o triplo;
    se nulo, mostre a mensagem, a variável numero.'''
'''- Escreva o programa que classifique três valores inteiros quaisquer
em ordem crescente. Os valores serão fornecidos pelo usuário.
Teste 1: Entrada: 1, 2, 3       Saída: 1, 2, 3
Teste 2: Entrada: 1, 3, 2       Saída: 1, 2, 3
Teste 3: Entrada: 2, 1, 3       Saída: 1, 2, 3
Teste 4: Entrada: 2, 3, 1       Saída: 1, 2, 3
Teste 5: Entrada: 3, 1, 2       Saída: 1, 2, 3
Teste 6: Entrada: 3, 2, 1       Saída: 1, 2, 3    '''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1<=num2<=num3:
    print(num1, num2, num3)
elif num2<=num3<=num1:
    print(num2, num3, num1)
elif num3<=num1<=num2:
    print(num3, num1, num2)
elif num1<=num3<=num2:
    print(num1, num3, num2)
elif num2<=num1<=num3:
    print(num2, num1, num3)
elif num1==num2==num3:
    print('Os três números são iguais')
else:
    print(num3,num2,num1)

if num1==num2 or num2==num3 or num1==num3:
    print('Dois números são iguais')



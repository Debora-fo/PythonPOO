'''- Escreva o programa que classifique três valores inteiros quaisquer
em ordem crescente. Os valores serão fornecidos pelo usuário.
Teste 1: Entrada: 1, 2, 3       Saída: 1, 2, 3
Teste 2: Entrada: 1, 3, 2       Saída: 1, 2, 3
Teste 3: Entrada: 2, 1, 3       Saída: 1, 2, 3
Teste 4: Entrada: 2, 3, 1       Saída: 1, 2, 3
Teste 5: Entrada: 3, 1, 2       Saída: 1, 2, 3
Teste 6: Entrada: 3, 2, 1       Saída: 1, 2, 3    '''

# exercício 1 refeito usando listas

numeros=[]
for num in range(3):
   num = int(input('Digite um número: '))
   numeros.append(num)
ordem = sorted(numeros)
print(numeros)
print(ordem)

'''
- Faça o programa que calcule a média aritmética de duas notas
bimestrais fornecidas pelo usuário.
   Onde:     média = nota1 + nota2
                           2

Teste 1: nota1: 4.5 e nota2: 6.1             Saída: 5.3
Teste 2: nota1: 7.5 e nota2: 5.1             Saída: 6.3

Abaixo segue uma lista com os operadores aritméticos utilizados em Python:
    +   → soma
    –   → subtração
    *   → multiplicação
    /   → divisão
    //  → divisão de inteiros (quociente da divisão)
    **  → potenciação
    %   → módulo (resto da divisão)
'''

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))


media = (nota1 + nota2 + nota3)/3
mediap = ((nota1 * 1) + (nota2 * 2) + (nota3 * 3))/6

print("\n\n\nMédia = ", (nota1 + nota2 + nota3)/3)
print("Nota 1 = ",nota1, "\nNota 2 = ", nota2, "\nNota 3 = ", nota3)
print("Média ponderada = ", mediap)

'''   ALTERAÇÕES:
a. Refaça-o considerando que o aluno realizou três avaliações. Teste com 2, 3 e 4.
    Resposta 3
b. Na execução, pule três linhas antes de mostrar o valor da média. 
c. Depois da média, mostre também o valor das três notas.
d. Acrescente o calculo da média ponderada, considerando que a prova1 
tem peso 1, a prova2 tem peso 2 e a prova3 tem peso 3.  
Teste com os valores 5, 6, 7.       A resposta certa é 6,3333333
e. Agora, refaça-o sem usar a variável media
    '''
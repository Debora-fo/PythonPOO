"""
- Desenvolva o programa que calcule a média aritmética de uma turma, onde
cada aluno realizou uma avaliação. Não sabemos a quantidade de alunos,
por isso usaremos o valor “ -1” como condição de saída. Na tela de saída,
mostre também a quantidade de alunos da turma. Sempre que tivermos uma divisão,
temos que verificar se o divisor é diferente de zero.

Dica: media = soma / ct

Teste 1:    notas: 5, 6 e -1      Saída: Média 5.5        Quantidade de alunos: 2
Teste 2:    notas: 5, 6, 7 e -1   Saída: Média 6          Quantidade de alunos: 3  -----
"""

soma = 0
contador = 0 #Vai contando os inputs por aluno, nesse caso ele inicia no 0

print('Digite [ -1 ] para sair')

while True:
    nota = float(input("Digite a nota do aluno " + str (contador + 1) + ": "))# Outras opções de mudar o número do aluno:
    if nota == -1:                                                            #nota = float (input("Digite a nota do aluno {} : " . format (contador+1)))
        break                                                                 # nota = float (input(f"Digite a nota do aluno {contador+1} : "))
    contador = contador + 1
    soma = soma + nota
if contador != 0:
    media = soma / contador
    print("Média da turma de ",contador, " alunos é  %.2f" %(media))
    print('Soma das notas dos alunos: ', soma)
else:
    print("ZeroDivisionError: division by zero")



''' ----- ALTERAÇÕES:
a. Se digite -1 na primeira leitura ocorre o erro: "ZeroDivisionError: division by zero". 
    Resolva esse problema. 
    Teste 3:    notas: -1                 Saída: Não existe divisão por zero
b. Troque a mensagem estática da entrada de dados (input) por uma mensagem dinâmica.
c. Mostre também a soma das notas dos alunos da turma.
d. Mostre a média da turma com duas casas decimais.
e. Mostre a média e a quantidade de alunos na mesma linha, nesta frase:
    A média da turma de X alunos é X.XX.                
'''
'''
- Refaça o programa que calcule a média aritmética de um aluno que realizou duas
avaliações. Além do valor da média, inclua na tela de saída uma das mensagens:
“Aluno aprovado.” ou “Aluno reprovado.”.
Considere que o aluno será aprovado se conseguir média maior ou igual a cinco.

Teste 1: Entrada: nota1 = 5, nota2 = 6                          Saída: Média = 5.5
                                                                       Aluno aprovado
Teste 2: Entrada: nota1 = 5, nota2 = 2                          Saída: Média = 3.5
                                                                       Aluno reprovado
'''

nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
peso1 = int(input("Peso da nota 1: "))
peso2 = int(input("Peso da nota 2: "))

media = ((nota1*peso1) + (nota2*peso2)) /(peso1+peso2)
if media >= 5:
    print("Sua média é ",("%.2f" % media),", aluno aprovado.")
else:
    print("Sua média é ",("%.2f" % media),", aluno reprovado.")

'''   ALTERAÇÕES:
a. Mostre o valor da média aritmética com duas casas decimais.
b. Altere a saída. Mostre a média e a mensagem na mesma linha:
    Média do aluno: x.xxx           Aluno aprovado ou Aluno reprovado
c. Refaça-o considerando que a primeira prova tem peso três e
   a segunda, peso cinco. Ou seja, calcula a média ponderada do aluno.
Teste 2: nota1 = 5, nota2=6, peso1=3, peso2=5    Saída: média = 5,625
d. Deixe o programa mais interessante, permita que o usuário digite
   o valor dos pesos para usar no cálculo da média ponderada. ----- DICAS ABAIXO:
print ('Média = {:.2f}' .format (media) )               # a. Solução 1
print (f'Média = {media:.2f}')                          # a. Solução 2
print ('Média = %.2f' % (media) )                       # a. Solução 3

'''

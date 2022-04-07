'''- Elabore o programa que leia a altura e o gênero (‘m’ pra masculino e ‘f’ pra feminino)
de um grupo de pessoas. Gere a tela de saída com as seguintes informações:
maior altura do grupo, menor altura do grupo, quantidade de homens e quantidade de mulheres.
Teste 1: 1.80, m, 1.60,  f, 0             Saída: Maior=1.80   Menor=1.60   Masc.= 1   Fem.= 1
Teste 2: 1.80, m, 1.60,  f, 1.7, m, 0     Saída: Maior=1.75   Menor=1.60   Masc.= 2   Fem.= 1
Teste 3: 1.80, m, 1.60,  f, 1.7, f , 0    Saída: Maior=1.80   Menor=1.65   Masc.= 1   Fem.= 2'''

maior = 0                                       # Começar com o menor valor possível
menor = 3                                       # Começar com o maior valor possível

ct_masc = 0
ct_fem = 0

total_alt = 0

print('Digite [ 0 ] para sair')

while True:

    altura = float(input("Digite a altura: "))

    if altura == 0:
        break

    genero = input("Digite:\n[m] para Masculino\n[f] para Feminino: ")

    if genero == "m" or genero == "M":
        ct_masc += 1  # ct_masc = ct_masc + 1
    elif genero == 'f' or genero == "F":
        ct_fem += 1  # ct_fem = ct_fem + 1
    else:
        print("Você digitou opção inválida.")

    if altura > maior:
        maior = altura

    if altura < menor:
        menor = altura

    total_alt = altura + total_alt
ct_geral = ct_masc + ct_fem

if altura == 0 and ct_geral == 0 :
    print("Não foi digitado nenhum dado.")

else:
    print("Maior altura no grupo: ", maior)
    print("Menor alturano grupo: ", menor)

    print("Quantidade de homens: ", ct_masc)
    print("Quantidade de mulheres: ", ct_fem)

    print("Porcentagem de homens:", (ct_masc * 100)/ ct_geral)

    print("Média de alturas: ",  (total_alt/ (ct_fem + ct_masc)))

'''ALTERAÇÕES:

a. Se o usuário digitar qualquer tecla diferente de 'm' ou 'f' mostre a mensagem 
de erro: "Você digitou opção inválida.".

b. Calcule e mostre também a média de alturas do grupo. Dica: media = soma / ct
Teste 4: 1.80, m, 1.60,  f, 0     Saída: Maior=1.80   Menor=1.60   Masc.= 1   Fem.= 1  Média = 1.7

c. Calcule e mostre também a porcentagem de homens.
Teste 5: 1.80, m, 1.60,  f, 0 Saída: Maior=1.80   Menor=1.60  Masc.= 1  Fem.= 1  Média = 1.7 Porc. = 50

d. Digite a condição de saída (zero) de primeira e evite os erros do Python.
    Mostre somente esta mensagem:    "Não foi digitado nenhum dado."

e. Permita o usuário digitar letra maiúscula ou minúscula. Resolva de duas maneiras. '''

'''
#if (genero == "m" or genero == "M"):                              #  Solução 1     # e.

    if genero.lower() == "m":   # if (genero.lower() == "m"):  #  Solução 2
        ct_masc += 1                       # ct_masc = ct_masc + 1
    elif geneno == 'f' or genero == 'F':      # elif genero.lower() == 'f':
        ct_fem += 1                         # ct_fem = ct_fem + 1'''
'''- Uma agência de publicidade quer prestar seus serviços somente para a
maior companhia, considerando a quantidade de funcionários. Para tal, consegue
um conjunto de dados com o CNPJ (Cadastro Nacional de Pessoa Jurídica) e a
quantidade de funcionários de várias empresas. Construa o programa que leia esses
dados de entrada e mostre o CNPJ e a quantidade de funcionários da maior empresa,
ou seja, da empresa com maior recursos humanos.
Teste 1: Entrada: 1, 15; 2, 20; 3, 10       Saída: Maior empresa: 2, qtd 20'''

maior_qtd = -1
menor_qtd = -1
maior_cnpj = ""
menor_cnpj = ""
ct = 0

print('Digite [s] para finalizar')

while True:

    cnpj = input("Digite o CNPJ: ")

    if cnpj == 's':
        break

    qtd = int(input("Digite a quantidade de funcionários: "))

    if qtd > maior_qtd:
        maior_qtd = qtd
        maior_cnpj = cnpj

    else:
        menor_qtd = qtd
        menor_cnpj = cnpj

    ct += 1


if maior_qtd > -1:
    print(f"A empresa {maior_cnpj} possui o maior número de funcionários\ncom um total de {maior_qtd}")
    print("Número de empresas processadas: ", ct)
    print(f"A empresa {menor_cnpj} possui o menor número de funcionários\ncom um total de {menor_qtd}")
else:
    print("Nenhuma dado fornecido.")



''' ----- ALTERAÇÕES:
a. Quantas empresas foram processadas?
b. Mostre também o CNPJ e a quantidade de funcionários da menor empresa.
    ----- DICAS:
ct = 0                                      # Antes do while                            # a.
    ct += 1                                 # Dentro do while
print('Quantidade de empresas:', ct)        # Depois do while
'''
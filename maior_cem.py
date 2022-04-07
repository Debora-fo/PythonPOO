'''
- 1. Projete o programa que leia um valor numérico e verifique se ele é maior
ou igual a cem.
Mostre uma das mensagens:
“Valor maior ou igual a cem.” ou “Valor menor que cem.”
'''

valor = int(input("Digite um valor: "))
if valor >= 100:
    print("Valor maior ou igual a cem.")
else:
    print("Valor menor que cem.")

'''
ALTERAÇÕES:
a. Mostrar também na tela de saída o valor numérico lido.

DICAS ABAIXO:
print ("Valor lido: ", valor)                   # a.
print("O seu número foi: {}" .format(valor))

'''
print("Valor indicado :", valor)
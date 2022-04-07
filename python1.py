#Aula de Python

#IMPRIMIR:

print('Hello World!')
#-----------------------------------------------------------------------

#OPERAÇÕES:
a=4
b=2
print(a+b)  #Soma
print(a-b)  #Subtração
print(a*b)  #Multiplicação
print(a**2) #Potênciação
print(a/b)  #Divisão
print(a//b) #Divisão arredondada
print(a%b)  #Mostrar o resto da divisão
#-----------------------------------------------------------------------

#FUNÇÕES:

#-----------------------------------------------------------------------

#Input (recebe um valor, igual ao CIN do C++):

nome=input('Qual é o seu nome? ')
print(nome)
#-----------------------------------------------------------------------

#COLOCAR UMA VARIÁVEL EM UMA STRING:

fruta='laranja'
print('Minha fruta favorita é %s' %fruta)  #%s vem de string :)

#usar para várias variáveis:
cor1='azul'
cor2='rosa'
print('O céu é {0} e a flor é {1}'.format(cor1,cor2))

#usar para organizar as casas decimais de uma variável:

conta = 17/3
print(conta)
print('O resultado da divisão é: {:.2f}'.format(conta))

#-----------------------------------------------------------------------

#CONDIÇÕES:

comida = 'pizza'
if comida == 'pizza':
    print ('Possui muitas calorias!')
elif comida =='abóbora':
    print ('Possui poucas calorias!')
else:
    print ('Desconheço as calorias!')

# == significa igual
# != significa diferente

#EX:

ano=int(input('Em que ano você nasceu?'))
idade=2020-ano
if idade>=18:
    print('Maior de idade')
else:
    print ('Menor de idade')

#-----------------------------------------------------------------------
#LOOP:

for i in range(5):
    print (i)

for n in range(8):
    print('Linha',n)

b=10
for j in range(b):
    print(j)



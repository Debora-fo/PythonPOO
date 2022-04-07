'''- Construa o programa que calcule o peso ideal de uma pessoa.
Utilize as seguintes fórmulas:
- Se homem, o peso ideal é calculado assim: ( 72,7 * altura ) - 58;
- Se mulher, o peso ideal é calculado assim: ( 62,1 * altura ) - 44,7.
Analise o problema e verifique quais são os dados que o usuário precisa fornecer.

Teste1: altura = 1.70 e genero = 1           Saída: peso ideal = 65.59 Kg
Teste2: altura = 1.70 e genero = 2           Saída: peso ideal = 60.8699999 Kg'''

altura = float(input("Digite sua altura: "))
genero = str(input("Qual é o seu gênero? Digite M para masculino e F para feminino: "))

pesohomem = (( 72.7 * altura ) - 58)
pesomulher = (( 62.1 * altura ) - 44.7)

if genero == 'M':
    print("Seu peso ideal é ", pesohomem)
elif genero == 'F':
    print("Seu peso ideal é ",pesomulher)
else:
    print("Erro")

'''ALTERAÇÕES:
a. Troque as duas linhas dentro do else por uma única linha de comando.
b. Troque a entrada para M ou F.
   Teste3: altura = 1.8     genero = M           Saída: peso ideal = 72.86 Kg 
c. Mostre uma mensagem de erro se ele digitar valor de gênero diferente de M e F.'''
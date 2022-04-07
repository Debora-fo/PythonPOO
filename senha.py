'''- Elabore o programa que verifica se o usuário digitou a senha correta.
Mostre a mensagem “Senha incorreta.” ou “Acesso liberado.”.
Vamos supor que a senha correta seja 123.

Teste 1: senha = 123        Resposta: Acesso liberado.
Teste 2: senha = 111        Resposta: Senha incorreta.'''

tentativa = str(input("Digite a senha: "))
senha = '1b3'

if tentativa == senha:
    print("Acesso liberado")
else:
    print("Senha incorreta")

'''ALTERAÇÕES:
a. Considere que a senha correta é 1b3.'''
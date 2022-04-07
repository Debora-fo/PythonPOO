'''- Resolva sem lista

- Em uma eleição presidencial, existem três candidatos. Os votos são
informados através de código. Os dados utilizados para escrutinagem obedecem
à seguinte codificação:
1, 2, 3 - voto dos respectivos candidatos;
5 - voto nulo; 6 - voto em branco;
- Elabore o programa que calcule a quantidade de votos de cada candidato, quantidade de
votos nulos, quantidade de votos em branco, percentual de votos nulos e percentual
de votos em branco.
Teste 1: Entrada: 1, 2, 3, 5, 6, 9
         Saída: Cand1=1 Cand2=1 Cand3=1 Nulo=1 Branco=1 pct_nulo=20 pct_branco=20 '''

ct_candidato1 = 0
ct_candidato2 = 0
ct_candidato3 = 0
ct_nulo = 0
ct_branco = 0

while True:
    voto = int(input("[1] Candidato 1\n[2] Candidato 2\n[3] Candidato 3\n[5] Voto nulo"
                     "\n[6] Voto em branco\n[9] Encerrar\nDigite seu voto: "))
    if voto == 9:
        break
    if voto == 1:
        ct_candidato1 += 1  # ct_candidato1 = ct_candidato1 + 1
    elif voto == 2:
        ct_candidato2 += 1
    elif voto == 3:
        ct_candidato3 += 1
    elif voto == 5:
        ct_nulo += 1
    elif voto == 6:
        ct_branco += 1
    else:
        print("Voto não registrado.")

ct_total = ct_candidato1 + ct_candidato2 + ct_candidato3 + ct_nulo + ct_branco

if ct_total != 0:
    print("Candidato1 = ", ct_candidato1, " votos.")
    print("Candidato2 = ", ct_candidato2, " votos.")
    print("Candidato3 = ", ct_candidato3, " votos.")
    print("Votos nulos = ", ct_nulo)
    print("Votos em branco = ", ct_branco)
    pct_nulo = ct_nulo / ct_total * 100
    pct_branco = ct_branco / ct_total * 100
    print('Porcentagem nulo: ', pct_nulo)
    print('Porcentagem branco: ', pct_branco)
else:
    print("Ninguém votou.")


'''   -----   ALTERAÇÕES:
a. Digite a condição de saída (voto = 9) de primeira, o que acontece? 
   e mostre somente esta mensagem:
   "Ninguém votou."
   
   
        ----- DICAS:
if ct_total != 0:                                                       # a.
    print("Candidato1 = ", ct_candidato1, " votos.")    
    print("Candidato2 = ", ct_candidato2, " votos.")
    print("Candidato3 = ", ct_candidato3, " votos.")
    print("Votos nulos = ", ct_nulo)
    print("Votos em branco = ", ct_branco)
    pct_nulo = ct_nulo / ct_total * 100
    pct_branco = ct_branco / ct_total * 100
    print('Porcentagem nulo: ', pct_nulo)
    print('Porcentagem branco: ', pct_branco)
else:
    print("Ninguém votou.")


'''
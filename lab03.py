numeroJogadores = int(input())
numerosMagicos = input().split()
limites = input().split()

grupoUm =  int(numeroJogadores/2)
grupoDois = numeroJogadores
if numeroJogadores%2 :
    grupoUm = grupoUm + 1

posicaoVencedor = pontuacaoVencedor = 0
empate = False
j = 0

for i in range(grupoUm) :
    L = int(limites[j])
    R = int(limites[j+1])
    pontuacao = (R-L) * int(numerosMagicos[i])

    if pontuacao > pontuacaoVencedor :
        pontuacaoVencedor = pontuacao
        posicaoVencedor = i+1
        empate = False
    elif pontuacao == pontuacaoVencedor :
        empate = True

    i = i+1
    j = j+2

for i in range(i, grupoDois) :
    L = int(limites[j])
    R = int(limites[j+1])
    pontuacao = (R-L) + int(numerosMagicos[i])

    if pontuacao > pontuacaoVencedor :
        pontuacaoVencedor = pontuacao
        posicaoVencedor = i+1
        empate = False
    elif pontuacao == pontuacaoVencedor :
        empate = True

    i = i+1
    j = j+2

if empate :
    print("Rodada de cerveja para todos os jogadores!")
else:
    print(f"O jogador número {posicaoVencedor} vai receber o melhor bolo da cidade pois venceu com {pontuacaoVencedor} ponto(s)!")

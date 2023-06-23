robo = 'r'
sujo = 'o'
limpo = '.'
impresso = False    # informa se a configuração atual da matriz já foi impressa pela função limpeza(), para evitar que escaneamento() a imprima de novo

def printarMatriz(matriz : list[list]) -> None:
    for linha in matriz:
        print(*linha)
    
    print()

def escaneamento(matriz : list[list], posAtual : tuple) -> None:

    limLinha = len(matriz)-1
    limColuna = len(matriz[0])-1

    indexLinha, indexColuna = posAtual
    while indexLinha <= limLinha:
        if indexLinha % 2 == 1:      # inverter o sentido se a linha for ímpar
            sentido = -1
        else:
            sentido = 1

        while indexColuna <= limColuna and indexColuna >= 0:
            global impresso
            
            matriz[indexLinha][indexColuna] = robo  # atualizar posicao do robô na matriz
            if impresso == False:
                printarMatriz(matriz)
            else:
                impresso = False
            matriz[indexLinha][indexColuna] = limpo # mudar posicao atual para limpo

            # checar por sujeira
            if indexColuna > 0 and matriz[indexLinha][indexColuna-1] == sujo:
                limpando(matriz, tuple((indexLinha, indexColuna)), tuple((indexLinha, indexColuna-1)))
            elif indexLinha > 0 and matriz[indexLinha-1][indexColuna] == sujo:
                limpando(matriz, tuple((indexLinha, indexColuna)), tuple((indexLinha-1, indexColuna)))
            elif indexColuna < limColuna and matriz[indexLinha][indexColuna+1] == sujo:
                limpando(matriz, tuple((indexLinha, indexColuna)), tuple((indexLinha, indexColuna+1)))
            elif indexLinha < limLinha and matriz[indexLinha+1][indexColuna] == sujo:
                limpando(matriz, tuple((indexLinha, indexColuna)), tuple((indexLinha+1, indexColuna)))

            indexColuna += sentido
        
        indexLinha += 1
        indexColuna += -sentido   # readequar o index da coluna às margens da matriz
    
    # verificar se o robô não terminou na última coluna da última linha
    if indexColuna-1 != limColuna: 
        indexLinha -= 1     # readequar o index da linha às margens da matriz
        #indexColuna += 1    # readequar o index da coluna às margens da matriz

        matriz[indexLinha][indexColuna] = limpo # mudar posicao atual para limpo

        indexColuna += 1    # para não imprimir repetido
        while indexColuna <= limColuna:
            matriz[indexLinha][indexColuna] = robo  # atualizar posicao do robô na matriz
            printarMatriz(matriz)
            matriz[indexLinha][indexColuna] = limpo # mudar posicao atual para limpo

            indexColuna += 1
    
    quit()


def limpando(matriz : list[list], posOriginal : tuple, posLimpar : tuple) -> None:

    limLinha = len(matriz)-1
    limColuna = len(matriz[0])-1

    indexLinha, indexColuna = posLimpar

    while matriz[indexLinha][indexColuna] == sujo: 
        matriz[indexLinha][indexColuna] = robo  # atualizar posicao do robô na matriz
        printarMatriz(matriz)
        matriz[indexLinha][indexColuna] = limpo # mudar posicao atual para limpo
        global impresso
        impresso = True

        if indexColuna > 0 and matriz[indexLinha][indexColuna-1] == sujo:
            indexColuna -= 1
        elif indexLinha > 0 and matriz[indexLinha-1][indexColuna] == sujo:
            indexLinha -= 1
        elif indexColuna < limColuna and matriz[indexLinha][indexColuna+1] == sujo:
            indexColuna += 1
        elif indexLinha < limLinha and matriz[indexLinha+1][indexColuna] == sujo:
            indexLinha += 1

    retornarEscaneamento(matriz, posOriginal, tuple((indexLinha, indexColuna)))


def retornarEscaneamento(matriz : list[list], posOriginal : tuple, posAtual : tuple) -> None:
    
    limLinha = len(matriz)-1
    limColuna = len(matriz[0])-1

    # checar se a posição atual após a limpeza seria a próxima a ser escaneada
    linhaOriginal, colunaOriginal = posOriginal
    linhaAtual, colunaAtual = posAtual

    if linhaOriginal % 2 == 0:              # definir qual seria a próxima posição a ser escaneada
        if colunaOriginal < limColuna:
            proxColuna = colunaOriginal + 1
            proxLinha = linhaOriginal
        else:
            proxColuna = limColuna
            proxLinha = linhaOriginal + 1
    else:
        if colunaOriginal > 0:
            proxColuna = colunaOriginal - 1
            proxLinha = linhaOriginal
        else:
            proxColuna = 0
            proxLinha = linhaOriginal + 1

    if tuple((proxLinha, proxColuna)) == posAtual:
        escaneamento(matriz, posAtual)

    # se a posição atual não for a que seria escaneada

    while colunaAtual < colunaOriginal:
        matriz[linhaAtual][colunaAtual] = limpo # mudar posicao atual para limpo
        colunaAtual += 1
        matriz[linhaAtual][colunaAtual] = robo # mudar posicao atual para limpo
        printarMatriz(matriz)
    while colunaAtual > colunaOriginal:
        matriz[linhaAtual][colunaAtual] = limpo # mudar posicao atual para limpo
        colunaAtual -= 1
        matriz[linhaAtual][colunaAtual] = robo # mudar posicao atual para limpo
        printarMatriz(matriz)

    while linhaAtual > linhaOriginal:  # linhaAtual não pode ser menor que linhaOriginal
        matriz[linhaAtual][colunaAtual] = limpo # mudar posicao atual para limpo
        linhaAtual -= 1
        matriz[linhaAtual][colunaAtual] = robo # mudar posicao atual para limpo
        printarMatriz(matriz)

    escaneamento(matriz, tuple((linhaAtual, colunaAtual)))


def main() -> None:

    matriz = []
    N = int(input())
    for k in range(N):
        linha = input().split()
        matriz.append(linha)

    escaneamento(matriz, tuple((0,0)))


if __name__ == "__main__":
    main()

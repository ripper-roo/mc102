class Masmorra:
    def __init__(linha, coluna):
        self.linhaMax = linha-1
        self.colunaMax = coluna-1

        self.mapa = [['.' for k in range(coluna)] for i in range(linha)]
    
    def getLinhaMax():
        return linhaMax

    def getColunaMax():
        return colunaMax

class Monstro:
    def __init__(self, vidaMonstro, ataqueMonstro, tipo, xMonstro, yMonstro, masmorra):
        self.vidaMonstro = vidaMonstro
        self.ataqueMonstro = ataqueMonstro
        self.tipo = tipo
        self.xMonstro = xMonstro
        self.yMonstro = yMonstro
        self.masmorra = masmorra

class Objeto:
    def __init__(self, nome, tipo, xObjeto, yObjeto, status):
        self.nome = nome
        self.tipo = tipo
        self.xObjeto = xObjeto
        self.yObjeto = yObjeto
        self.status = status

class Link:
    def __init__(self, vidaLink, danoLink, xLink, yLink, masmorra):
        self.vidaLink = vidaLink
        self.danoLink = danoLink
        self.xLink = xLink
        self.yLink = yLink
        self.masmorra = masmorra
    
    def moverAte(linha, coluna):

        pass

    def mover():
        if yLink % 2 == 0:
            if xLink < masmorra.getLinhaMax():
                xLink += 1
            else:
                yLink -= 1
        else:
            if xLink > 0:
                xLink -= 1
            else:
                yLink -= 1

    def atacar():
        pass

    def usarItem():
        pass
    
    def recebeDano():
        pass


def main() -> None:

    monstros = []   # lista de monstros
    objetos = []    # lista de objetos

    ### LEITURA ###
    vidaDano = input().split()
    vidaLink, danoLink = vidaDano

    linhaColuna = input().split()
    linha, coluna = linhaColuna

    posLink = input().split()
    xLink, yLink = posLink

    posSaida = input().split()
    xSaida, ySaida = posSaida    

    q = int(input())
    for k in range(q):
        info = input().split()
        vidaMonstro, ataqueMonstro, tipo, xMonstro, yMonstro = info
        m = Monstro(vidaMonstro, ataqueMonstro, tipo, xMonstro, yMonstro)
        monstros.append(m)

    b = int(input())
    for k in range(b):
        info = input().split()
        nome, tipo, xObjeto, yObjeto, status = info
        o = Objeto(nome, tipo, xObjeto, yObjeto, status)
        objetos.append(o)

    ### PROCESSAMENTO ###

    # link
    link = Link(vidaLink, danoLink, xLink, yLink)

    while link


    print(vida, dano)
    print(linha, coluna)

if __name__ == "__main__":
    main()
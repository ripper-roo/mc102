class Monstro:

    def __init__(self, vida, pontosAtaque, componentes, fraquezas, danoMax, coordenadas):
        self.vida
        self.pontosAtaque
        #self.qtdPartes
        self.componentes
        self.fraquezas
        self.danoMax
        self.coordenadas


def main() -> None:
    
    ### LEITURA ###
    a = int(input())

    flechasLeitura = input().split()
    flechas = {}
    i = 0
    # passar informações das flechas para um dicionário
    for k in range( len(flechasLeitura)//2 ):
        key = flechasLeitura[i]
        value = flechasLeitura[i+1]
        flechas.update({key: value})
        i+=2

    n = int(input())
    u = int(input())

    monstros = [] # lista para guardar objetos do tipo Monstro
    for k in range(n):
        v = int(input())
        p = int(input())
        q = int(input())

        partes = []
        for j in range(q):
            partesLeitura = input().split(sep=',').strip()
            partes.append(partesLeitura)
        
        # instanciar monstro
        monstro.append( Monstro(v, p, componentes, fraquezas, danoMax, coordenadas) )


        
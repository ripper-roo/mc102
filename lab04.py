numeroDias = int(input())
for i in range(numeroDias):

    numeroBriga = 0
    animaisAtendidos = []
    animaisNaoAtendidos = []
    animaisIndisponivel = []

    print("Dia:", i+1)

    numeroBriga = int(input())
    paresBriga = {}
    while numeroBriga:
        nomesBriga = input().split()
        nome1 = nomesBriga[0]
        nome2 = nomesBriga[1]

        if nome1 in paresBriga:
            paresBriga[nome1].append(nome2)
        else:
            paresBriga[nome1] = [nome2]


        if nome2 in paresBriga:
            paresBriga[nome2].append(nome1)
        else:
            paresBriga[nome2] = [nome1]

        numeroBriga -= 1

    procedimentosLista = input().split()
    procedimentosRestantes = {}
    for j in range(0, len(procedimentosLista), 2):
        procedimentosRestantes[procedimentosLista[j]] = int(procedimentosLista[j+1])
    
    listaPresenca = []
    numeroVisitas = int(input())
    for j in range(numeroVisitas):
        procedimentosDesejados = input().split()
        nome = procedimentosDesejados[0]
        proc = procedimentosDesejados[1]

        #lista de presença
        listaPresenca.append(nome)

        #verificar briga
        if nome in paresBriga:
            for n in paresBriga[nome]:
                if n in listaPresenca:
                    numeroBriga += 1
    
        #analisar procedimentos
        if proc in procedimentosRestantes:
            if procedimentosRestantes[proc] > 0:
                procedimentosRestantes[proc] = procedimentosRestantes[proc]-1
                animaisAtendidos.append(nome)
            else:
                animaisNaoAtendidos.append(nome)
        else:
            animaisIndisponivel.append(nome)

    #saída
    print("Brigas:", numeroBriga)

    if len(animaisAtendidos):
        print("Animais atendidos: ", end="")
        print(*animaisAtendidos, sep=", ")

    if len(animaisNaoAtendidos):
        print("Animais não atendidos: ", end="")
        print(*animaisNaoAtendidos, sep=", ")

    if len(animaisIndisponivel):
        for n in animaisIndisponivel:
            print("Animal", n, "solicitou procedimento não disponível.")

    print()
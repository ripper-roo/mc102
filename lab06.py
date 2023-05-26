def iguala_vetores(v1, v2, numero_v1, numero_v2):
    """Iguala o número de elementos de duas listas para o maior possível

    Parâmetros:

    v1, v2: vetores a serem igualados.
    numero_v1: número que será usado como padding para v1
    numero_v2: número que será usado como padding para v2

    """
    maior = max(len(v1), len(v2))

    for i in range(len(v1), maior):
        v1.append(numero_v1)
    for i in range(len(v2), maior):
        v2.append(numero_v2)

    return v1, v2


def soma_vetores(v1, v2):
    if len(v1) != len(v2):
        v1, v2 = iguala_vetores(v1, v2, 0, 0)

    return [i+j for i, j in zip(v1, v2)]


def subtrai_vetores(v1, v2):
    if len(v1) != len(v2):
        v1, v2 = iguala_vetores(v1, v2, 0, 0)

    return [i-j for i, j in zip(v1, v2)]


def multiplica_vetores(v1, v2):
    if len(v1) != len(v2):
        v1, v2 = iguala_vetores(v1, v2, 1, 1)

    return [i*j for i, j in zip(v1, v2)]


def divide_vetores(v1, v2):
    if len(v1) != len(v2):
        v1, v2 = iguala_vetores(v1, v2, 0, 1)

    return [i//j for i, j in zip(v1, v2)]


def multiplicacao_escalar(v1, escalar):
    return [escalar*i for i in v1]


def n_duplicacao(v1, n):
    vetor_resultante = []
    for i in range(n):
        vetor_resultante += v1

    return vetor_resultante


def soma_elementos(v1):
    soma = 0
    for i in v1:
        soma += i

    return [soma]


def produto_interno(v1, v2):
    if len(v1) != len(v2):
        v1, v2 = iguala_vetores(v1, v2, 1, 1)

    soma = 0
    for i, j in zip(v1, v2):
        soma += i*j

    return [soma]


def multiplica_todos(v1, v2):
    vetor_resultante = []
    for i in range(len(v1)):
        vetor_resultante.append(0)  # semelhante a soma = 0
        for j in range(len(v2)):
            vetor_resultante[i] += v1[i]*v2[j]

    return vetor_resultante


def correlacao_cruzada(v1, mascara):
    n = len(v1)
    k = len(mascara)

    vetor_resultante = []
    for i in range(0, n-k+1):
        parte_v1 = v1[i:k+i]
        soma_produto_interno = produto_interno(parte_v1, mascara)
        vetor_resultante.append(*soma_produto_interno)

    return vetor_resultante


def main():
    v1 = (input().split(","))

    while (operacao := input()) != "fim":
        if operacao == "soma_vetores":
            v2 = (input().split(","))

            # transformar componentes do vetor em int
            v1 = [int(i) for i in v1]
            v2 = [int(i) for i in v2]

            v1 = soma_vetores(v1, v2)

        elif operacao == "subtrai_vetores":
            v2 = (input().split(","))

            # transformar componentes do vetor em int
            v1 = [int(i) for i in v1]
            v2 = [int(i) for i in v2]

            v1 = subtrai_vetores(v1, v2)

        elif operacao == "multiplica_vetores":
            v2 = (input().split(","))

            # transformar componentes do vetor em int
            v1 = [int(i) for i in v1]
            v2 = [int(i) for i in v2]

            v1 = multiplica_vetores(v1, v2)

        elif operacao == "divide_vetores":
            v2 = (input().split(","))

            # transformar componentes do vetor em int
            v1 = [int(i) for i in v1]
            v2 = [int(i) for i in v2]

            v1 = divide_vetores(v1, v2)

        elif operacao == "multiplicacao_escalar":
            escalar = int(input())

            # transformar componentes do vetor em int
            v1 = [int(i) for i in v1]

            v1 = multiplicacao_escalar(v1, escalar)

        elif operacao == "n_duplicacao":
            n = int(input())

            # transformar componentes do vetor em int
            v1 = [int(i) for i in v1]

            v1 = n_duplicacao(v1, n)

        elif operacao == "soma_elementos":
            # transformar componentes do vetor em int
            v1 = [int(i) for i in v1]

            v1 = soma_elementos(v1)

        elif operacao == "produto_interno":
            v2 = (input().split(","))

            # transformar componentes do vetor em int
            v1 = [int(i) for i in v1]
            v2 = [int(i) for i in v2]

            v1 = produto_interno(v1, v2)

        elif operacao == "multiplica_todos":
            v2 = (input().split(","))

            # transformar componentes do vetor em int
            v1 = [int(i) for i in v1]
            v2 = [int(i) for i in v2]

            v1 = multiplica_todos(v1, v2)

        elif operacao == "correlacao_cruzada":
            mascara = (input().split(","))

            # transformar componentes do vetor em int
            v1 = [int(i) for i in v1]
            mascara = [int(i) for i in mascara]

            v1 = correlacao_cruzada(v1, mascara)

        print(v1)

if __name__=='__main__':
    main()

def reverter(genoma:list, i:int, j:int) -> list:
    while i < j:
        aux = genoma[i]
        genoma[i] = genoma[j]
        genoma[j] = aux

        i += 1
        j -= 1

    return genoma

def transpor(genoma:list, i:int, j:int, k:int) -> list:
    parteRemovida = genoma[i:j+1]
    genoma = remover(genoma, i, j)
    genoma = combinar(genoma, parteRemovida, i+(k-j) )

    return genoma

def combinar(genoma:list, g:str, i:int) -> list:
    for char in g:
        genoma.insert(i, char)
        i+=1

    return genoma

def concatenar(genoma:list, g:str) -> list:
    genoma.extend(g)
    return genoma

def remover(genoma:list, i:int, j:int) -> list:
    for k in range( (j-i)+1 ): # número de elementos para remover + 1 (para se adequar ao range())
        genoma.pop(i)

    return genoma

def transpor_e_reverter(genoma:list, i:int, j:int, k:int) -> list:
    genoma = transpor(genoma, i, j, k)

    genoma[i:j+1] = genoma[i:j+1][::-1]
    genoma[j+1:k] = genoma[j+1:k][::-1]

    return genoma

def buscar(genoma:list, g:str) -> int:
    numOcorrencias = 0

    for posGenoma in range(len(genoma)):
        posG = 0
        while genoma[posGenoma] == g[posG]: # enquanto os caracteres forem iguais
            if posG == len(g)-1:            # se o final do genoma g foi alcançado, então houve uma correspondência
                numOcorrencias+=1
                break

            if posG < len(g)-1 and posGenoma < len(genoma)-1: # verificar limites da lista
                posG+=1
                posGenoma+=1
            else:
                break

    return numOcorrencias

def buscar_bidirecional(genoma:list, g:str) -> int:
    numOcorrencias = buscar(genoma, g)
    genoma.reverse()
    numOcorrencias += buscar(genoma, g)
    genoma.reverse() # por algum motivo, reverse() está afetando a variável genoma de main(), e não a local de buscar_bidirecional()

    return numOcorrencias

def mostrar(genoma:list) -> None:
    print(*genoma, sep="")


def main():
    genoma = list(input())

    comando = ""
    while comando != "sair":
        entrada = input().split()
        comando = entrada[0]

        match comando:
            case "reverter":
                genoma = reverter(genoma, int(entrada[1]), int(entrada[2]))
            case "transpor":
                genoma = transpor(genoma, int(entrada[1]), int(entrada[2]), int(entrada[3]))
            case "combinar":
                genoma = combinar(genoma, entrada[1], int(entrada[2]))
            case "concatenar":
                genoma = concatenar(genoma, entrada[1])
            case "remover":
                genoma = remover(genoma, int(entrada[1]), int(entrada[2]))
            case "transpor_e_reverter":
                genoma = transpor(genoma, int(entrada[1]), int(entrada[2]), int(entrada[3]))
            case "buscar":
                print(buscar(genoma, entrada[1]))
            case "buscar_bidirecional":
                print(buscar_bidirecional(genoma, entrada[1]))
            case "mostrar":
                mostrar(genoma)

main()


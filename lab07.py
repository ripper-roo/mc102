def encontrarChave(textoCriptografado:list, operador:str, operando1:str, operando2:str) -> int:
    vogais = ["a","e","i","o","u"]
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    consoantes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    pos1 = pos2 = 0
    numeroQuebraDeLinha = 0 # contar o número de \n's alcançados e subtrair no cálculo do índice

    # encontrando o operador 1

    if operando1 == "vogal":
        for k in range(len(textoCriptografado)):
            char = textoCriptografado[k]

            if char == '\n':
                numeroQuebraDeLinha += 1
            elif char.lower() in vogais:
                pos1 = k - numeroQuebraDeLinha
                break
    elif operando1 == "numero":
        for k in range(len(textoCriptografado)):
            char = textoCriptografado[k]

            if char == '\n':
                numeroQuebraDeLinha += 1
            elif char.lower() in numeros:
                pos1 = k - numeroQuebraDeLinha
                break
    elif operando1 == "consoante":
        for k in range(len(textoCriptografado)):
            char = textoCriptografado[k]

            if char == '\n':
                numeroQuebraDeLinha += 1
            elif char.lower() in consoantes:
                pos1 = k - numeroQuebraDeLinha
                break
    else:
        for k in range(len(textoCriptografado)):
            char = textoCriptografado[k]

            if char == '\n':
                numeroQuebraDeLinha += 1
            elif char == operando1:
                pos1 = k - numeroQuebraDeLinha
                break

    # encontrando o operador 2

    if operando2 == "vogal":
        for k in range(pos1+numeroQuebraDeLinha, len(textoCriptografado)):
            char = textoCriptografado[k]

            if char == '\n':
                numeroQuebraDeLinha += 1
            elif char.lower() in vogais:
                pos2 = k - numeroQuebraDeLinha
                break
    elif operando2 == "numero":
        for k in range(pos1+numeroQuebraDeLinha, len(textoCriptografado)):
            char = textoCriptografado[k]

            if char == '\n':
                numeroQuebraDeLinha += 1
            elif char.lower() in numeros:
                pos2 = k - numeroQuebraDeLinha
                break
    elif operando2 == "consoante":
        for k in range(pos1+numeroQuebraDeLinha, len(textoCriptografado)):
            char = textoCriptografado[k]

            if char == '\n':
                numeroQuebraDeLinha += 1
            elif char.lower() in consoantes:
                pos2 = k - numeroQuebraDeLinha
                break
    else:
        for k in range(pos1+numeroQuebraDeLinha, len(textoCriptografado)):
            char = textoCriptografado[k]

            if char == '\n':
                numeroQuebraDeLinha += 1
            elif char == operando2:
                pos2 = k - numeroQuebraDeLinha
                break

    # calculando chave

    if operador == "+":
        return pos1+pos2
    elif operador == "-":
        return pos1-pos2
    if operador == "*":
        return pos1*pos2
        

def descriptografar(textoCriptografado:list, chave:int) -> list:
    textoDescriptografado = []
    for k in textoCriptografado:
        if k == '\n':
            textoDescriptografado.append(k) # adicionar as quebras de linha
            continue

        codePoint = ord(k)+chave

        # fazer com que o codePoint fique na faixa 32-126

        while codePoint > 126: 
            codePoint = (codePoint%126) + (codePoint//126)*31
        while codePoint < 32:
            codePoint = 127 - (32-codePoint)

        textoDescriptografado.append(chr(codePoint))

    return textoDescriptografado



def main() -> None:

    operador = input()
    operando1 = input()
    operando2 = input()
    nLinhas = int(input())

    textoCriptografado = []
    for k in range(nLinhas):
        linha = input()
        textoCriptografado.extend(linha)
        textoCriptografado.append('\n')     # para saber onde acaba a linha no momento da impressão
    textoCriptografado.pop()                # retirar o último \n sobrante

    chave = encontrarChave(textoCriptografado, operador, operando1, operando2)
    textoDescriptografado = descriptografar(textoCriptografado, chave)

    print(chave)
    print(*textoDescriptografado, sep="")

if __name__=='__main__':
    main()
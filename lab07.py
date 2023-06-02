def encontrarChave():
    pass

def descriptografar():
    pass

def main() -> None:

    operador = input()
    operando2 = input()
    operando1 = input()
    nLinhas = int(input())

    textoCriptografado = []
    for k in range(nLinhas):
        linha = input()
        textoCriptografado.extend(linha)

    encontrarChave(operador, operando1, operando2)
    textoDescriptografado = descriptografar()
    print(textoDescriptografado)

if __name__=='__main__':
    main()
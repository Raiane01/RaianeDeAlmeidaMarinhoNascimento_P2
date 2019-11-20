import copy

def inverter(entrada_matriz):
    matriz = copy.deepcopy(entrada_matriz)

    det_matriz = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    matriz[0][0], matriz[1][1] = matriz[1][1], matriz[0][0]

    if det_matriz == 0:
        return None

    det_matriz = 1/det_matriz

    matriz[0][1] = -matriz[0][1]
    matriz[1][0] = -matriz[1][0]

    for linha in range(2):
        matriz[linha][0] *= det_matriz
        matriz[linha][1] *= det_matriz

    return matriz

def main():
    matriz = [0] * 2

    for linha in range(2):
        matriz[linha] = [0] * 2

    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())

    matriz[0][0] = a
    matriz[0][1] = b
    matriz[1][0] = c
    matriz[1][1] = d
    
    inverte_matriz = inverter(matriz)

    if inverte_matriz == None:
        print("Nao e inversivel")

    else:
        for linha in range(2):
            for coluna in range(2):
                print(matriz[linha][coluna], end=('\t'))
            print()

        for linha in range(2):
            for coluna in range(2):
                print(inverte_matriz[linha][coluna], end=('\t'))
    print()

main()

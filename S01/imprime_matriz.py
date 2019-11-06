def imprime_matriz(matriz):
    for i in range(len(matriz)):
        j = 0
        for j in range(len(matriz[i])):
            if j < len(matriz[i]) - 1:
                print(matriz[i][j], end=" ")
            else:
                print(matriz[i][j], end="")
        print("")

minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
#import ordenada as o

def ordena(lista):
    """Recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada em ordem crescente."""
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
            j += 1
        i += 1

    return lista


def main():
    #o.testa_ordenacao(ordena( [1, 3, 5, 0, 2, 4]), True)
    #o.testa_ordenacao(ordena( [1, 800, 3232, 24, 23, 23, 33, 32]), True)
    #o.testa_ordenacao(ordena( [0, 10, 99, 98, 98, 98, 98, 3, 5, 0, 2, 4]), True)
    pass

main()
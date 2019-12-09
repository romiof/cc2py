# Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e
#   devolve o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de busca binária.
#  Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.
#
# Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve "imprimir" cada um dos índices testados pelo algoritmo.

def busca(lista, valor):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        # Palplite é procurar no meio da lista
        meio = (esquerda + direita) // 2
        print(meio)
        if lista[meio] == valor:
            return meio
        # Se não acharmos no meio, vamos ver se está no começo ou no fim
        elif valor < lista[meio]:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return False

def testa_bb(lista, valor, posicao):
    x = busca(lista, valor)
    if x == posicao:
        print("Teste OK !")
    else:
        print("ERRO! Esperada posicao", posicao, "recebido ", x, "  ##   Lista: ", lista, "Procurei por:", valor)

def main():
    #testa_bb(['a', 'e', 'i'], 'e', 1)
    #testa_bb([1, 2, 3, 4, 5], 6, False)
    #testa_bb([1, 2, 3, 4, 5, 6], 4, 3)

    #testa_bb([1, 2, 3, 4, 5], 6, False)
    #testa_bb([1, 2, 3, 4, 5, 6], 4, 3)

    #busca([1, 2, 3, 4, 5, 6], 4)
    #busca([0,1,2,3,4,5], 4)
    pass

main()


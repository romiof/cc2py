def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False


def testa_busca(lista, elemento, re):
    temp = busca(lista, elemento)
    if temp == re:
        print("Teste OK!")
    else:
        print("Erro !! Esperado:", re, "Porém recebido", temp)


def main():
    testa_busca( ['a', 'e', 'i'], 'e', 1)
    testa_busca( [12, 13, 14], 15, False)
    testa_busca( ['casa', 'bola', 'lua'], 'cobra', False)


main()
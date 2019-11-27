def ordenada(lista):
    """ Recebe uma lista com números inteiros e retorna se está ordenada"""
    retorno = True
    for i in range(len(lista)):
        if i < len(lista) -1 :
            if lista[i] > lista[i +1]:
                return False
                
    return retorno


def testa_ordenacao(lista, param):
    a = ordenada(lista) 
    if a == param:
        print("Correto")
    else:
        print("ERRO! Esperado:", param, "recebido", a)


def main():
    #testa_ordenacao ( [0, 3, 1, 2, 3, 4, 5, 6, 7], False)
    #testa_ordenacao ( [0, 1, 2, 3, 4, 5, 6, 7], True)
    #testa_ordenacao ( [-8, -2, 1, 2, 3, 4, 5, 680, 77], False)
    pass

main()


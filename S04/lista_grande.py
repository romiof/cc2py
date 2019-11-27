import random

def  lista_grande(n):
    """Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n e devolve uma lista contendo n números inteiros aleatórios."""
    lista = []
    for i in range(n):
        lista.append( random.randint(-100, 100))
    
    return lista


def testa_qtde(n):
    tam = lista_grande(n)
    #print (tam)
    if len(tam) == n:
        print("Correto!")
    else:
        print("ERRO! Esperado tamanho", n, "mas foi recebido", len(tam))


def main():
    testa_qtde(9)
    testa_qtde(19)
    testa_qtde(29)


main()
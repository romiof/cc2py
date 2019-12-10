# Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista de números inteiros
# e devolve uma outra lista apenas com os números ímpares da lista dada.
#
# DICA: você vai precisar do método extend() que as listas possuem.
#

def encontra_impares(lista):
    lista_impares = [] 
    if lista[0]%2 != 0:
        #lista_impares.extend(lista)
        lista_impares.append(lista[0])
    # BASE RECURSAO
    if len(lista) == 1:
        return lista_impares
    # CHAMADA RECURSIVA
    else:
        #print (lista_impares)
        return lista_impares + encontra_impares(lista[1:])

#def main():
#    lis = [1, 2, 3, 4 ,6 ,8 ,9 ,0 ,1]
#    print(encontra_impares( lis ) )
#
#main()

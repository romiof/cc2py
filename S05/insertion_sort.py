def insertion_sort(lista):
    fim = len(lista)
    for i in range(fim):
        for j in range(fim - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                #print(lista)
    return lista

#insertion_sort( [3, 5, 1, 9, 12, 4, -99, 2, 0, -1, 99, 100, 70, 60, -90, ] )
def dimensoes(matriz):
    x = len(matriz)
    for item in matriz:
        y = 0
        y = y + len(item)
    return x, y


def soma_matrizes(m1, m2):
    x1, y1 = dimensoes(m1)
    x2, y2 = dimensoes(m2)
    m = []
    if x1 == x2 and y1 == y2:
        for i in range(len(m1)):
            m.append([])
            j = 0
            for j in range(len(m1[i])):
                m[i].append( m1[i][j] + m2[i][j] )
        return m
    else:
        return False
    

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]


print(soma_matrizes(m1, m2))



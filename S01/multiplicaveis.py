def dimensoes(matriz):
    x = len(matriz)
    for item in matriz:
        y = 0
        y = len(item)
    return x, y

def sao_multiplicaveis(m1, m2):
    x1, y1 = dimensoes(m1)
    x2, y2 = dimensoes(m2)
    if y1 == x2:
        return True
    else:
        return False

m1 = [[1], [1], [1]]
m2 = [[1, 2, 3], [1, 2, 3]]
print(sao_multiplicaveis(m1, m2))
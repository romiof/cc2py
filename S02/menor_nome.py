# Função que recebe uma lista de string contendo nome de pessoas como parametro.
# Deve devolver o nome mais curto
# IGNORAR espaços antes e depois do nome, e devolver o nome Capitalizado

def menor_nome(lista):
    nome_curto = lista[0]
    for nome in lista:
        if len(nome.strip()) < len(nome_curto.strip()):
            nome_curto = nome
    return nome_curto.strip().capitalize()


def testa_menor_nome(lista, nome_curto):
    teste = menor_nome(lista)
    if teste != nome_curto:
        print("ERRO !!! esperado string", nome_curto, "e recebido", teste)
    else:
        print("OK")


def main():
    #lista_nomes = ['nu            ', 'Isadora', 'Tere', 'Ana ', 'Nome2 ']
    #menor_nome (lista_nomes)
    testa_menor_nome( ['nu            ', 'Isadora', 'Tere', 'Ana ', 'Nome2 '], "Nu" )
    testa_menor_nome( ['CAssio ', 'Felipe  ', '   Cristiano ', 'katia   ', 'FErnando', 'CAMILA   '], "Katia" )
    testa_menor_nome( ['ncasa ', 'Jao  ', '   aJJ ', 'Gustavo   ', 'gabi', 'CAMILA   '], "Jao" )


main()


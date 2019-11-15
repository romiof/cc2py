# Escreva uma função que receba uma lista de strings e retorne o primeiro string na ordem Lexográfica (ASCII)
# Ignorar na comparação MAIUS e MINUS quando foi feito o exercício do vídeo.
# No exercício para entregar, comparar MAIUS e MINUS.

def primeiro_lex(lista):
    str_ordenada = lista[0].strip()
    for nome in lista:
        if nome.strip() < str_ordenada.strip():
            str_ordenada = nome.strip()
    return str_ordenada

def testa_menor_str(lista, nome_curto):
    teste = primeiro_lex(lista)
    if teste != nome_curto:
        print("ERRO !!! esperado string", nome_curto, "e recebido", teste)
    else:
        print("OK")


def main():
    testa_menor_str( ['nu            ', 'Isadora', 'Tere', 'Ana ', 'Nome2 '], "Ana" )
    testa_menor_str( ['CADssio ', 'Felipe  ', '   Cristiano ', 'katia   ', 'FErnando', 'CAMILA   '], "CADssio" )
    testa_menor_str( ['ncasa ', 'Jao  ', '   aJJ ', 'Gustavo   ', 'gabi', 'CAMILA   '], "CAMILA" )


main()
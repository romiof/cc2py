# Escreva uma função que conta quantas letras tem de consoantes ou de vogais na palavra
# Ignorar caracteres não presente na tabela ASCII ( 65 - 90 )

def conta_letras(frase, contar="vogais"):
    qtde = 0
    frase = frase.lower().strip()
    for c in frase:
        if ord(c) >= 97 and ord(c) <= 122:
            if contar == "vogais" and (c == "a" or c == "e" or c == "i" or c == "o" or c == "u"):
                qtde += 1
            elif contar == "consoantes" and c != "a" and c != "e" and c != "i" and c != "o" and c != "u":
                qtde += 1
    return qtde


def testa_conta_letras(qtde, palavra, tipo="vogais"):
    if conta_letras(palavra, tipo) != qtde:
        print("ERRO !!! esperado contagem de", qtde, "e recebido", conta_letras(palavra, tipo))
    else:
        print("OK")


def main():
    testa_conta_letras(6, "programamos em python")
    testa_conta_letras(6, "programamos em python", "vogais")
    testa_conta_letras(13, "programamos em python", "consoantes")


main()
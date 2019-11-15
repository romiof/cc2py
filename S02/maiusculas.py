# Escreva uma função que receba uma string e diga quais posições as letras são maiusculas.
# Ignorar caracteres não presente na tabela ASCII ( 65 - 90 )

def maiusculas(palavra):
    letrasMa = ""
    for c in palavra:
        if ord(c) >= 65 and ord(c) <= 90:
            letrasMa += c
    return letrasMa


def testa_maiusculas(palavra, letras):
    if maiusculas(palavra) != letras:
        print("ERRO !!! esperado string", letras, "e recebido", maiusculas(palavra))
    else:
        print("OK")


def main():
    testa_maiusculas("Programamos em python 2?", "P")
    testa_maiusculas("Programamos em Python 3.", "PP")
    testa_maiusculas("PrOgRaMaMoS em python!", "PORMMS")


main()
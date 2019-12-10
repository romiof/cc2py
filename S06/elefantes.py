def incomodam(n):
    """Implemente a função incomodam(n) que devolve uma string contendo "incomodam " (a palavra seguida de um espaço) N vezes.
    Se N não for um inteiro estritamente positivo, a função deve devolver uma string vazia.
    Essa função deve ser implementada utilizando recursão."""
    if n < 1:
        return str("")
    else:
        return "incomodam " + incomodam(n - 1)

def elefantes(n, i = 1):
    """Utilizando a função acima, implemente a função elefantes(n) que devolve uma string contendo a letra da música
    "Um elefante incomoda muita gente" de 1 até n elefantes. Se n não for maior que 1, a função deve devolver uma string vazia.
    Essa função também deve ser implementada utilizando recursão."""
    musica = ""
    if n <= 1:
        return ""
    else:
        if i == 1:
            musica = "Um elefante incomoda muita gente\n"
        else:
            musica = str(i) + " elefantes incomodam muita gente\n"
        return musica + str(i+1) + " elefantes " + incomodam(i+1) + "muito mais\n" + elefantes(n-1, i+1)

#print (incomodam(2))
#print (elefantes(4))
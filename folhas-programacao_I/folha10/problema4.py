#Problema 4

"""
 Implemente uma função encontra que recebe um iterável (de um dos tipos
aprendidos nas aulas) e um elemento e devolva um tuplo com as posições em
que se encontra o elemento. Caso o elemento não exista, deve ser lançada a
exceção KeyError com uma mensagem de texto adequada.
"""


def encontra(iteravel, elemento):
    """
    Determina as posições de um elemento num iterável.
    
    Requires: iteravel é um iterável.
    Ensures: devolve um tuplo com as posições
    do elemento ou lança KeyError se não existir.
    """
    posicoes = ()
    i = 0
    
    for valor in iteravel:
        if valor == elemento:
            posicoes = posicoes + (i,)
            
        i += 1

    if len(posicoes) == 0:
        raise KeyError("Elemento não encontrado")

    return posicoes
        
    

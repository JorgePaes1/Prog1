def concatenar_listas( lista1 , lista2):
    """
    Concatena elementos de duas listas de strings do mesmo tamanho.

    :param lista1: a primeira lista de strings.
    :param lista2: a segunda lista de strings.
    :return: uma lista com a concatenação dos elementos de mesmo índice da duas listas.
    """
    if len(lista1) != len(lista2):
        raise ValueError('As listas não tem o mesmo tamanho')
    
    resultado = []
    for i in range(len(lista1)):
        resultado.append(lista1[i] + lista2[i])
    
    return resultado

lista1 = ['a','b','c']
lista2 = ['x','y','z']
resultado = concatenar_listas(lista1 , lista2)
print(resultado)

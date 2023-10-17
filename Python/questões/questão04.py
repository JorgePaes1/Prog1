'''
Dada uma lista onde cada elemento corresponde a uma outra lista, faça
um filtro para obter uma lista onde cada lista interna seja homogênea de números
inteiros. Retorna a lista resultante.
'''

def listas_homogeneas(lista_de_listas):
    '''
    Filtra a lista de listas para obter uma lista de listas onde cada lista interna contém apenas inteiros.

    :param lista_de_listas: Lista de listas.
    :return: Lista de listas homogêneas de numeros inteiros. 
    '''
    lista_filtrada = [lst for lst in lista_de_listas if all(isinstance(item, int) for item in lst)]
    return lista_filtrada

# Exemplo de uso:
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 'x'], ['a', 'b', 'c']]
listas_filtradas = listas_homogeneas(lista_de_listas)
print(listas_filtradas)

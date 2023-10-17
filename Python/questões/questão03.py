'''
Dada uma lista de string, faça um filtro para obter uma lista somente com
os elementos cujo tamanho da string seja menor que 10. A lista resultante deve estar
ordenada em ordem alfabética. Retorna a lista resultante.
'''

def filtro_ordem_alfabetica(lista):
    '''
    Filtra os elementos da lista com tamanho de string menor que 10 e retorna a lista em ordem alfabetica.

    :param lista: Lista de Strings.
    :param return: Lista de strings filtrada e ordenada.
    '''
    lista_filtrada = list(filter(lambda s: len(s) < 10, lista))
    lista_ordenada = sorted(lista_filtrada)
    return lista_ordenada

lista_de_strings = ["maçã", "banana", "laranja", "uva", "abacaxi", "pera", "melancia"]
lista_filtrada_ordenada = filtro_ordem_alfabetica(lista_de_strings)
print(lista_filtrada_ordenada)

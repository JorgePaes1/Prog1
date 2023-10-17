'''
Dada uma lista de string e uma lista de números inteiros, faça um filtro
para obter uma lista de string onde o tamanho do elemento é menor ou igual ao valor
do número inteiro de índice correspondente. Retorna a lista resultante
'''

def filtrar_strings(lista_strings: list, lista_inteiros: list):
    lista_filtrada = []
    for string, inteiro in zip(lista_strings, lista_inteiros):
        if len(string) <= inteiro:
            lista_filtrada.append(string)
    return lista_filtrada

# Exemplo de uso:
lista_de_strings = ["abc", "de", "fghij", "k", "lmq"]
lista_de_numeros = [2, 1, 5, 0, 3]
lista_filtrada = filtrar_strings(lista_de_strings, lista_de_numeros)
print(lista_filtrada)  # Saída: ['abc', 'de', 'k', 'lmnopq']


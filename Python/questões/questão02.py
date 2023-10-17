'''
Dada uma lista de números inteiros, faça o mapeamento para obter uma
lista de números primos. Cada elemento da lista deve ser igual ao menor número
primo maior que o elemento corrente da lista.
'''

def e_primo(numb) :
    '''Verifica se o número é primo.'''
    if numb < 2:
        return False
    for i in range(2, int(numb**0.5) + 1):
        if numb % i == 0:
            return False
    return True

def menor_primo_maior_que(numb):
    '''Encontra o menor número primo maior que o número dado.'''
    numb += 1
    while True:
        if e_primo(numb):
            return numb
        numb += 1
    
def primos_maiores_que(lista):
    '''
    Gera uma lista de números primos, onde cada elemento é o menor número primo maior que o elemento da lista original.

    :param lista: Lista de números inteiros.
    :return: Lista de números primos
    '''
    lista_primos = [menor_primo_maior_que(numb) for numb in lista]
    return lista_primos

# Exemplo de uso:
numeros = [10, 20, 30, 40, 50]
lista_de_primos = primos_maiores_que(numeros)
print(lista_de_primos)

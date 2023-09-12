def criar_list_revers(lista):
    return lista[::-1]

def criar_list_impar(lista):
    for i in range(len(lista)):
        if i % 2 != 0:
            print(lista)


def criar_list_metade(lista):
    fim = len(lista) // 2
    return lista[:fim]

def criar_list_segunda_metade(lista):
    inicio = len(lista) //2
    return lista[inicio:]


def maior_valor(lista):
    maior = lista[0]
    for valor in lista[1:]:
        maior = (maior + valor + abs(maior-valor)) // 2
    return maior

def calcular_saldo_medio(cadastro):
    saldo_medio = 0
    for elemento in cadastro:
        saldo_medio += elemento['saldo']
    return saldo_medio / len(cadastro)

def remove_gmail(cadastro,dominio):
    filtro = []
    for elemento in cadastro:
        if dominio not in elemento['e-mail']:
            filtro.append(elemento)
    return filtro

def filtrar_por_tipo(lista, tipo):
    lista_filtrada = []
    for item in lista:
        if type(item) == tipo:
            lista_filtrada.append(item)
    return lista_filtrada 

def filtrar_nome(lista):
    filtro = []
    for elemento in lista:
        filtro.append(elemento['nome'])
    return filtro

def formata_nomes(lista_nomes, modo):
    lista_formatada = []
    if modo == 'CAIXA ALTA':
        for item in lista_nomes:
            lista_formatada.append(item.upper())
    elif modo == 'CAIXA BAIXA':
        for item in lista_nomes:
            lista_formatada.append(item.lower())
    else:
        print('Formatação invalida')
    return lista_formatada


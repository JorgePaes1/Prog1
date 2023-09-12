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

'''
Fazer uma interface com uma lista de dicionarios usando controle de fluxo de tratamento de excenção
1°- Fazer uma função que receba valores de um cadastro e adicione numa de lista de dicionario.
2°- Fazer uma função que listar todos os cadastros
3°- Aplicar o controle de fluxo de tratamento de error
'''

def cadastro():
    cadastro = []
    while True:
        try:
            nome = input("Digite seu nome:\n")
            if not all(c.isalpha() or c.isspace() for c in nome):
                raise ValueError("O nome deve conter apenas letras")
            idade = input("Digite sua idade:\n")
            email = input("Digite seu email:\n")
            cpf = input("Digite seu cpf:\n")
            dicionario = {"Nome": nome,
                          "Idade": idade,
                          "Email": email,
                          "CPF": cpf,
                          }
            cadastro.append(dicionario)
            resposta = input("Deseja continuar cadastrando? (S/N):\n")
            if resposta.lower() == "n":
                break
        except Exception as e:
            print(e)
    return cadastro


def listar(cadastro):
    for pessoa in cadastro:
        print(f"\nNome: {pessoa['Nome']}")
        print("Dados:")
        for chave, valor in pessoa.items():
            if chave != "Nome":
                print(f"{chave}: {valor}")
        print()


cadastro = cadastro()
listar(cadastro)

'''
Fazer uma interface com uma lista de dicionarios usando controle de fluxo de tratamento de excenção
1°- Fazer uma função que receba valores de um cadastro e adicione numa de lista de dicionario.
2°- Fazer uma função que listar todos os cadastros
3°- Aplicar o controle de fluxo de tratamento de error
'''
import re  # biblioteca usada para formata

# iniciamos a nossa função cadastro


def cadastro():
    # criamos umas lista para armazenar e retorna como umas lista de dicionarios
    cadastro = []
    # criamos umm laço de repetição para fazer as perguntas
    while True:
        # iniciamos com a nossa estrutura de tratamento de error
        try:
            nome = input("Digite seu nome:\n")  # primeiro perguntamos o nome
            # usando um laço de condição, caso o que tá entre parêntes seja FALSE, refazemos a pergunta até atender as condições
            if not all(c.isalpha() or c.isspace() for c in nome):
                # a função raise lança a nossa excesão caso não seje verdadeiro a função all
                raise ValueError("O nome deve conter apenas letras")
            while True:  # iniciamos outro laço de repetição para pergunta a idade
                try:  # caso o usuario coloque a idade sendo um número inteiro o laço para e seguimos para a proxima pergunta
                    idade = int(input("Digite sua idade:\n"))
                    break
                except ValueError:  # caso ele digite algo que não seja um número, ativamos a nossa função raise e refazemos a pergunta
                    print("A idade deve ser um número inteiro.")
            while True:  # iniciamos outro laço para pergunta o email
                try:  # se o usuario digita o email no formato certo paramos o laço e continuamos o código
                    # usamos a função regular para verificar se o usuario irá digitar o email no formato correto
                    email = input("Digite seu email:\n")
                    # a função re verifica se o email começa com @ e termina com gmail ou hotmail.com
                    if re.match(r"[^@]+@(gmail|hotmail)\.com", email):
                        break
                    else:  # se o email não tiver no formato correto, refazemos a pergunta com a função raise
                        raise ValueError(
                            "O email deve estar no formato gmail.com ou email.com")
                except ValueError as e:
                    print(e)
            while True:  # fazemos um laço para perguntar o CPF
                try:  # se o CPF for digitado de maneira correta continuamos com o código
                    cpf = input("Digite seu cpf:\n")
                    # usamos a função re para verificar se o CPF obedece o formato 000.000.000-00
                    if re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
                        break
                    else:  # senão lançamos a nossa excesão e refazmos a pergunta
                        raise ValueError(
                            "Formato de CPF errado, digite da seguinte forma: 000.000.000-00")
                except ValueError as e:
                    print(e)
            # adicionamos todos os dados a um dicionario
            dicionario = {"Nome": nome,
                          "Idade": idade,
                          "Email": email,
                          "CPF": cpf,
                          }
            # e adicionamos o dicionario a lista cadastro
            cadastro.append(dicionario)
            # perguntamos ao usuario se ele quer cadastra outra pessoa
            resposta = input("Deseja continuar cadastrando? (S/N):\n")
            if resposta.lower() == "n":  # se a resposta dele for n(não), finalizamos o cadastro, senão repetimos o laço
                break
        except Exception as e:
            print(e)
    return cadastro  # retornamos a nossa lista de dicionarios cadastro

# criamos a nossa função de printar os cadastros


def listar_cadastro(cadastro):
    # usamos a função enumerete para printar a lista
    for i, pessoa in enumerate(cadastro, start=1):
        # usando o contador i, printamos o número do dicionario para ficar mais visivel ao usuario
        print(f"\nCadastro {i}:")
        # printamos primeiramente o nome da pessoa
        print(f"\nNome: {pessoa['Nome']}")
        print("Dados:")  # agora vem os dados
        for chave, valor in pessoa.items():  # usamos a função items que cria uma lista de tupla de chaves e valores (pares de chave-valor)
            if chave != "Nome":  # já printamos o nome então seguimos com o resto dos dados
                print(f"{chave}: {valor}")
        print()


cadastro = cadastro()
listar_cadastro(cadastro)

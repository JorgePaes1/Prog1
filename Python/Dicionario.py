import funcoes as f

cadastro = [
    {
        'nome' : 'Renato',
        'e-mail': 'renato@email.com',
        'saldo': 108
    },
    {   
        'nome' : 'Jose',
        'e-mail': 'Jose@email.com',
        'saldo': 1024

    },
    {
        'nome' : 'Maria',
        'e-mail': 'Maria@gmail.com',
        'saldo': 56
    },
    {
        'nome' : 'Joao',
        'e-mail': 'Joao@gmail.com',
        'saldo': 50
    }
]

extrair_nomes = f.filtrar_nome(cadastro)
nomes = f.formata_nomes(extrair_nomes, 'CAIXA BAIXA')
print(f'nomes: {nomes}')

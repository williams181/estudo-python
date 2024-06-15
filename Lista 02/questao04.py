"""
Ler o nome completo do usuário e imprimi-lo com o primeiro é último nome escritos todo em maiúsculas.
"""

nome_completo = input("Digite um nome: ")

partes_nome = nome_completo.split()

primeiro_nome = partes_nome[0]

ultimo_nome = partes_nome[-1]

primeiro_nome_maiusculo = primeiro_nome.upper()

ultimo_nome_maiusculo = ultimo_nome.upper()

print(primeiro_nome_maiusculo, *partes_nome[1:-1], ultimo_nome_maiusculo)
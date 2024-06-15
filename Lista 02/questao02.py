"""
Ler o nome do usuário e imprimi-lo em formato de escala, ou seja, só a primeira letra na primeira linha, as duas primeiras letras na
segunda inha, e assim por diante.
"""

nome = input("Dgite um nome: ")

for i in range(len(nome)):
    print(nome[:i+1])
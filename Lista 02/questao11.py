"""
Ler por linhas matriz M x N, onde M <= 4 e N <= 8 são lidos antes da leitura da matriz. Depois, percorrendo a matriz  por colunas, armazenar
em uma lista os elementos desta matriz que sejam múltiplos de 6. No final, imprimir de maneira organizada a matriz e o vetor.
"""
M = int(input("Digite o número de linhas da matriz (M <= 4): "))
N = int(input("Digite o número de colunas da matriz (N <= 8): "))
multiplos_de_6 = []
matriz = []
for i in range(M):
    linha = []
    for j in range(N):
        elemento = int(input(f"Digite o elemento da posição ({i+1}, {j+1}): "))
        linha.append(elemento)
        if elemento % 6 == 0:
            multiplos_de_6.append(elemento)
    matriz.append(linha)
print("Matriz:")
for i in range(M):
    for j in range(N):
        print(matriz[i][j], end=" ")
    print()
print("Vetor de múltiplos de 6:", multiplos_de_6)
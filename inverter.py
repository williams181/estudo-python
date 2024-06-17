# Inicializa a lista original
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Inicializa uma lista vazia para armazenar os números na ordem inversa
numeros_invertidos = []

# Percorre a lista original de trás para frente
for i in range(len(numeros) - 1, -1, -1):
    numeros_invertidos.append(numeros[i])

# Imprime a lista original
print("Lista original:", numeros)

# Imprime a lista invertida
print("Lista invertida:", numeros_invertidos)
"""
Ler uma lista de N números (N é informado pelo usuário antes), e depois criar duas outras listas com os números pares e ímpares separados.
No final imprimir as 3 listas.
"""

n = int(input("Informe o tamanho dos vetores: "))

vetor1 = []
vetor2 = []

print("Informe os valores do primeiro vetor:")
for i in range(n):
    valor = int(input(f"Elemento {i+i}: "))
    vetor1.append(valor)

print("Informe os valores do segundo vetor:")
for i in range(n):
    valor = int(input(f"Elemento {i+1}: "))
    vetor2.append(valor)

vetor_resultante = []
for i in range(n):
    soma = vetor1[i] + vetor2[i]
    print(soma)
    vetor_resultante.append(soma)

print("\nVetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor Resultante:", vetor_resultante)

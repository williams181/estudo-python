"""
Ler as notas finais de N alunos (N é informado pelo usuário antes),calcular e imprimir a média destas notas e depois imprimir as notas
que sejam maiores do que a média calculada.
"""

N = int(input('Quantidade de notas de alunos: '))
Lista_Notas = []

for i in range(N):
    Nota1 = float(input('Digite a nota'))
    Lista_Notas.append(Nota1)

soma = 0.0
Lista_Resultado = []

for i in Lista_Notas:
    print(i)
    soma += i

result = soma / len(Lista_Notas)
print(result)
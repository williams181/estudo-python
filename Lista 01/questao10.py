"""
Calcular o menor de uma séria de números inteiros lidos. A leitura dos números deve parar quando o número zero for lido.
"""

# menor

n = int(input('numero: '))
menor = n
while(n != 0):
    if (menor > n):
        menor = n
    n = int(input("numero: "))
print('menor', menor)

# maior

n = int(input('numero: '))
maior = n
while(n != 0):
    if (maior < n):
        maior = n
    n = int(input("numero: "))
print('maior', maior)
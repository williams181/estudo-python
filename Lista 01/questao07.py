"""
Somar os inteiros ímpares entre dois valores inteiros informados pelo usuário. # while
"""

v1 = int(input("Digite um valor para o intervalo:"))
v2 = int(input("Digite outro valor para o intervalo:"))

soma = 0

if v1 % 2 == 0:
    v1 = v1 + 1

for it in range(v1,v2+1):
    if (it % 2 != 0):
        soma = soma + it
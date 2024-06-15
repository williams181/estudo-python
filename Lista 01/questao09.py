"""
Ler um número inteiro N e imprimir o valor do n-ésimo termo da sequencia a seguir: [-1, 0, 5, 6, 11, 12, 17, 18, 23, 24...]
"""

n = int(input("numero1: "))

enesimo = -1

for i in range(1, n):
    if (enesimo % 2 != 0):
        enesimo += 1
    else:
        enesimo += 5 # enesimo = enesimo + 5
print('o valor do','enesimo é:',enesimo)


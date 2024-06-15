"""
O mínimo múltiplo comum (MMC) de 2 números inteiros positivos é o menor número inteiro que é multiplo de ambos. Seu programa deve ler 2
números inteiros positivos e determinar o MMC destes 2 números.
"""

nip1 = int(input('Digite o 1º número inteiro:'))
nip2 = int(input('Digite o 2º número inteiro:'))

if nip1 > nip2:
    nip1, nip2 = nip2, nip1

ac = nip2
mmc = 0

while mmc == 0:
    if ac % nip1 == 0 and ac % nip2 == 0:
        mmc = ac
    ac = ac + 1

print('O MMC dos números', nip1, ' e ', nip2, ' é ', mmc)
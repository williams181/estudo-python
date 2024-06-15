"""
Somar os inteiros pares entre 50 e 100 (inclusive)
"""

Soma = 0

for i in range (50,101):
    if (i % 2 == 0):
        Soma  = Soma + i
print("result", Soma)
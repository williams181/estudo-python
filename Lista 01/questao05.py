"""
Calcular o fatorial de um número inteiro lido # while
"""
num = int(input("numero: "))

result = 1 
count = 1

while count <= num:
    result = result * count
    count = count + 1
print(f"resul: {result:.0f}")

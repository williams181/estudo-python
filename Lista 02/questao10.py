"""
Altere o programa anterior para garantir que o usuário digitará no máximo 100 números.
"""
numbers = []

while len(numbers) < 100:
    num = int(input("Digite um número inteiro (negativo para parar): "))
    if num < 0:
        break
    if 10 <= num <= 99:
        numbers.append(num)

i = len(numbers) - 1
while i >= 0:
    print(numbers[i])
    i -= 1

"""
Ler uma sequencia de números inteiros positivos (ou zero). A leitura deve parar com a digitação de um número negativo. O seu programa
deve imprimir os números lidos cujos valores tem dois dígitos significativos, mas na ordem inversa em que forem lidos - o último número
lido deve ser o primeiro a ser impresso.
"""
numbers = []

while True:
    num = int(input("Digite um número inteiro (negativo para parar): "))
    if num < 0:
        break
    if 10 <= num <= 99:
        numbers.append(num)

i = len(numbers) - 1
while i >= 0:
    print(numbers[i])
    i -= 1

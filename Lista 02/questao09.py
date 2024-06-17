"""
Ler uma sequencia de números inteiros positivos (ou zero). A leitura deve parar com a digitação de um número negativo. O seu programa
deve imprimir os números lidos cujos valores tem dois dígitos significativos, mas na ordem inversa em que forem lidos - o último número
lido deve ser o primeiro a ser impresso.
"""
numbers = []

num = int(input("Digite um número inteiro (negativo para parar): "))

while num > 0:
    num = int(input("Digite um número inteiro (negativo para parar): "))
    if 10 <= num <= 99:
        numbers.append(num)

numeros_invertidos = []

for i in range(len(numbers) -1, -1, -1):
    numeros_invertidos.append(numbers[i])
    
print(numeros_invertidos)
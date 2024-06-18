"""
Faça um programa Python para ler uma sequencia de números inteiros - a leitura para quando o número zero for lido. No entanto, o usuário
só deve digitar no maximo 150 números válidos. O prgrama deve imprimir as seguintes informações como resultado:
  * A quantidade total de números negativos lidos.
  * Os númeors positivos lidos cujos valores tiverem 4 dígitos significativos. A impressão destes números deve mostrar primeiro os números
    menores que 5100, na mesma ordem relativa em que foram lidos, e depois os maiores ou iguais a 5100, na ordem inversa da que foram lidos.
  * A média dos números positivos de 3 dígitos impressos no item anterior.
  * O menor número negativo lido.
  OBS1: Não pode usar as funções/métodos len, min, max, sum, nem sort.
"""

maximo = 150
pos4d = [0] * maximo
qtd = neg = menorNeg = qtd4d = med4d = 0

num = int(input("Digite um número: "))
while num == 0:
    num = int(input("Digite pelo menos um número válido: "))

while num != 0 and qtd < maximo:
    menorNeg = num
    qtd += 1
    if num < 0:
        neg = neg + 1
        if menorNeg > num:
            menorNeg = num
        pos4d[qtd4d] = num
        qtd4d += 1
    else:
        if 999 < num < 10000:
            med4d += num
            pos4d[qtd4d] = num
            qtd4d += 1
    num = int(input("Digite outro número, 0 p/parar: "))

if num != 0:
    print("Quant. máxima de números atingida, último número foi descartado!")

print('Quantidade de negativos =', neg)

if neg == 0:
    print('Nenhum negativo foi digitado, logo não existe menor.')
else:
    print('A quantidade de numeros negativos é: ', neg)
    print('O menor negativo digitado foi: ', menorNeg)
    
if qtd4d == 0:
    print('Nenhum positivo de 4 dígitos foi digitado, logo não existe média.')
else:
    # print('Positivos de 4 dígitos: ', end='')
    for i in range(qtd4d):
        if pos4d[i] < 5100 and pos4d[i] > 999:
            print(pos4d[i])
    for i in range(qtd4d-1, -1, -1): # inversa
        if pos4d[i] >= 5100 and pos4d[i] < 9999:
            print(pos4d[i])
    med4d = med4d / qtd4d

if med4d == 0:
    print("Não houve um numero positivo digitado.")
else:
    print('Média dos positivos de 4 dígitos:', med4d)

if neg == 0:
    print('Nenhum negativo foi digitado, logo não existe menor.')
else:
    print('O menor negativo digitado foi: ', menorNeg)
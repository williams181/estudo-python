"""
Faça um programa Python para ler uma sequencia de números inteiros - a leitura para quando o número -999999 for lido. No entanto, o
usuário só deve poder digitar no máximo 250 números. O programa deve imprimir as seguintes informações como resultado:
    * A quantidade total de números lidos.
    * Os números lidos cujo os valores tiverem 3 dígitos significativos. A impressão destes números devem mostrar primeiro os números
    negativos (de 3 dígitos), na mesma ordem relativa em que foram lidos, e depois os positivos (idem).
    * A soma dos números positivos de 3 dígitos impressos no item anterior.
    * O menor número positivo lido.
"""

maximo = 7
pos3d = [0] * maximo
qtd = neg = menorNeg = qtd3d = 0

num = int(input("Digite um número: "))
while (num != -999999 and qtd < maximo):
    # num = int(input("Digite um numero inteiro (-9999999 para parar): "))
    qtd += 1
    if num < 0:
        neg = neg + 1
        if num < menorNeg:
            menorNeg = num
    else:
        if 99 < num < 1000:
            pos3d.append(num)
            qtd3d += 1
    num = int(input("Digite outro número (-999999) para parar: "))

if num != 0:
    print("Quant. máxima de números atingida, último número foi descartado!")

print('Quantidade de negativos =', neg)

if qtd3d == 0:
    print('Nenhum positivo de 3 dígitos foi digitado, logo não existe média.')
else:
    print('Positivos de 3 dígitos: ', end='')
    for i in range(qtd3d):
        if pos3d[i] < 0:
            print(pos3d[i], end=', ')
        
    for i in range(qtd3d):
        if pos3d[i] > 0:
            print(pos3d[i], end=', ')

if neg == 0:
    print('Nenhum negativo foi digitado, logo não existe menor.')
else:
    print('O menor negativo digitado foi', menorNeg)
"""
### Questão 1

Faça um programa Python para ler uma sequência de números inteiros - a leitura para quando o número -1 for lido. No entanto, o usuário só deve poder digitar no máximo 200 números inteiros. O programa deve imprimir as seguintes informações como resultado (nesta ordem):

  * Os números lidos cujos valores têm 2 dígitos significativos e também são múltiplos de 3.
    A impressão destes números deve ser feita na ordem inversa da que foram lidos.
  * O maior número lido que não seja múltiplo de 4.

"""

qtd = 0
qtd3 = 0
mult3 = [0] * 200
maiorNaoMult4 = -999999999999
num = int(input("Digite um número inteiro (-1 para parar): "))
while num != -1 and qtd < 200:
    qtd += 1
    if (num % 3 == 0) and (num > -100) and (num < 100) and (abs(num) > 9):
        mult3[qtd3] = num
        qtd3 += 1
    if (num % 4 != 0) and (num > maiorNaoMult4):
        maiorNaoMult4 = num
    num = int(input("Digite outro número inteiro (-1 para parar): "))

if qtd3 == 0:
    print("Nenhum múltiplo de 3 com 2 dígitos foi digitado.")
else:
    mult3 = mult3[:qtd3]
    mult3.reverse()  # não usar reverse
    print("Múltiplos de 3 com 2 dígitos significativos:", mult3)

if maiorNaoMult4 == -999999999999:
    print("Nenhum número não múltiplo de 4 foi digitado.")
else:
    print("O maior não múltiplo de 4 é", maiorNaoMult4)

"""
### Questão 2

Faça um programa Python para ler uma sequência de números inteiros - a leitura para quando o número -888888 for lido. No entanto, o usuário só deve poder digitar no máximo 300 números. O programa deve imprimir as seguintes informações como resultado:

  * A quantidade total de números lidos.
  * Os números lidos cujos valores tiverem 2 dígitos significativos. A impressão destes números deve mostrar primeiro os números positivos (de 2 dígitos), na mesma ordem relativa em que foram lidos, e depois os negativos (idem).
  * A soma dos números negativos de 2 dígitos impressos no item anterior.
  * O maior número negativo lido.
"""

"""
Faça um programa Python para ler uma sequência de números inteiros - a leitura para quando o número -888888 for lido. No entanto, o usuário só deve poder digitar no máximo 300 números. O programa deve imprimir as seguintes informações como resultado:

  * A quantidade total de números lidos.
  * Os números lidos cujos valores tiverem 2 dígitos significativos. A impressão destes números deve mostrar primeiro os números positivos (de 2 dígitos), na mesma ordem relativa em que foram lidos, e depois os negativos (idem).
  * A soma dos números negativos de 2 dígitos impressos no item anterior.
  * O maior número negativo lido.
"""
# minha versao

maximo = 300
pos2d = [0] * maximo
qtd = neg = maiorNeg = qtd2d = somaNeg = 0

num = int(input("Digite um numero para começar: "))
while num == 0:
    num = int(input('Digite um numero valido diferente de 0: '))

while (num != -888888) and (qtd < maximo):
    qtd += 1
    if (num < 0):
        neg += 1
        if (maiorNeg < num):
            maiorNeg = num 
        if (num < -9) and (num > -100):
            pos2d[qtd2d] = num
            somaNeg += num
            qtd2d += 1
    elif (num > 9) and (num < 99):
        pos2d[qtd2d] = num
        qtd2d += 1

    num = int(input("Digite outro numero, -888888 p/parar: "))

if (qtd2d == 0):
    print('Não foi digitado um numero de 2 digitios!')
else:
    # print('Positivos de 4 dígitos: ', end='')
    for i in range(qtd2d):
        if pos2d[i] > 0:
            print(pos2d[i])
    for i in range(qtd2d -1, -1, -1):
        if pos2d[i] < 0:
            print(pos2d[i])

if (somaNeg == 0):
    print("Não foi digitado um numero negativo!")
else:
    print("A quantidade de numeros negativos é igual a: ",neg)
    print("A soma dos numeros negativos é igual a: ",somaNeg)
    print("A quantidade de numeros lidos e igual a: ",qtd)

# chat

qtd = 0
num3dig = []
somaPositivos = 0
menorPositivo = 999999999999
num = int(input("Digite um número inteiro (-999999 para parar): "))
while num != -999999 and qtd < 250:
    qtd += 1
    if (abs(num) > 99) and (abs(num) < 1000):
        num3dig.append(num)
        if num > 0:
            somaPositivos += num
            if num < menorPositivo:
                menorPositivo = num
    num = int(input("Digite outro número inteiro (-999999 para parar): "))

print("Quantidade total de números lidos:", qtd)

negativos = [x for x in num3dig if x < 0]
positivos = [x for x in num3dig if x > 0]
print("Números de 3 dígitos significativos:")
print("Negativos:", negativos)
print("Positivos:", positivos)

print("Soma dos números positivos de 3 dígitos:", somaPositivos)

if menorPositivo == 999999999999:
    print("Nenhum número positivo foi lido.")
else:
    print("O menor número positivo é", menorPositivo)

"""
### Questão 3

Faça um programa Python para ler uma sequência de números inteiros - a leitura para quando o número -1 for lido. No entanto, o usuário só deve digitar no máximo 200 números válidos. O programa deve imprimir as seguintes informações como resultado:

  * A quantidade total de números positivos lidos.
  * Os números negativos lidos cujos valores tiverem 3 dígitos significativos. A impressão destes números deve mostrar primeiro os números menores que -500, na mesma ordem relativa em que foram lidos, e depois os maiores ou iguais a -500, na ordem inversa da que foram lidos.
  * A média dos números negativos de 3 dígitos impressos no item anterior.
  * O maior número positivo lido.

  OBS1: Não pode usar as funções/métodos len, min, max, sum, nem sort.
"""

qtd = 0
negativos = 0
positivos4dig = []
somaPositivos4dig = 0
qtdPositivos4dig = 0
menorNegativo = -999999999999
num = int(input("Digite um número inteiro (0 para parar): "))
while num != 0 and qtd < 150:
    qtd += 1
    if num < 0:
        negativos += 1
        if num < menorNegativo:
            menorNegativo = num
    elif 999 < num < 10000:
        positivos4dig.append(num)
        somaPositivos4dig += num
        qtdPositivos4dig += 1
    num = int(input("Digite outro número inteiro (0 para parar): "))

print("Quantidade total de números negativos lidos:", negativos)

menores5100 = [x for x in positivos4dig if x < 5100]
maioresOuIguais5100 = [x for x in positivos4dig if x >= 5100]

print("Números positivos de 4 dígitos significativos:")
print("Menores que 5100:", menores5100)
print("Maiores ou iguais a 5100:", maioresOuIguais5100[::-1])  # Imprimir em ordem inversa

if qtdPositivos4dig > 0:
    mediaPositivos4dig = somaPositivos4dig / qtdPositivos4dig
    print("Média dos números positivos de 4 dígitos:", round(mediaPositivos4dig, 4))
else:
    print("Nenhum número positivo de 4 dígitos foi lido.")

if menorNegativo == 999999999999:
    print("Nenhum número negativo foi lido.")
else:
    print("O menor número negativo é", menorNegativo)

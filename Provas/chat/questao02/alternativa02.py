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
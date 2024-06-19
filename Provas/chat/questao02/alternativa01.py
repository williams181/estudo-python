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
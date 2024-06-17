"""
Faça um programa Python para ler uma sequencia de números inteiros negativos - a leitura para quando o número zero for lido.
No entanto, o usuário só deve poder digitar no maximo 150 números negativos. O programa deve imprirmir as seguintes informações
como resultado (nesta ordem):
  * Os números lidos cujos valores tem 2 dígitos significativos e também são múltiplos de 5.
    A impressão destes números deve ser feita na ordem inversa da que foram lidos.
  * O maior número lido que não seja múltiplo de 7.
"""

qtd = 0
qtd5 = 0
mult5 = [0] * 7
maiorNaoMult7 = -999999999999
num = int(input("Digite um número negativo: "))

while num >= 0:
    num = int(input("Digite pelo menos um número negativo: "))

while num != 0 and qtd < 150:
    qtd += 1
    if (num % 5 == 0) and (num > -100) and (num < -9):
        mult5[qtd5] = num
        qtd5 += 1
    if (num % 7 != 0) and (num > maiorNaoMult7):
        maiorNaoMult7 = num
    num = int(input("Digite outro número negativo, 0 p/parar: "))
    while num > 0:
        num = int(input("Digite um número negativo, 0 p/parar: "))

if qtd == 150:
    print("Quant. máxima de números atingida, último número foi descartado!")

if qtd5 == 0:
    print("Nenhum múltiplo de 5 com 2 dígitos foi digitado.")
else:
    mult5 = mult5[:qtd5]
    mult5_inverso = mult5[::-1]
    print("Múltiplos de 5 com 2 dígitos significativos:", mult5_inverso)

if maiorNaoMult7 == -999999999999:
    print("Nenhum não múltiplo de 7 foi digitado.")
else:
    print("O maior não múltiplo de 7 é", maiorNaoMult7)




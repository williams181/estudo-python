"""
Faça um programa Python para ler uma sequencia de números inteiros negativos - a leitura para quando o número zero for lido.
No entanto, o usuário só deve poder digitar no maximo 150 números negativos. O programa deve imprirmir as seguintes informações
como resultado (nesta ordem):
  * Os números lidos cujos valores tem 2 dígitos significativos e também são múltiplos de 5.
    A impressão destes números deve ser feita na ordem inversa da que foram lidos.
  * O maior número lido que não seja múltiplo de 7.
"""

maximo = 150
pos2dMult5 = [0] * 150
qtd = qtd5 = 0
maiorNaoMult7 = -999999999
lista_inverso = []

num = int(input("Difite um numero para iniciar: "))

while num >= 0:
    num = int(input("Digite pelo menos um número negativo: "))

while (num != 0) and (qtd < 150):
    qtd += 1
    if (num < -9) and (num > -100):
        if (num % 5 == 0):
            pos2dMult5[qtd5] = num
            qtd5 += 1
        if (num % 7 != 0) and (num > maiorNaoMult7):
            maiorNaoMult7 = num
    num = int(input("Digite outro número negativo, 0 p/parar: "))
    while num > 0:
        num = int(input("Digite um número negativo, 0 p/parar: "))

if qtd5 == 0:
    print("Sem múltiplo de 5 com 2 digitos foi digitado.")
else:
    for i in range(qtd5 -1, -1, -1):
        print(pos2dMult5[i]) 

if maiorNaoMult7 == -999999999:
    print("Sem numeros não multiplos de 7.")
else:
    print("o maior não multiplo de 7 é: ",maiorNaoMult7)

        


"""
### Questão 1

Faça um programa Python para ler uma sequência de números inteiros - a leitura para quando o número -1 for lido. No entanto, o usuário só deve poder digitar no máximo 200 números inteiros. O programa deve imprimir as seguintes informações como resultado (nesta ordem):

  * Os números lidos cujos valores têm 2 dígitos significativos e também são múltiplos de 3.
    A impressão destes números deve ser feita na ordem inversa da que foram lidos.
  * O maior número lido que não seja múltiplo de 4.

"""

maximo = 200
pos2d = [0] * maximo
maiorNaoMult4 = -999999999999
pos = maiorPos = qtd = qtd2 = 0

num = int(input("Digite um número inteiro para começar: "))

while num == 0:
    num = int(input("Digite um número inteiro (-1  p/parar): "))
    
while (num != -1) and (qtd < maximo):
    qtd = qtd + 1
    if (num > 1):
        pos = pos + 1
        if (num <= 99) and (num >= 10):
            pos2d[qtd2] = num
            qtd2 += 1
        if (num % 4 != 0) and (maiorNaoMult4 < num):
            maiorNaoMult4 = num
    num = int(input("Digite outro numero, (-1 p/parar): "))
            
if (qtd2 == 0):
    print('Não foi digitado um numero de 2 digitios!')
else:
    for i in range(qtd2 - 1, -1, 1):
        print(pos2d[i])

if (maiorNaoMult4 == -999999999999):
    print("Não foi digitado um numero não multiplo de 4.") 
else:
    print("o maior numero não multiplo de 4 foi: ",maiorNaoMult4)
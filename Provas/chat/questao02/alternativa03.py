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

"""
Faça um programa Python para ler uma sequencia de números inteiros - a leitura para quando o número zero (0) for lido. No entanto, o usuário
só deve digitar no maximo 400 números válidos. O prgrama deve imprimir as seguintes informações como resultado:
  * A quantidade total de números negativos lidos. #
  * A quantidade total de números positivos lidos.#
  * Os númeors positivos lidos cujos valores tiverem 5 dígitos significativos e também são múltiplos de 5. A impressão destes números deve mostrar primeiro os números
    menores que 30000, na mesma ordem relativa em que foram lidos, e depois os maiores ou iguais a 30000, na ordem inversa da que foram lidos.
  * A média dos números negativos de 5 dígitos impressos no item anterior. #
  * A média dos números positivos de 5 dígitos impressos no item anterior. #
  * O menor número negativo lido. *
  * O maior número positivo lido. *
  OBS1: Não pode usar as funções/métodos len, min, max, sum, nem sort.
"""

maximo = 400
pos5Mul5 = [0] * maximo
qtd = qtd5Neg = neg = pos = menorNeg = qtdPos = qtdNeg = medNeg = maiorPos = medPos = resultMed = 0

num = int(input("Digite um numero para iniciar: "))
    
while (num != 0) and (qtd < 400):
    qtd +=1
    if (num > 0):
        qtdPos += 1
        if (num > 9999) and (num < 100000) and (num % 5 == 0):
            pos5Mul5[pos] = num
            pos += 1
            medPos += num
        if (maiorPos < num):
            maiorPos = num
    elif (num < 0):
        neg += 1
        if (num >-100000) and (num < -9999):
            pos5Mul5[qtd5Neg] = num
            qtd5Neg += 1
            medNeg += num
        if (menorNeg > num):
            menorNeg = num
    num = int(input("Digite outr número negativo ou positivo (0 p/parar):"))

if (pos == 0) or (qtd5Neg == 0):
    print("Não foi digitado numeros de 5 digitos.")
else:
    for i in range(pos):
        if (pos5Mul5[i] > 30000):
            print("positivos: ",pos5Mul5[i])
            
    for i in range(pos - 1, -1, -1):
        if (pos5Mul5[i] >= 10000 and pos5Mul5[i] < 30000):
            print("positivos: ",pos5Mul5[i])
        
print("total de numeros positivos lidos: ",qtdPos)
print("total de numeros negativos lidos: ", neg)
print("o menor numero negativo lido: ", menorNeg)
print("o maior numero positivo: ", maiorPos)
print("a media dos numeros positivos de 5 digitos é: ",medPos/pos)
print("a media dos numeros negativos de 5 digitos é: ", medNeg/qtd5Neg)
            
    

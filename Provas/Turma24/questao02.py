"""
Faça um programa Python para ler uma sequencia de números inteiros - a leitura para quando o número -999999 for lido. No entanto, o
usuário só deve poder digitar no máximo 250 números. O programa deve imprimir as seguintes informações como resultado:
    * A quantidade total de números lidos.
    * Os números lidos cujo os valores tiverem 3 dígitos significativos. A impressão destes números devem mostrar primeiro os números
    negativos (de 3 dígitos), na mesma ordem relativa em que foram lidos, e depois os positivos (idem).
    * A soma dos números positivos de 3 dígitos impressos no item anterior.
    * O menor número positivo lido.
"""

maximo = 250 
pos3d = [0] * maximo
qtd = neg = menorPos = qtd3d = somaPos = 0

num = int(input("Digite um numero para inicializar: "))
while (num == 0):
    num = int(input("O numero deve ser valido e diferente de 0: "))

while (num != -999999) and (qtd < maximo):
    qtd += 1
    if (num < 0):
        if (num < -99) and (num > -1000):
            pos3d[qtd3d] = num
            qtd3d += 1
    elif (num > 99) and (num < 1000):
        pos3d[qtd3d] = num
        qtd3d += 1
        somaPos += num
    menorPos = num
    if (menorPos > num):
        menorPos = num

    num = int(input("Digite outro numero, sendo -999999 p/parar: "))

if (qtd3d == 0):
    print("não teve a ocorrencia de um nunero de 3 digitios!")
else:
    # print("Numeros de 3 digitos significativos: ", end='')
    for i in range(qtd3d):
        if pos3d[i] > 0:
            print(pos3d[i])
    # print("Numeros de 3 digitos significativos: ", end='')
    for i in range(qtd3d):
        if pos3d[i] < 0:
            print(pos3d[i])

if (somaPos == 0):
    print("Nenhum numero positivo de 3 digitos foi recebibo!")
else: 
    print("A soma dos numeros positivos é: ",somaPos)
    print("A quantidade de numeros lidos é: ", qtd)
    print("O menor numero positivo lido é: ",menorPos)

        
    


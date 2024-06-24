"""
Faça um programa Python para ler uma sequencia de números inteiros - a leitura para quando o número -999999 for lido. No entanto, o
usuário só deve poder digitar no máximo 250 números. O programa deve imprimir as seguintes informações como resultado:
    * A quantidade total de números lidos. *
    * Os números lidos cujo os valores tiverem 3 dígitos significativos. A impressão destes números devem mostrar primeiro os números
    negativos (de 3 dígitos), na mesma ordem relativa em que foram lidos, e depois os positivos (idem).
    * A soma dos números positivos de 3 dígitos impressos no item anterior.
    * O menor número positivo lido.
"""

qtd = soma3d = qtd3 = qtdNeg = 0
menorPos = 9999999999999999
maximo = 5
pos3d = [0] * maximo

num = int(input("Digite um numero para começar: "))

while num == 0:
    num = int("Digite um numero diferente de 0: ")
    
while (num != -999999) and (qtd < maximo):
    qtd = qtd + 1
    if ((num > 99) and (num < 1000)) or ((num < -99) and (num > -1000)): # usar a propriedade or caso precise colocar numeros negativos e positivos com digitos siginificativos iguais
        pos3d[qtd3] = num
        qtd3 = qtd3 + 1
    if (num > 99) and (num < 1000):
        soma3d = soma3d + num
        if (menorPos > num): 
            menorPos = num

    num = int(input("Digite outro número negativo, 0 p/parar: "))
        
if qtd == 250:
    print("Quant. máxima de números atingida, último número foi descartado!")

if qtd3 == 0:
    print("Lista não foi percorrida.")
else:
    for i in range(qtd3):
        if pos3d[i] < 0:
            print(pos3d[i])    
    for i in range(qtd3):
        if pos3d[i] > 0:
            print(pos3d[i])    
            
print("A soma dos numeros positivos de 3 digitos é: ", soma3d)
print("o menor possitivo é: ",menorPos)
        
 
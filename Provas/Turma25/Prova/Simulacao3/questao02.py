maximo = 150
pos2d = [0] * maximo
qtd = qtdNeg = 0
maiorMult7 = -999999999

num = int(input("Digite um numero para iniciar: "))

while num > 0:
	num = int(input("Digite um numero negativo: "))
	
while (num < 0) and (qtd < maximo):
	qtd += 1
	if (num > -100) and (num < -9):
		pos2d[qtdNeg] = num
		qtdNeg += 1
	if (num % 7 != 0) and (num > maiorMult7):
		maiorMult7 = num
	num = int(input("Digite um numero negativo (0 p/parar): "))

if qtdNeg == 0:
	print("Não foram digitados numeros negativos com 2 digitos significativos.")
else:
	for i in range(qtdNeg):
		print(pos2d[i])

if maiorMult7 == -999999999:
	print("Não foram digitados numeros não multiplos de 7.")
else:
	print("o maior numero lido que não e multiplo de 7 é: ",maiorMult7)
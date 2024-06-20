def serie(n):
	nu1 = 3
	nu2 = -5
	de = 1
	res = 0.0
	for i in range(2, n + 2):
		if (i % 2 == 0):
			res = res + nu1 / de
			nu1 = nu1 * 5
		else:
			res = res + nu2 / de
			nu2 = nu2 * 6
		de = de  * i
		print(f"{nu1}/{i}")
	return res

n = int(input("Digite o numero de termos (n < 1 p/parar): "))
while n > 0:
	resultado = serie(n)
	n = int(input("Digite o numero de termos (n < 1 p/parar): "))

print("O valor da serie é: ",resultado)
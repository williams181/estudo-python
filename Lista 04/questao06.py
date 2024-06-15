"""
Fazer subrotinas recursivas para calcular o valor das seguintes séries - com n termos, onde n deve ser parametro recebido na chamada:
    a. S = 2/500 - 5/490 + 2/480 - 5/470 + ...
    b. S = 37*38/1 + 36*37/2 + 35*36/3 + ...
"""
# a. S = 2/500 - 5/490 + 2/480 - 5/470 + ...
def calcular_serie_a(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        termo = 2 / (500 - (n-1)*10)
    else:
        termo = -5 / (500 - (n-1)*10)
    return termo + calcular_serie_a(n - 1)
n = int(input("Digite o número de termos da série: "))
resultado = calcular_serie_a(n)
print("O valor da série é:", resultado)

# b. S = 37*38/1 + 36*37/2 + 35*36/3 + ...
def calcular_serie_b(n):
    if n == 1:
        return 37 * 38
    else:
        termo = (n-1) * n / n
        return termo + calcular_serie_b(n - 1)
n = int(input("Digite o número de termos da série: "))
resultado = calcular_serie_b(n)
print("O valor da série é:", resultado)
"""
Calcular a média aritmética de vários números reais fornecidos pelo usuário. A leitura dos números deve parar quando um
número negativos for lido.
"""

qtdNum = 0
soma = 0.0
condicao = True

while (condicao):
    n = int(input("Numero: "))
    if ( n >= 0): 
        qtdNum = qtdNum + 1
        soma = soma + n
    else:
        condicao = False
print("a media aritimetica dos numeros informados é",soma/qtdNum)
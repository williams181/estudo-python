"""
Construir uma tabela de conversão de graus Fahrenheit para Celsius, para todos os Fahrenheit em um intervalo informado pelo usuário.
Obs: C = (F - 32) * 5/9
"""

li = int(input('Digite o 1º valor do intervalo:'))
ls = int(input('Digite o 2º valor do intervalo:'))

if li > ls:
    aux = li
    li = ls
    ls = aux

print('Tabela de Conversão\nCelsius\t|\tFahrenheit')
for it in range(li, ls+1):
    print(it, '\t\t|', (it-32)*5/9)
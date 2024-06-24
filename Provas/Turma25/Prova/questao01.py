"""
Faça uma função Python para calcular a soma dos N primeiros termos da série abaixo. O valor de N deve ser um parametro e a função
deve retornar zero como resultado caso o número de termos não seja positivo.

  S = 10/1 - 15/5 + 20/8 - 25/11 + 30/15 - 35/17 + ...

Escrever também um programa principal para perguntar ao usuário a quantidade de vezes (qtd) que ele deseja calcular o valor da série
e, em seguida, os números de termos desejados nestas qtd vezes. Para cada um deles, seu programa deve usar a função e imprimir o
resultado da série (com 4 casas decimais), da seguinte forma: "O valor da série com ... termos é ...".
"""

def serie(n):
    num = 10
    den1 = 1
    den2 = 5
    soma = 0.0
    for i in range(n):
        if i % 2 == 0:
            soma = soma + num / den1
            den1 = den1 + 7
        else:
            soma = soma - num / den2
            den2 = den2 + 6
        num = num + 5
    return soma

qtd = int(input('Quantidade de cálculos: '))
while qtd < 1:
    qtd = int(input('Inválida. Quantidade de cálculos: '))

for j in range(qtd):
    termos = int(input('Quantidade de termos: '))
    while termos < 1:
        termos = int(input('Inválido. Quantidade de termos: '))
    res = serie(termos)
    print('O valor da série com %d termos é %.4f' % (termos, res))

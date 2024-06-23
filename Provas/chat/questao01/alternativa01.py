"""
### Questão 1

Faça uma subrotina Python do tipo função para calcular a soma dos N primeiros termos da série abaixo, onde o valor de N é um parâmetro e o resultado do cálculo da série é o resultado da função. Observe que o símbolo "!" se refere ao fatorial do número.

S = 4 - 7/3! + 16/5! - 35/7! + 68/9! - 121/11! + ...

OBS - Inclua também um programa principal para ler vários valores de N e testar a sua função: a execução deve parar com um número de termos inválido (<1).
"""

import math

def serie(n):
    nu1 = 4
    nu2 = -7
    de = 1
    res = 0.0
    for i in range(2, n + 2):
        if i % 2 == 0:
            res = res + nu1 / de
            nu1 = nu1 * 5
        else:
            res = res + nu2 / de
            nu2 = nu2 * 6
        de = de * i
    return res

n = int(input('Digite número de termos (<1 para parar): '))
while n > 0:
    r1 = serie(n)
    print(r1)
    n = int(input('Digite número de termos (<1 para parar): '))
    
    
def serie(n):
    nu1 = 5
    nu2 = -10
    de = 2
    res = 0.0
    for i in range(1, n + 1):
        if i % 2 != 0:
            res += nu1 / de
            nu1 += 5
        else:
            res += nu2 / de
            nu2 -= 5
        de += 2
    return res

n = int(input('Digite número de termos (<1 para parar): '))
while n > 0:
    r1 = serie(n)
    print(r1)
    n = int(input('Digite número de termos (<1 para parar): '))

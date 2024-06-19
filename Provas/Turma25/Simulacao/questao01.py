"""
Faça uma subrotina Python do tipo função para calcular a soma dos N primeiros termos da série abaixo, onde o valor de N é um parametro e
o resultado do cálculo da série é o resultado da função. Observe que o símbolo "!" se refere ao fatorial do número.

S = 3 - 5/2! + 15/3! - 30/4! + 75/5! - 180/6! + ...

OBS - Inclua também um programa principal para ler vários valores de N e testar a sua função: a execução deve para com um número de
termos inválido (<1).
"""

def serie(n):
    nu1 = 3
    nu2 = -5
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
        print(f"{nu1}/{i}")
    return res

n = int(input('Digite número de termos(<1 p/parar): '))
while n > 0:
    r1 = round(serie(n), 5)
    print(n, r1)
    n = int(input('Digite número de termos(<1 p/parar): '))

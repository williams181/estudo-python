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
    for i in range(3, n + 4, 2):
        res += nu1 / math.factorial(de) if de % 2 == 1 else nu2 / math.factorial(de)
        nu1 = nu1 * 2 + 1
        nu2 = nu2 * 2 - 1
        de += 2
    return res

n = int(input('Digite número de termos (<1 para parar): '))
while n > 0:
    r1 = round(serie(n), 5)
    print(n, r1)
    n = int(input('Digite número de termos (<1 para parar): '))

"""
### Questão 2

Faça uma subrotina Python do tipo função para calcular a soma dos N primeiros termos da série abaixo, onde o valor de N é um parâmetro e o resultado do cálculo da série é o resultado da função.

S = 1 - 9/4 + 10/2 - 21/8 + 32/5 - 49/12 + 100/7 + ...

Escrever também um programa principal para perguntar ao usuário a quantidade de vezes (qtd) que ele deseja calcular o valor da série e, em seguida, os números de termos desejados nestas qtd vezes. Para cada um deles, seu programa deve usar a função e imprimir o resultado da série (com 4 casas decimais), da seguinte forma: "O valor da série com ... termos é ...".

"""

def serie(n):
    nu1 = 1
    nu2 = -9
    de = 1
    res = 0.0
    for i in range(1, n + 1):
        if i % 2 != 0:
            res += nu1 / de
            nu1 = nu1 * 3 + 1
        else:
            res += nu2 / de
            nu2 = nu2 * 2 - 1
        de += 2
    return res

qtd = int(input('Digite a quantidade de vezes que deseja calcular a série: '))
for _ in range(qtd):
    n = int(input('Digite o número de termos: '))
    resultado = round(serie(n), 4)
    print(f'O valor da série com {n} termos é {resultado}')

"""
### Questão 3

Faça uma função Python para calcular a soma dos N primeiros termos da série abaixo. O valor de N deve ser um parâmetro e a função deve retornar zero como resultado caso o número de termos não seja positivo.

  S = 5/2 - 10/4 + 15/6 - 20/8 + 25/10 - 30/12 + ...

Escrever também um programa principal para perguntar ao usuário a quantidade de vezes (qtd) que ele deseja calcular o valor da série e, em seguida, os números de termos desejados nestas qtd vezes. Para cada um deles, seu programa deve usar a função e imprimir o resultado da série (com 4 casas decimais), da seguinte forma: "O valor da série com ... termos é ..."
"""

def serie(n):
    if n <= 0:
        return 0
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

qtd = int(input('Digite a quantidade de vezes que deseja calcular a série: '))
for _ in range(qtd):
    n = int(input('Digite o número de termos: '))
    resultado = round(serie(n), 4)
    print(f'O valor da série com {n} termos é {resultado}')

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

n = int(input('Digite número de termos (<1 para parar): '))
while n > 0:
    r1 = serie(n)
    print(r1)
    n = int(input('Digite número de termos (<1 para parar): '))

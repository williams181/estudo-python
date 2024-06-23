"""
### Questão 3

Faça uma função Python para calcular a soma dos N primeiros termos da série abaixo. O valor de N deve ser um parâmetro e a função deve retornar zero como resultado caso o número de termos não seja positivo.

  S = 5/2 - 10/4 + 15/6 - 20/8 + 25/10 - 30/12 + ...

Escrever também um programa principal para perguntar ao usuário a quantidade de vezes (qtd) que ele deseja calcular o valor da série e, em seguida, os números de termos desejados nestas qtd vezes. Para cada um deles, seu programa deve usar a função e imprimir o resultado da série (com 4 casas decimais), da seguinte forma: "O valor da série com ... termos é ..."
"""

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

n = int(input("Digite número de termos (menor 1 um p/parar): "))

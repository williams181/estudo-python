"""
Faça uma subrotina Python do tipo função para calcular a soma dos N primeiros termos da série abaixo, onde o valor de N é um parametro
e o resultado do cálculo da série é o resultado da função.

S = 2 - 7/5 + 8/3 - 13/10 + 32/9 - 19/15 + 128/27 + ...

Escrever também um programa principal para perguntar ao usuário a quantidade de vezes (qtd) que ele deseja calcular o valor da série e,
em seguida, os números de termos desejados nestas qtd vezes. Para cada um deles, seu programa deve usar a função e imprimir o resultado
da série (com 4 casas decimais), da seguinte forma: "O valor da série com ... termos é ...".

"""

def serie(n):
    soma = 0
    n1 = 2
    d1 = 1
    n2 = 7
    d2 = 5
    for i in range(n):
        if (i % 2 != 0):
            soma = soma - (n2/d2)
            n2 = n2 + 6
            d2 = d2 + 5
            print(f"{n2}/{d2}")
        else:
            soma = soma + (n1/d1)
            n1 = n1 * 4
            d1 = d1 * 3
            print(f"{n1}/{d1}")
    return soma
qtd = int(input('Digite a quantidade de vezes que deseja calcular o valor da série: '))
termo = int(input('Quantidade de termos desejados: '))
while (qtd > 0):
    resultado = serie(termo)
    print('O valor da série com %d termos é %.4f' % (termo, resultado))
    termo = int(input('Quantidade de termos desejados'))
    qtd -= 1
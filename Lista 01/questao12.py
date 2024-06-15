"""
O máximo divisor comum (MDC) de 2 números inteiros positivos é o maior número inteiro que divide ambos sem deixar resto. Seu programa
deve ler 2 números inteiros positivos e determinar o MDC destes 2 números. Obs: Não utulizar nenhuma fórmula ou estraégia matemática para
calcular o MDC - coloque o programa para trabalhar para voce...
"""

num1 = int(input( 'Digite o primeiro número'))
num2 = int(input( 'Digite o segundo número'))

mdc = num1
if num2 < mdc:
    mdc = num2
while (num1 % mdc !=0) or (num2 % mdc !=0):
    mdc= mdc - 1

print('O MDC entre é:', num1, num2 , mdc)
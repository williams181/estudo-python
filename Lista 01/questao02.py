"""
Ler 2 números inteiros e calcular o resto da divisão do primeiro pelo segundo. Se o resto for zero, imprimir o primeiro número,
senão imprimir o quadrado do resto. Existe uma situação que pode causar problemas: pense se seu programa está preparado para lidar com isso.
"""

n1 = int(input("numero1: "))
n2 = int(input("numero2: "))

result = n1 % n2
resultQuad = result * result

if result == 0:
    print("result",n1)
else:
    print("result", resultQuad)


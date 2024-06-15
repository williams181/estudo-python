"""
Ler 3 números e imprimir o menor deles. Sua solução é facilmente escalável para uma grande quantidade de números?
"""

n1 = int(input("numero1: "))
n2 = int(input("numero2: "))
n3 = int(input("numero3: "))

if (n1 < n2 and n1 < n3):
    print("result", n1)
elif (n2 < n1 and n2 < n3):
    print("result", n2)
else:
    print("result", n3)

n1 = int(input("n1: "))
n2 = int(input("n1: "))
n3 = int(input("n1: "))
men = 99999999999
if n2 < men:
    men = n2
if n3 < men:
    men = n3
print('result',men)
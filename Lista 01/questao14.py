"""
Ler um número inteiro positivo e dizer se ele é primo ou não.
"""

Num1 = int(input('Digite algum número : '))

QtdDiv = 0 

for i in range(1,Num1+1):
    if(Num1 % i ==0):
        print(Num1, QtdDiv,i)
        QtdDiv= QtdDiv +1

if (QtdDiv ==2):
    print('É primo', Num1)
else:
    print(Num1, 'Não é primo')
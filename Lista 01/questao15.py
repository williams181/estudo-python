"""
Ler um número inteiro positivo e dizer se ele é perfeito ou não. OBS: um número é perfeito se ele é igual a soma de todos os seus divisores
(exceto ele mesmo).
"""

num1 = int(input('Digite um número'))

div = 0

for i in range(1, num1):
    if( num1 % i ==0):
        div = div +i

if(div == num1):
    print('É perfeito')

else:
    print('Não é perfeito')
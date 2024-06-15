"""
Construir uma tabela de conversão de graus Fahrenheit para Celsius, para todos os Fahrenheit em um intervalo informado pelo usuário.
Obs: C = (F - 32) * 5/9
"""

Temp01 = int(input('Digite o primeiro valor'))
Temp02 = int(input('Digite o segundo valor'))

if (Temp01 > Temp02):
        Temp01, Temp02 = Temp02, Temp01

for i in range(Temp01,Temp02+1):

    
    print(i,'Temperatura', (i-32)* 5/9) 
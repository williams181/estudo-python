"""
Ler um número inteiro positivo N digitado pelo usuário e depois ler N números inteiros positivos (0 < x < 4000) e, para cada um deles,
imprimir a sua representação em algarismos romanos. OBS. Lembre que os valores dos algarismos romanos são: I=10, V=5, L=50, C=100, D=500,
e M=1000, e que IV=4, IX=9, XL=40, XC=90, CD=400 e CM=900.
"""

nipQtd = int(input('Digite um número inteiro positivo:'))
while nipQtd < 1:
    nipQtd = int(input('Número inválido!\nTente novamente!\nDigite um número inteiro positivo:'))
rom = ''
it = 1
while it <= nipQtd:
    nip = int(input('Digite um número inteiro positivo (> 0 e < 4000):'))
    while nip < 1 or nip > 3999:
        nip = int(input('Número inválido!\nTente novamente!\nDigite um número inteiro positivo (> 0 e < 4000):'))
    num = nip # 
    if nip >= 1000:
        rom = rom + 'M'
        nip = nip - 1000
    if nip >= 900:
        rom = rom + 'CM'
        nip = nip - 900
    if nip >= 500:
        rom = rom + 'D'
        if (nip - 500) >= 300:
            rom = rom + 'CCC'
            nip = nip - 800
        elif (nip - 500) >= 200:
            rom = rom + 'CC'
            nip = nip - 700
        elif (nip - 500) >= 100:
            rom = rom + 'C'
            nip = nip - 600
        else:
            nip = nip - 500
    if nip >= 400:
        rom = rom + 'CD'
        nip = nip - 400
    if nip >= 100:
        rom = rom + 'C'
        if nip >= 300:
            rom = rom + 'CC'
            nip = nip - 300
        elif nip >= 200:
            rom = rom + 'C'
            nip = nip - 200
        else:
            nip = nip - 100
    if nip >= 90:
        rom = rom + 'XC'
        nip = nip - 90
    if nip >= 50:
        rom = rom + 'L'
        if nip >= 80:
            rom = rom + 'XXX'
            nip = nip - 80
        elif nip >= 70:
            rom = rom + 'XX'
            nip = nip - 70
        elif nip >= 60:
            rom = rom + 'X'
            nip = nip - 60
        else:
            nip = nip - 50
    if nip >= 40:
        rom = rom + 'XL'
        nip = nip - 40
    if nip >= 10:
        rom = rom + 'X'
        if nip >= 30:
            rom = rom + 'XX'
            nip = nip - 30
        elif nip >= 20:
            rom = rom + 'X'
            nip = nip - 20
        else:
            nip = nip - 10
    if nip == 9:
        rom = rom + 'IX'
        nip = nip - 9
    if nip >= 5:
        rom = rom + 'V'
        if nip == 8:
            rom = rom + 'III'
            nip = nip - 8
        elif nip == 7:
            rom = rom + 'II'
            nip = nip - 7
        elif nip == 6:
            rom = rom + 'I'
            nip = nip - 6
        else:
            nip = nip - 5
    if nip == 4:
        rom = rom + 'IV'
        nip = nip - 4
    elif nip == 3:
        rom = rom + 'III'
        nip = nip - 3
    elif nip == 2:
        rom = rom + 'II'
        nip = nip - 2
    elif nip == 1:
        rom = rom + 'I'
        nip = nip - 1
    print('O número', num, 'em algarismos romanos é', rom)
    rom = ''
    it = it + 1
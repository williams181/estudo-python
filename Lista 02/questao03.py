
#Metodo do corno

s1 = input('Busca')
s2 = input('Texto')

contador = 0 

res = s2.find(s1)

while res != -1:
    contador = contador +1
    res = s2.find (s1, res+1)

print('Res = ', contador)
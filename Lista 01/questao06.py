"""
Calcular o valor de S com N termos, onde N é informado pelo usuário e:
  a. S = 1 + 3/2 + 5/3 + 7/4 + ...
  b. S = 2/500 - 5/490 + 2/480 - 5/470 + ...
  c. S = 37*38/1 + 36*57/2 + 35*36/3 + ...
"""
# a. S = 1 + 3/2 + 5/3 + 7/4 + ...
n = int(input('Digite o número de termos:'))
s = 0.0 
nu = 1  
it = 1
while (it <= n):
    s = s + nu / it  
    nu = nu + 2 
    it = it + 1
print('A soma dos', n, 'termos da sequência 6.a. é', s)
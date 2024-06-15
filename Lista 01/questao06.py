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
de = 1
for it in range(1,n+1):
    print(f"{nu}/{it}")
    s = s + nu/it 
    nu = nu + 2 
print('A soma dos',n,'termos da sequência 6.a. é',s)

# b. S = 2/500 - 5/490 + 2/480 - 5/470 + ..

n = int(input('Digite o número de termos:'))
s = 0.0
de = 500
nu = 2 
for it in range(1, n+1):
    if de != 0: 
        if nu == 2: 
            s = s + nu/de
            nu = 5
        else: 
            s = s - nu/de 
            nu = 2
        de = de - 10 
    else:
        print('A variável',de,'atingiu o valor nulo e a divisão por 0 é impossível.')
print('A soma dos', n, 'termos da sequência 6.b. é', s)

# c. S = 3738/1 + 3657/2 + 35*36/3 + ...

n = int(input('Digite o número de termos:'))
s = 0.0
n1 = 37
d1 = 1
for it in range(1, n+1):
    s = s + n1*(n1+1)/d1
    n1 = n1 - 1
    d1 = d1 + 1
print('A soma dos',n,'termos da sequência 6.c. é',s)
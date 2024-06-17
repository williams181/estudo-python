"""
Ler uma tabela de pessoas onde:
    leitura
    * Cada pessoa tem um código (inteiro), um nome (String) e um salário (float).
    * A leitura da tabela para com um código que não seja positivo.

    busca
    * Depois o usuário informará um valor máximo de salário. Caso o valor máximo não seja positivo, o programa deve informar o erro ao
    * usuário e pedir os dados novamente.
    * O programa deve imprimir os dados das pessoas cujos salários sejam menores ou iguais ao valor máximo informado, seguidos pelo número
      de pessoas correspondentes, e pela média dos salários destas pessoas.

    (codigo,nome,salario)
    condição de parada <0 

    programa 


    leitura:

     variavel = entrada(input)

     while variavel >= 0:
           
         variavel = entrada(input)


    busca 
      

    
"""
#LEITURA
n = int(input("Digite o tamanho da tabela de pessoas: "))
while (n < 1):
    n = int(input("Tamanho deve ser inteiro e positivo. Tente novamente: "))

tab = [None]*n

for i in range(n):
    codP = int(input("Digite um codigo da pessoa: "))
    while (codP < 1):
         codP = int(input("Código deve ser inteiro positivo. Tente novamente: "))
    nomeC = input("Digite o nome da pessoa: %d:\n" % (codP))
    salario = float(input("Digite um salario: %s:\n" % (nomeC)))
    tab[i]=(codP,nomeC,salario)

#BUSCA
salarioMaximo = float(input("Digite o salario maximo: "))
while (salarioMaximo < 0):
    salarioMaximo = float(input("Salario invalido: "))

index = 0
while index<n: 
        
    if (tab[index][2] <= salarioMaximo):
        codP = tab[index][0]
        nomeC = tab[index][1]
        salario = tab[index][2]
        #codP, nomeC, salario = tab[index]        
        print('%d | %s | %f.' % (codP,nomeC,salario))
    
    index = index +1 


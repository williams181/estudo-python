"""
Ler uma tabela com Cursos, onde:
    * Cada curso é formado por um código (inteiro positivo), um nome (String), e o centro a que pertence (inteiro positivo).
    * A leitura da tabela de cursos para com o código de curso zero.
    * Depois o usuário fornecerá uma lista de códigos de centro para que o programa imprima o código e nome de todos os cursos associados
    a cada centro digitado.
    * Se o código do centro não existir na tabela, mostrar a mensagem "Nenhum curso encontrado" e continuar.
    * O programa para com a digitação e um código de centro inválido (negativo ou zero).
"""

n = int(input("Digite o tamanho da tebala de cursos: "))
while (n < 1):
    n = int(input("Tamanho deve ser inteiro e positivo. Tente novamente: "))

tab = [None]*n

for i in range(n):
    codC = int(input("Digite o código de um curso: "))
    while (codC < 1):
        codC = int(input("Código deve ser inteiro positivo. Tente novamente: "))
    nomeC = input("Digite o nome do curso: %d:\n" % (codC))
    centro = int(input("Digite o centro a qual pertence: %d:\n" % (codC)))
    tab[i] = (codC, nomeC, centro)
    print('Tabela com %d cursos foi lida corretamente.' % (n))
    print('Tabela ->', tab)



busca = int(input('Digite o codigo do curso para busca (<=0 para parar): '))

while (busca > 0):
        i = 0
        while (i < n):
            if busca == tab[i][2]:
                codC, nomeC, centro = tab[i][0:]
                print('Curso %d e %s e seu centro é %d.' % (codC, nomeC, centro))
            i = i +1
        if i >= n:
            print('Curso não encontratado  (codC)',tab)
        busca = int(input('Digite o codigo do curso para busca (<=0 para parar): '))
print('Fim Programa!.')

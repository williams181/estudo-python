"""
Faça um programa Python para ler um arquivo texto. com nome externo a ser informado pelo usuário, contendo informações de todas as
disciplinas da universidade, uma disciplina por linha. Cada disciplina tem código (string com 5 posições), nome (string com 35 posições),
é número de créditos (inteiro com 2 posições), com um espaço adicional de separação entre eles. Caso o nome do arquivo não seja correto,
o seu programa deve informar o usuário que não encontrou o arquivo e terminar a execução. Caso consiga ler o arquivo, o seu programa
deve imprimir as seguintes informações:
  * Os dados (código, nome e créditos) de todas as disciplinas cujos códigos começam por "IF" e terminam por "3" (ex: IF423);
  * A quantidade de disciplinas impressas no item anterior;
  * A soma dos créditos destas disciplinas; e
  * A quantidade total de disciplinas que existe no arquivo lido.
"""

def Universidade(univer, base):
    grav = 0
    nomeArqEnt = 'D:\\' + univer + ".txt"
    nomeArqSai = 'D:\\' + univer + "Disciplinas.txt"
    arqEnt = open(nomeArqEnt, 'r')
    arqSai = open(nomeArqSai, 'w')
    for linha in arqEnt:
        cod = linha[0:5]
        nome = linha[6:41]
        cred = linha[42:44]
        pontos = int(cred)
        if pontos > base:
            arqSai.write('%s %s\n' % (univer, cred))
            grav += 1
    arqEnt.close()
    arqSai.close()
    print('Gravado arq. da universidade', univer)
    if grav > 0:
        print("Disciplinas gravadas!")
    else:
        print("Não há disciplinas gravadas!")

n = int(input("Digite o numero (>0) de disciplinas a processar: "))
while n < 1:
    n = int(input("Digite o numero (>0) de disciplinas a processar: "))
for i in range(n):
    cod = input("Digite o codigo da disciplina: ")
    nome = input("Digite o nome da disciplina: ")
    cred = int(input("Digite o credito da disciplina: "))
    while cred < 0:
        cred = int(input("Digite o credito da disciplina: "))
    try:
        Universidade(nome, cred)
    except IOError:
        print("Erro no arquivo da universidade", nome)
print("Fim do programa!")

nomeArq = input('Nome do arquivo: ')
disc = discIF3 = credIF3 = 0
try:
    arqEnt = open(nomeArq, 'r')
    print('Disciplinas com código começando por IF e terminando por 3:')
    for lin in arqEnt:
        disc += 1
        cod = lin[0:5]
        nome = lin[6:41]
        cred = int(lin[42:44])
        if (cod[0:2] == 'IF') and (cod[4] == '3'):
            print(cod, nome, cred)
            discIF3 += 1
            credIF3 += cred
    arqEnt.close()
    print('Quantidade de disciplinas selecionadas:', discIF3)
    print('Total de créditos dessas disciplinas:', credIF3)
    print('Total de disciplinas do arquivo lido:', disc)
except IOError:
    print('Erro no arquivo')
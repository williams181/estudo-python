"""
Faça um programa Python para ler um arquivo (nome externo 'funcionarios.csv'), contendo informações das pessoas que trabalham em uma
empresa: matrícula (inteiro com 4 posições), sexo (inteiro com 1 posição, sendo 1=masc, e 2=fem.), nome (string com 30 posições),
e salário (float com 10 posições, já inclusos o ponto decimal e 2 casas decimais). Um arquivo exemplo será fornecido juntamente com a
questão: observe que as informações são separadas pelo caracter ";" (ponto-e-vírgula) no forma csv.

O seu programa deve criar um arquivo (seu nome externo deve ser informado pelo usuário) contendo somente a matrícula e o salário dos
funcionários (um funcionário por linha) com salário acima de um dado valor (informado antes pelo usuário).

No final, o seu programa deve imprimir (na tela do terminal) um resumo das informações gravadas no arquivo contendo o número de
registros gravados no arquivo e as médias dos salários destes funcionários separados por sexo.
"""

def Empresa(func, base):
    media = 0.0
    grav = 0
    nomeArqEnt = 'D:\\' + func + '.csv'
    nomeArqSai = 'D:\\' + func + 'Info.csv'
    arqEnt = open(nomeArqEnt, 'r')
    arqSai = open(nomeArqSai, 'w')
    for linha in arqEnt:
        matr = linha[0:3]
        sexo = linha[4:5]
        nome = linha[6:35]
        salarioSt = linha[36:45]
        salarios = int(salarioSt)
        if salarios > base:
            arqSai.write('%s %s\n' % (matr, salarios))
            media = media + salarios
            grav = grav + 1
    arqEnt.close()
    arqSai.close()
    print('Gravando arq. dos funcionarios da empresa', func)
    if grav > 0:
        media = media / grav
        print(' Selec.', grav, 'funcionarios, com média de', media, 'salarios.')
    else:
        print(' Nenhum funcionario selecionado.')
    return

n = int(input('Digite o numero (>0) empresas a processar: '))
while n < 1:
    n = int(input('Digite o numero (>0) de empresas a processar: '))

for n in range(n):
    nome = input('Digite o nome da empresa: ')
    salar = float(input('Digite o salario base (>=0) a ser usada: '))
    while salar < 0:
        salar = float(input('Digite o salario base (>=0) a ser usada: '))
    try:
        Empresa(nome, salar)
    except IOError:
        print('Erro no arquivo da empresa', nome, ': empresa desprezada.')
print('Fim do programa')

# segunda resposta com base no exemplo do professor prova turma 25

nomeArq = input('Nome do arquivo: ')
func = medMasc = medFem = 0
try:
    arqEnt = open(nomeArq, 'r')
    print('Informações dos funcionarios da empresa: ', nomeArq)
    for linha in arqEnt:
        func += 1
        mat = linha[0:4]
        sex = linha[6]
        codSex = int(sex)
        nome = linha[7:38]
        sal = float(linha[39:50])
        if codSex == 1:
            print(mat, sex, nome, sal)
            medMasc += sal
            print("O total de registros é: ", func, "com a média dos salários masculinos sendo de: ", medMasc / func)
        elif codSex == 2:
            medFem += sal
            print("O total de registros é: ", func, "com a média dos salários femininos sendo de: ", medFem / func)
        else:
            print('Não binario')
    arqEnt.close()
except IOError:
    print('Erro no arquivo')

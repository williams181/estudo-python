"""
Faça uma subrotina Python do tipo procedimento chamada melhoresClientes para:

    (a) ler um arquivo texto, cujo nome externo é formado a partir do nome de uma empresa, recebido como parametro, seguido da extensão
        '.txt'. O arquivo conterá as informações dos clientes do programa de fidelidade desta empresa, a saber; matrícula (inteiro com
        5 dígitos), sexo (1 = masculino ou 2 = feminino), número de pontos (inteiro com 7 dígitos), e nome do cliente (string com 35
        posições). Arquivo exemplo será fornecido juntamente com a questão.
    (b) Gravar um arquivo, cujo nome externo é 'Melhores' concatenado após o nome da empresa, seguido da extensão '.txt', contendo
        somente a matrícula e o total de pontos (um cliente por linha) dos clientes com pontuação acima de um dado valor recebido
        como segundo parametro na subrotina. 
    (c) No final, o procedimento deve imprimir (na tela do terminal) um resumo das informações gravadas no arquivo contendo o nome
        da empresa, o número de registros gravados no arquivo e a média das pontuações destes melhores clientes.
    Faça também um programa principal que leia o nome da empresa e o total de pontos a ser considerado na escolha dos melhores clientes
    de N empresas, com N informado no incício pelo usuário, e faça uso do proceidmento MelhoresClientes para uma delas. Caso ocorra erro
    no arquivo de alguma das empresas, no seu programa deve informar o usuário e desconsiderar esta empresa, possivelmente continuando
    a executar com outras empresas.
"""

def MelhoresClientes(nomeEmpresa, valorPontuacao):
    grav = medMasc = medFem = qtdMasc = qtdFem = 0
    try:
        arqEnt = open('D://william//' + nomeEmpresa + '.txt', 'r')
        arqSai = open('D://william//' + nomeEmpresa + 'Melhores.txt', 'w')
        for linha in arqEnt:
            matricula = linha[0:5]
            matriculaInt = int(matricula)
            sexo = linha[6]
            numeroPontos = linha[8:15]
            numeroPontosInt = int(numeroPontos)
            nome = linha[16:51]
            if (valorPontuacao > numeroPontos):
                arqSai.write('%d %d\n' % (matriculaInt, numeroPontosInt))
                grav = grav + 1
            if (sexo == '1'):
                qtdMasc += 1
                medMasc += numeroPontosInt
            elif (sexo == '1'):
                qtdFem += 1
                medFem += numeroPontosInt
        arqEnt.close()
        arqSai.close()
        print('A media das pontuações dos homen é: ',medMasc/qtdMasc)
        print('A media das pontuações dos mulhres é: ',medFem/qtdFem)
        print('O nome do arquivo é: ',nomeEmpresa)
        print('Aquantidade de registros gravados é: ',grav)
    except IOError as msg:
        print('Erro',msg)
        
n = int(input("Digite a quantidade de empresas: "))

while (n < 1):
    n = int(input("A quantidade de empresas deve ser maior que 0: "))
    
for i in range(n):
    nome = input('Digite o nome da empresa: ')
    pontos = int(input("Digite os pontos da empresa: "))
    MelhoresClientes(nome, pontos)
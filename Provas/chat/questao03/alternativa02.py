"""
### Questão 2
Faça um programa Python para ler um arquivo (nome externo 'estudantes.csv'), 
contendo informações das pessoas que estudam em uma escola: matrícula 
(inteiro com 6 posições), sexo (inteiro com 1 posição, sendo 1=masc, e 2=fem.), 
nome (string com 35 posições), e média final (float com 5 posições, já inclusos 
o ponto decimal e 2 casas decimais). Um arquivo exemplo será fornecido juntamente 
com a questão: observe que as informações são separadas pelo caracter ";" 
(ponto-e-vírgula) no formato csv.
O seu programa deve criar um arquivo (seu nome externo deve ser informado 
pelo usuário) contendo somente a matrícula e a média final dos estudantes 
(um estudante por linha) com média acima de um dado valor (informado antes 
pelo usuário).
No final, o seu programa deve imprimir (na tela do terminal) um resumo das 
informações gravadas no arquivo contendo o número de registros gravados no arquivo 
e as médias das notas destes estudantes separados por sexo.
"""

def escola(nomeArquivo, valorMedia):
    grav = mediaHomem = mediaMulher = qtdMedMulher = qtdMedHomem = 0
    try:
        arqEnt = open('D:\\'+nomeArquivo+'.csv')
        arqSai = open('D:\\'+nomeArquivo+'Melhores.csv')
        for linha in nomeArquivo:
            matricula = linha[0:6]
            sexo = linha[7:8]
            nome = linha[9:44]
            mediaFinal = linha[45:55]
            mediaFinalFloat = float(mediaFinal)
            if (mediaFinal > valorMedia):
                arqSai.write('%d; %d; %s; %f;\n' % (matricula, sexo, nome, mediaFinalFloat))
                grav += 1
            if (sexo == 1):
                mediaMulher +=  mediaFinalFloat
                qtdMedMulher += 1
            elif (sexo == 2):
                mediaHomem += mediaFinalFloat
                qtdMedHomem += 1
            arqEnt.close()
            arqSai.close()
        print("Arquivo gravado com sucesso. ",nomeArquivo)
        print("O numero de registros gravados é: ",grav)
        print("A media das notas das mulheres é: ",mediaMulher/qtdMedMulher)
        print("A media das notas dos homens é: ",mediaHomem/qtdMedHomem)
    except IOError:
        print("Erro ao gravar o arquivo.")
        
n = int(input("Digite a quantidade de aquivos que deseja gravar: "))

while n < 1:
    n = int(input("Digite um numero maior que 0: "))
    
for i in range(n):
    nome = input("Digite o nome do arquivo: ")
    valor = input("Digite o valor da media: ")
    
    escola(nome, valor)
    
print("Fim do programa.")        
            
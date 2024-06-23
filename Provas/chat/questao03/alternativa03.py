"""
### Questão 3

Faça um programa Python para ler um arquivo texto, com nome 
externo a ser informado pelo usuário, contendo informações 
de todos os produtos de um supermercado, um produto por linha. 
Cada produto tem código (string com 6 posições), nome 
(string com 40 posições), e preço (float com 8 posições, 
já inclusos o ponto decimal e 2 casas decimais), com um espaço 
adicional de separação entre eles. Caso o nome do arquivo não 
seja correto, o seu programa deve informar o usuário que não 
encontrou o arquivo e terminar a execução. Caso consiga ler o 
arquivo, o seu programa deve imprimir as seguintes informações:

  * Os dados (código, nome e preço) de todos os produtos cujos 
  códigos começam por "PRD" e terminam por "0" (ex: PRD450);
  * A quantidade de produtos impressos no item anterior;
  * A soma dos preços destes produtos; e
  * A quantidade total de produtos que existe no arquivo lido.
"""

def supermercado(super):
    try: 
        grav = somaPreco = qtdProd = 0
        nomeArqEnt = 'D:\\' + super + '.txt'
        nomeArqSai = 'D:\\' + super + 'Produtos.txt'
        arqEnt = open(nomeArqEnt, 'r')
        arqSai = open(nomeArqSai, 'w')
        for linha in arqEnt:
            codigo = linha[0:6]
            nome = linha[8:48]
            preco = linha[50:58]
            if (codigo == 'PRD' and (codigo[:6])):
                arqSai.write('{} {} {:.2f}\n'.format(codigo, nome, preco))
                grav += 1
                qtdProd += 1
                somaPreco += preco
        arqEnt.close()
        arqSai.clone()
        print("Gravado arquivo do supermercado: ",super)
        if grav <= 0:
            print("Não foi gramado nenhum arquivo.")
        else:
            print("Arquivo gravado com sucesso.")
        print("A quantidade de registros gravados e: ",grav)
        print("A quatidade de produtos registrados é: ",qtdProd)
        print("A soma dos precos dos produtos é: ",somaPreco)
    except IOError:
        print("Erro ao gravar o arquivo.")
        
n = int(input("Digite o numero de registros: "))

while n < 0:
    n = int(input("Digite o numero de disciplinas (0 p/parar): "))

for i in range(n):
    cod = input("Digite o codigo do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preço do produto: ")
    
supermercado(nome)

"""
### Questão 3

Faça um programa Python para ler um arquivo texto, com nome externo a ser informado pelo usuário, contendo informações de todos os produtos de um supermercado, um produto por linha. Cada produto tem código (string com 6 posições), nome (string com 40 posições), e preço (float com 8 posições, já inclusos o ponto decimal e 2 casas decimais), com um espaço adicional de separação entre eles. Caso o nome do arquivo não seja correto, o seu programa deve informar o usuário que não encontrou o arquivo e terminar a execução. Caso consiga ler o arquivo, o seu programa deve imprimir as seguintes informações:

  * Os dados (código, nome e preço) de todos os produtos cujos códigos começam por "PRD" e terminam por "0" (ex: PRD450);
  * A quantidade de produtos impressos no item anterior;
  * A soma dos preços destes produtos; e
  * A quantidade total de produtos que existe no arquivo lido.
"""

def processaVendas(nomeArquivo, qtdMin, valorMin):
    try:
        with open(nomeArquivo, 'r') as arq:
            vendas = arq.readlines()
    except FileNotFoundError:
        print(f'Arquivo "{nomeArquivo}" não encontrado.')
        return
    
    produtosQtdMaior = []
    produtosValorMaior = []
    totalVendasQtd = 0.0
    totalVendasValor = 0.0

    for linha in vendas:
        codigo = linha[0:6].strip()
        quantidade = int(linha[7:12].strip())
        valorUnitario = float(linha[13:].strip())
        valorTotal = quantidade * valorUnitario

        if quantidade > qtdMin:
            produtosQtdMaior.append((codigo, quantidade, valorTotal))
            totalVendasQtd += valorTotal

        if valorUnitario > valorMin:
            produtosValorMaior.append((codigo, quantidade, valorTotal))
            totalVendasValor += valorTotal
    
    with open('produtosQtdMaior.txt', 'w') as arqQtd:
        for produto in produtosQtdMaior:
            arqQtd.write(f"{produto[0]} {produto[1]} {produto[2]:.2f}\n")
    
    with open('produtosValorMaior.txt', 'w') as arqValor:
        for produto in produtosValorMaior:
            arqValor.write(f"{produto[0]} {produto[1]} {produto[2]:.2f}\n")
    
    print(f"Quantidade total de produtos processados: {len(vendas)}")
    print(f"Total das vendas (quantidade > {qtdMin}): {totalVendasQtd:.2f}")
    print(f"Total das vendas (valor unitário > {valorMin}): {totalVendasValor:.2f}")

nomeArquivo = input("Digite o nome do arquivo de vendas: ")
qtdMin = int(input("Digite a quantidade mínima vendida: "))
valorMin = float(input("Digite o valor unitário mínimo: "))
processaVendas(nomeArquivo, qtdMin, valorMin)
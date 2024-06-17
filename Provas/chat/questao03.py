"""
### Questão 1

Faça uma subrotina Python do tipo procedimento chamada `melhoresVendedores` para:

(a) Ler um arquivo texto, cujo nome externo é formado a partir do nome de uma loja, recebido como parâmetro, seguido da extensão '.txt'. O arquivo conterá as informações dos vendedores da loja, a saber: matrícula (inteiro com 5 dígitos), sexo (1 = masculino ou 2 = feminino), total de vendas (inteiro com 8 dígitos), e nome do vendedor (string com 40 posições). Um arquivo exemplo será fornecido juntamente com a questão.

(b) Gravar um arquivo, cujo nome externo é 'TopVendedores' concatenado após o nome da loja, seguido da extensão '.txt', contendo somente a matrícula e o total de vendas (um vendedor por linha) dos vendedores com vendas acima de um dado valor recebido como segundo parâmetro na subrotina. Ou seja, este procedimento deve ter 2 parâmetros.

(c) No final, o procedimento deve imprimir (na tela do terminal) um resumo das informações gravadas no arquivo contendo o nome da loja, o número de registros gravados no arquivo e a média das vendas destes melhores vendedores.

Faça também um programa principal que leia o nome da loja e o total de vendas a ser considerado na escolha dos melhores vendedores de N lojas, com N informado no início pelo usuário, e faça uso do procedimento `melhoresVendedores` para cada uma delas. Caso ocorra erro no arquivo de alguma das lojas, o seu programa deve informar o usuário e desconsiderar esta loja, possivelmente continuando a executar com outras lojas.
"""

def processaFuncionarios(nomeArquivoSaida, salarioBase):
    try:
        with open('funcionarios.csv', 'r') as arqEnt:
            funcionarios = arqEnt.readlines()
    except FileNotFoundError:
        print('Arquivo "funcionarios.csv" não encontrado.')
        return
    
    with open(nomeArquivoSaida, 'w') as arqSai:
        totalMasculino = 0
        totalFeminino = 0
        qtdMasculino = 0
        qtdFeminino = 0
        registros = 0

        for linha in funcionarios:
            matricula, sexo, nome, salario = linha.strip().split(';')
            salario = float(salario)
            if salario > salarioBase:
                arqSai.write(f"{matricula} {salario:.2f}\n")
                registros += 1
                if sexo == '1':
                    totalMasculino += salario
                    qtdMasculino += 1
                elif sexo == '2':
                    totalFeminino += salario
                    qtdFeminino += 1

    print(f'Registros gravados: {registros}')
    if qtdMasculino > 0:
        mediaMasculino = totalMasculino / qtdMasculino
    else:
        mediaMasculino = 0.0
    if qtdFeminino > 0:
        mediaFeminino = totalFeminino / qtdFeminino
    else:
        mediaFeminino = 0.0

    print(f'Média dos salários dos funcionários masculinos: {mediaMasculino:.2f}')
    print(f'Média dos salários dos funcionários femininos: {mediaFeminino:.2f}')

nomeArquivoSaida = input('Digite o nome do arquivo de saída: ')
salarioBase = float(input('Digite o salário base: '))
processaFuncionarios(nomeArquivoSaida, salarioBase)

"""
### Questão 2

Faça um programa Python para ler um arquivo (nome externo 'estudantes.csv'), contendo informações das pessoas que estudam em uma escola: matrícula (inteiro com 6 posições), sexo (inteiro com 1 posição, sendo 1=masc, e 2=fem.), nome (string com 35 posições), e média final (float com 5 posições, já inclusos o ponto decimal e 2 casas decimais). Um arquivo exemplo será fornecido juntamente com a questão: observe que as informações são separadas pelo caracter ";" (ponto-e-vírgula) no formato csv.

O seu programa deve criar um arquivo (seu nome externo deve ser informado pelo usuário) contendo somente a matrícula e a média final dos estudantes (um estudante por linha) com média acima de um dado valor (informado antes pelo usuário).

No final, o seu programa deve imprimir (na tela do terminal) um resumo das informações gravadas no arquivo contendo o número de registros gravados no arquivo e as médias das notas destes estudantes separados por sexo.
"""

def processaDisciplinas(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arq:
            disciplinas = arq.readlines()
    except FileNotFoundError:
        print(f'Arquivo "{nomeArquivo}" não encontrado.')
        return
    
    totalDisciplinas = 0
    selecionadas = []
    somaCreditos = 0

    for linha in disciplinas:
        totalDisciplinas += 1
        codigo = linha[0:5].strip()
        nome = linha[6:41].strip()
        creditos = int(linha[42:].strip())
        
        if codigo.startswith("IF") and codigo.endswith("3"):
            selecionadas.append((codigo, nome, creditos))
            somaCreditos += creditos
    
    print("Disciplinas selecionadas:")
    for disciplina in selecionadas:
        print(f"Código: {disciplina[0]}, Nome: {disciplina[1]}, Créditos: {disciplina[2]}")
    
    print(f"Quantidade de disciplinas impressas: {len(selecionadas)}")
    print(f"Soma dos créditos das disciplinas impressas: {somaCreditos}")
    print(f"Quantidade total de disciplinas no arquivo: {totalDisciplinas}")

nomeArquivo = input("Digite o nome do arquivo de disciplinas: ")
processaDisciplinas(nomeArquivo)

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
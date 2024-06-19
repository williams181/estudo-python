"""
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
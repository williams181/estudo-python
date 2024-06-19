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
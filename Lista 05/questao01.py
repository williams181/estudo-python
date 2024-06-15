"""
Considere um arquivo texto cujo nome externo é 'discip.old' e que contém informações de disciplinas (Código com 5 posições, nome com
35 posições e créditos com 2 posições), uma disciplina por linha. Seu programa deve criar um segundo arquivo com nome externo 'discip.new'
contendo informações das mesmas disciplinas, mas com as seguintes modificações:
    (a) As disciplinas cujos códigos são IF125 e IF380 devem ser excluídas, i.e., não devem ser gravadas no novo arquivo.
    (b) Os números de créditos das disciplinas cujos códigos começam por MA devem ser alterados para 5.
    (c) O novo arquivo terá um campo a mais (carga horária, com 3 posições) cujo valor deve ser o número de créditos da disciplina
        multiplicado por 5.
    No final o seu programa deve imprimir o número de disciplinas de cada arquivo e ainda o número de disciplinas que tiveram deus números
    de créditos alterados.
"""
arquivo_antigo = open('discip.old', 'r')
arquivo_novo = open('discip.new', 'w')
total_disciplinas = 0
total_alteradas = 0
for linha in arquivo_antigo:
    codigo = linha[:5].strip()
    nome = linha[5:40].strip()
    creditos = int(linha[40:42])
    if codigo == 'IF125' or codigo == 'IF380':
        print()
    elif codigo.startswith('MA'):
        creditos = 5
        total_alteradas += 1
    carga_horaria = creditos * 5
    arquivo_novo.write(f"{codigo:5}{nome:35}{creditos:2}{carga_horaria:3}\n")
    total_disciplinas += 1
arquivo_antigo.close()
arquivo_novo.close()
print("Número de disciplinas no arquivo antigo:", total_disciplinas)
print("Número de disciplinas com número de créditos alterados:", total_alteradas)
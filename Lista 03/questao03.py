"""
Ler uma tabela de alunos onde:
    * Cada aluno tem cpf (inteiro), um nome (String) e uma idade (inteiro).
    * A leitura da tabela para com um cpf que não seja positivo.
    * Sabe-se que o usuário digitará no máximo 200 alunos.

    * Depois o usuário informará um inteiro positivo N, seguido por uma série de N intervalos de idade (idades mínima e máximo).
    * O programa deve imprimir, para cada intervalo digitado pelo usuário, os dados dos alunos que se enquadram no intervalo seguidos pelo
      número de alunos do intervalo.
    * Caso a idade mínima de algum intervalo não seja menor do que a idade máxima, o programa deve imprimir uma mensagem de erro e continuar.
"""

n = int(input("Digite o tamanho da tebala de alunos: "))
while (n < 1):
     n = int(input("Tamanho deve ser inteiro e positivo. Tente novamente: "))

tab = [None]*n

for i in range(n):
     cpf = int(input("Digite o CPF: "))
     while (cpf < 0):
        cpf = int(input("CPF deve ser inteiro positivo. Tente novamente: "))
     nome = input("Digite o nome: ")
     idade = int(input("Digite a idade: "))
     
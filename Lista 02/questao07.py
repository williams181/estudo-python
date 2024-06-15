N = int(input('Quantidade de notas de alunos: '))
Lista_Notas = []

for i in range(N):
    Nota1 = float(input('Digite a nota'))
    Lista_Notas.append(Nota1)

soma = 0.0
Lista_Resultado = []

for i in Lista_Notas:
    #Lista_Resultado += Lista_Notas
    print(i)
    soma += i

result = soma / len(Lista_Notas)
print(result)
#print(ListazNotas)
#print(Lista_Resultado)
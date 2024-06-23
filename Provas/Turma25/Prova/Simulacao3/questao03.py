def MelhoresClientes(arquivo, pontuacao):
	try:
		grav = 0
		medPont = 0
		arqEnt = open("C://william/" + arquivo + "txt", "r")
		arqSai = open("C://william/" + arquivo + "Melhores.txt", "w")
		for linha in arquivo:
			matricula = linha[0:5]
			sexo = linha[6:7]
			pontos = linha[8:14]
			postInt = int(pontos)
			nome = linha[15:50]
			if (postInt > pontuacao):
				arqSai.write("%s, %d," % (matricula, postInt))
				grav += 1	
			arqEnt.close()
			arqSai.clone()
		print("Arquivo gravado com sucesso. ",arquivo)
	except IOError:
		print("Erro ao gravar o arquivo. Tente novamente")

n = int(input("Digite a quantidade de arquivos que deseja processar: "))

while n < 1:
	n = int(input("Digite a quantidade de arquivos que deseja processar: "))

for i in range(n):
	nome = input("Digite o nome do cliente: ")
	pont = input("Digite a pontuacao deste cliente: ")
	
	MelhoresClientes(nome, pont)
print("Fim do programa.")
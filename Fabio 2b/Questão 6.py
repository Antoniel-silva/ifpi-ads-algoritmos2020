#6. Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino ou N para Noturno e
#escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

#entradas
turno = str(input("Digite um tuno: M, V ou N: "))

if turno == "M" or turno == "m":
	print("Bom dia!")

elif turno == "V" or turno == "v":
	print("Boa Tarde!")

elif turno == "N" or turno == "n":
	print("Boa Noite!")

else:
	print("Valor Invalido!")

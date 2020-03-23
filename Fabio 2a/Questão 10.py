#10. Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

#entradas

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))


if (dia <= 31 and dia >= 1) and (mes <= 12 and mes >= 1) and (ano > 0):
	print("Data válida.")

else:
	print("Data inválida.")

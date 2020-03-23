#15. Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
#Escreva na tela qual dos professores tem salário total maior.

#entradas
prof1 = int(input("Digite a quantidade de horas aulas do professor 1: "))
valor1 = float(input("Digite o valor da h/a: "))
prof2 = int(input("Digite a quantidade de horas aulas do professor 2: "))
valor2 = float(input("Digite o valor da h/a: "))

total1 = prof1 * valor1
total2 = prof2 * valor2

if total1 > total2:
	print("O professor 1 ganha mais.")

else:
	print("O professor 2 ganha mais.")
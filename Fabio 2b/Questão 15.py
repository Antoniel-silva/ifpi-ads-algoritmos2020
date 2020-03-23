#15. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#            Até 5 Kg         Acima de 5 Kg
#Morango R$ 2,50 por Kg     R$ 2,20 por Kg
#Maçã R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
#ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
#morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

#entradas
fruta = str(input("Qual fruta? mo para morango e ma para maçã: "))
qtd = float(input("Digite a quantidade Kg de fruta: "))

if fruta == "mo" and qtd <= 5:
	valor = qtd * 2.5
	print(f'O valor total é {valor} reais.')


elif fruta == "mo" and qtd > 5:
	valor = qtd * 2.2
	print(f'O valor total é {valor} reais.')


elif fruta == "mo" and qtd > 8:
	valor = qtd * 2.2
	print(f'O valor total é {valor - (valor * .1)} reais.')


elif fruta == "mo" and qtd > 8:
	valor = qtd * 2.2
	if valor == 25:
		print(f'O valor total é {valor - (valor * .1)} reais.')





elif fruta == "ma" and qtd <= 5:
	valor = qtd * 1.8
	print(f'O valor total é {valor} reais.')


elif fruta == "mo" and qtd > 5:
	valor = qtd * 1.5
	print(f'O valor total é {valor} reais.')


elif fruta == "mo" and qtd > 8:
	valor = qtd * 1.5
	print(f'O valor total é {valor - (valor * .1)} reais.')


elif fruta == "mo" and qtd > 8:
	valor = qtd * 1.5
	if valor == 25:
		print(f'O valor total é {valor - (valor * .1)} reais.')



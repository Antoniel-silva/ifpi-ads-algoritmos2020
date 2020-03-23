#14. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#1. Álcool:
#· até 20 litros, desconto de 3% por litro
#· acima de 20 litros, desconto de 5% por litro
#2. Gasolina:
#· até 20 litros, desconto de 4% por litro
#· acima de 20 litros, desconto de 6% por litro.
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
#seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
#o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

#entradas
litros = int(input("Digite a quantidade de litros: "))
comb = str(input("Digite A, para álcool ou G, para Gasolina: "))

if comb == "A" or comb == "G":
	if litros <= 20 and comb == "A":
		a = (litros * 1.9)
		desconto = a - (a * .03)
		print(f'O valor a ser pago por {litros}L de Alcool é R$ {desconto}')

	elif litros > 20 and comb == "A":
		a = (litros * 1.9)
		desconto = a - (a * .05)
		print(f'O valor a ser pago por {litros}L de Alcool é R$ {desconto}')

	elif litros <= 20 and comb == "G":
		a = (litros * 2.5)
		desconto = a - (a * .04)
		print(f'O valor a ser pago por {litros}L de Gasolina é R$ {desconto}')

	elif litros > 20 and comb == "G":
		a = (litros * 2.5)
		desconto = a - (a * .06)
		print(f'O valor a ser pago por {litros}L de Gasolina é R$ {desconto}')

else:
        print("Não é um codigo de combustível válido!")

		

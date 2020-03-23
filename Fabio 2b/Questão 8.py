#8. Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
#depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
#11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde
#ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
#quantidade de horas trabalhadas no mês.
#Desconto do IR:
#o Salário Bruto até R$ 900,00 (inclusive) - isento
#o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
#o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
#o Salário Bruto acima de R$ 2.500,00 - desconto de 20%
#Escreva na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e
#a quantidade de hora é 220.
#Salário Bruto: (5 * 220) : R$ 1100,00
#(-) IR (5%) : R$ 55,00
#(-) INSS ( 10%) : R$ 110,00
#FGTS (11%) : R$ 121,00
#Total de descontos : R$ 165,00
#Salário Liquido : R$ 935,00

#entradas
valor_horas = float(input("Digite o valor da hora trabalhada: "))
qtd_horas = int(input("Digite a quantidade de horas trabalhadas: "))
salario = valor_horas * qtd_horas

if salario <= 900:
	print(f'Salário Bruto: R$ {salario}')
	print(f'(-) IR (ISENTO)')
	print(f'(-) INSS (ISENTO)')
	print(f'FGTS (ISENTO)')
	print(f'Total de Descontos: R$ 0,00')
	print(f'Salario Liquido : R$ {salario}')


elif salario > 900 and salario <= 1500:
	print(f'Salário Bruto: R$ {salario}')
	print(f'(-) IR (5%) : R$ {salario * .05}')
	print(f'(-) INSS (10%) : R$ {salario * .1}')
	print(f'FGTS (11%) : R$ {salario * .11}')
	print(f'Total de Descontos: R$ {(salario * .05) + (salario * .1) + (salario * .11)}')
	print(f'Salario Liquido : R$ {salario - ((salario * .05) + (salario * .1) + (salario * .11))}')


elif salario > 1500 and salario <= 2500:
	print(f'Salário Bruto: R$ {salario}')
	print(f'(-) IR (10%) : R$ {salario * .1}')
	print(f'(-) INSS (10%) : R$ {salario * .1}')
	print(f'FGTS (11%) : R$ {salario * .11}')
	print(f'Total de Descontos: R$ {(salario * .05) + (salario * .1) + (salario * .11)}')
	print(f'Salario Liquido : R$ {salario - ((salario * .1) + (salario * .1) + (salario * .11))}')


elif salario >= 2500:
	print(f'Salário Bruto: R$ {salario}')
	print(f'(-) IR (20%) : R$ {salario * .2}')
	print(f'(-) INSS (10%) : R$ {salario * .1}')
	print(f'FGTS (11%) : R$ {salario * .11}')
	print(f'Total de Descontos: R$ {(salario * .05) + (salario * .1) + (salario * .11)}')
	print(f'Salario Liquido : R$ {salario - ((salario * .2) + (salario * .1) + (salario * .11))}')
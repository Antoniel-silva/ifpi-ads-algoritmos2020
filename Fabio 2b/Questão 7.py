#7. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
#contrataram para desenvolver o programa que calculará os reajustes. Escreva um algoritmo que leia o
#salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#o salários até R$ 280,00 (incluindo) : aumento de 20%
#o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#· o salário antes do reajuste;
#· o percentual de aumento aplicado;
#· o valor do aumento;
#· o novo salário, após o aumento.

#entradas

salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
	novo_salario = salario + (salario * .2)
	print(f'O salario antes do reajuste é {salario}')
	print('O percentual de aumento foi de 20%')
	print(f'O aumento foi de {novo_salario - salario}')
	print(f'O novo salario é: {novo_salario}')

elif salario > 280 and salario <= 700:
	novo_salario = salario + (salario * .15)
	print(f'O salario antes do reajuste é {salario}')
	print('O percentual de aumento foi de 15%')
	print(f'O aumento foi de {novo_salario - salario}')
	print(f'O novo salario é: {novo_salario}')

elif salario > 700 and salario <= 1500:
	novo_salario = salario + (salario * .10)
	print(f'O salario antes do reajuste é {salario}')
	print('O percentual de aumento foi de 10%')
	print(f'O aumento foi de {novo_salario - salario}')
	print(f'O novo salario é: {novo_salario}')

elif salario > 1500:
	novo_salario = salario + (salario * .05)
	print(f'O salario antes do reajuste é {salario}')
	print('O percentual de aumento foi de 5%')
	print(f'O aumento foi de {novo_salario - salario}')
	print(f'O novo salario é: {novo_salario}')
#4. Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente
#do algarismo da unidade.
#entradas
a = int(input("Digite um número inteiro de 2 algarismos: "))

num1 = a // 10
num2 = a % 10

if num1 == num2:
	print("Os algarismos são iguais.")

else:
	print("Os algarismos são diferentes!")

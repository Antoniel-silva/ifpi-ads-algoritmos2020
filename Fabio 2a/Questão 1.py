#1. Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a == b == c:
	print("Todos são iguais!")

elif a != b and a != c and b != c:
	print("Todos diferentes")

elif a == b and a != c:
	print("Dois números iguais")

elif a != b and a == c:
	print("Dois números iguais")

elif a != b and a != c and b == c:
	print("Dois números iguais")

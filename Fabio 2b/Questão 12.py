#12. Leia um número e escreva se o número é inteiro ou decimal.

#entrada
num = float(input("Digite um numero: "))

#processamento
if num % (num //1) == 0:
	print("É inteiro!")

else:
	print("É decimal")

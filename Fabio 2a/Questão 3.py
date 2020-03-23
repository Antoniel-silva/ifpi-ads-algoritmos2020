#3. Leia 3 (três) números, verifique e escreva o maior entre os números lidos.
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a > b and a > c:
	print(f'O numero {a} é maior')
if a < b and b > c:
	print(f'O numero {b} é maior')
if a < c and b < c:
        print(f'O número {c} é maior')
#13. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são
#diferentes.

#entradas
num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))
num3 = int(input("Digite o 3° número: "))
num4 = int(input("Digite o 4° número: "))
num5 = int(input("Digite o 5° número: "))

if num1 > num2 > num3 > num4 > num5:
	print(f'{num1} é maior.')

elif num1 < num2 > num3 > num4 > num5:
        print(f'{num2} é maior.')

elif num1 > num2 < num3  > num4 > num5:
        print(f'{num3} é maior.')

elif num1 > num2 > num3 < num4 > num5:
        print(f'{num4} é maior.')

elif num1 > num2 > num3 > num4 < num5:
        print(f'{num5} é maior.')

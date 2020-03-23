#14. Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.

#entradas
num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))
num3 = int(input("Digite o 3° número: "))
num4 = int(input("Digite o 4° número: "))
num5 = int(input("Digite o 5° número: "))

#processamento e saida

media = (num1 + num2 + num3 + num4 + num5) / 5
if media >=1:

        if media < num1 and media < num2 and media < num3 and media < num4:
                print(f'{num1} {num2} {num3} {num4} são maiores que a média')

        elif media < num1 and media < num2 and media < num3:
                print(f'{num1} {num2} {num3} são maiores que a média')

        elif media < num1 and media < num2:
                print(f'{num1} {num2} são maiores que a média')

        elif media < num1:
                print(f'{num1} é maior que a média')

        elif media < num2 and media < num3 and media < num4 and media < num5:
                print(f'{num2} {num3} {num4} {num5} são maiores que a média')
        elif media < num3 and media < num4 and media < num5:
                print(f'{num3} {num4} {num5} são maiores que a média')
        elif media < num4 and media < num5:
                print(f'{num4} {num5} são maiores que a média')
        elif media < num5:
                print(f'{num5} é maior que a média')


else:
	print("Os numeros não são maiores que a media")

#11. Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
#valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
#possíveis para a variável opção são 1, 2 e 3.

#entradas

opcao = int(input("Digite uma opção de 1 a 3: "))
if opcao <= 3 and opcao > 0:
        num1 = int(input("Digite o numero 1: "))
        num2 = int(input("Digite o numero 2: "))
        num3 = int(input("Digite o numero 3: "))

        if opcao >=1 and opcao <=3:
                if opcao == 1:
                        print(f'{num1} foi o número escolhido')

                if opcao == 2:
                        print(f'{num2} foi o número escolhido')

                if opcao == 3:
                        print(f'{num3} foi o número escolhido')

else:
	print("Numero fora do intervalo!")

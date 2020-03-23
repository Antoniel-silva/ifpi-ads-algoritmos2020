#17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
#escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
#são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
#divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
#escreva o quadrado dos números lidos.

#entradas
v1 = int(input("Digite um número: "))
v2 = int(input("Digite outro número: "))

resto_divisao = v1 % v2
#print(resto_divisao)

if resto_divisao == 1:
	print("A soma com o resto é igual a:",v1+v2+resto_divisao)

elif resto_divisao == 2:
	if (v1 % 2) == 0 and v2 % 2 == 0:
		print(f'O número {v1} e {v2} são pares')
		
        if v1 % 2 == 1 and v2 % 2 == 0:
                print(f'O número {v1} é impar e o número {v2} é par')
	
        #elif v1 % 2 == 1 and v2 % 2 == 0:
                #print(f'O número {v1} é impar e o número {v2} é par')

        #elif v1 % 2 == 0 and v2 % 2 == 1:
                #print(f'O número {v1} é par e o número {v2} é impar')

        #else:
                #print(f'O número {v1} e {v2} são impares')

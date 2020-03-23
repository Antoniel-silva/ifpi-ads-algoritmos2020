#7. Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
#(três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
#formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
#escaleno (3 lados diferentes). dNão existe lado com tamanho 0 (zero).

#entradas

lad1 = float(input("Digite o valor do primeiro ângulo: "))
lad2 = float(input("Digite o valor do segundo ângulo: "))
lad3 = float(input("Digite o valor do terceiro ângulo: "))

#processamento
if lad1 and lad2 and lad3 != 0:
        if lad1 == lad2 == lad3 or (lad1 +lad2) >= lad3:
                if lad1 == lad2 == lad3:
                        print("Triangulo Equilátero")

                elif lad1 == lad2 or lad1 == lad3 or lad2 == lad3:
                        print("Triangulo isósceles")

                else:
                        print("Triangulo escaleno")

else:
	print("Não forma um triângulo")

#6. Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
#se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180º). Se formam,
#verifique se formam um triângulo acutângulo (3 ângulos < 90º), retângulo (1 ângulo = 90º) ou
#obtusângulo (1 ângulo > 90º). Não existe ângulo com tamanho 0º (zero grau).

#entradas:
ang1 = float(input("Digite o valor do primeiro ângulo: "))
ang2 = float(input("Digite o valor do segundo ângulo: "))
ang3 = float(input("Digite o valor do terceiro ângulo: "))

#processamento
if (ang1 + ang2 + ang3) == 180:
        if ang1 and ang2 and ang3 < 90:
                print("Formou um triangulo acutângulo")

        if ang1 == 90 or ang2 == 90 or ang3 == 90:
                print("Formou um triangulo retângulo")

        if ang1 > 90 or ang2 >90 or ang3 > 90:
                print("Formou um triangulo obtusângulo")

        else:
                print("Triangulo não tem classificação")

else:
        print("Não forma um triângulo")

#5. Leia 3 (três) números e escreva-os em ordem crescente.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a <b and a < c and b < c:
	print("A ordem crescente é:" ,a,b,c)
	

elif a > b and a < c and b < c:
        print("A ordem crescente é: ", b,a,c)

        
elif a > b and a > c and b > c:
        print("A ordem crescente é: ", c,b,a)


elif a > b and a > c and b < c:
        print("A ordem crescente é: ", b,c,a)


elif a < b and a > c and b > c:
        print("A ordem crescente é: ", c,a,b)

#Q18 Leia N, calcule e escreva o valor de S

#entradas:
n = int(input("Digite o valor de N: "))

numerador = 1
denominador = n
con = 1
b = 0

while con <= n:
    s = numerador/denominador
 
    b+= s
    con+=1
    numerador+=1
    denominador-=1
    
print(f' o valor total é: {b}')

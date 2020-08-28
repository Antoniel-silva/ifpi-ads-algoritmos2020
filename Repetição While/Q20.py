#Q20 Leia N, calcule e escreva o valor de S

#entradas:
n = int(input("Digite o valor de N: "))

numerador = 1
con = 1
b = 0
s = 0

while con <= n:
    if con % 2 == 0:
        s = s - (numerador/con)
        con+=1
        
    else:
        s = s + (numerador/con)
        con+=1
        
con+=1
    

print(f' o valor total é: {s}')

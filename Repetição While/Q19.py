#Q19 Leia N, calcule e escreva o valor de S

#entradas:
n = int(input("Digite o valor de N: "))

numerador = n
con = 1
s = 0

while con <= n:
    if con % 2 == 0:
        s = s - (numerador/con)
        
    else:
        s = s + (con/numerador)
        
    numerador-=1    
    con+=1
    

print(f' o valor total é: {s}')

#5. Leia um número, calcule e escreva seu fatorial.

#entradas
con = 0
n = int(input("Digite um número para calcular seu fac! : "))
con2 = n
t = 0


while con <= n:
    a = con2 - 1
    con += 1
    con2 -= 1
    t *= a

print(t)
    
    

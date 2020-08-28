#Q21
#entradas
n = int(input("Digite o valor de N: "))

#processamenrto
numerador = 1
denominador = 1
con = 1
total = 0

while con <= n:
    s = numerador / denominador
    total+= s

    con += 1
    numerador += 2
    denominador += 1

print(f' O valor é {total}')


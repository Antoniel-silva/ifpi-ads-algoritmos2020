#12. Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.
n = int(input("Digite um valor para N: "))
con = 1
total = 0
while con <= n:
    b = int(input(f' Digite o valor do {con}° número: '))
    total+= b
    con +=1
print(f' A soma é {total} e a média é {total / n}')

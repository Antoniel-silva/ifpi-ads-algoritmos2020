#2. Leia N e escreva todos os números inteiros pares de 1 a N.

#entrada:
con = 1
n = int(input("Digite um valor maior que 0: "))

while con <= n:
    if con % 2 == 0:
        print(con)
    con += 1

print("fim")

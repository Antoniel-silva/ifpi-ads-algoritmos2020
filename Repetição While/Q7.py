#7. Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.

n = int(input("Digite o valor para N:  "))
con = 1
a = 0

while con <= n:
    a += con
    con += 1

print(f' A soma dos númeos inteiros entre 1 e {n} é: {a}')

#3. Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
#Aritmética que tem por valor inicial A0 e razão R.

#entradas:

a = int(input("Digite o valor do primeiro número da P.A.: "))
limite = int(input("Digite o valor do limite da P.A.: "))
r = int(input("Digite o valor da razão da P.A.: "))

while a <= limite:
    print(a)
    a += r

print("fim")

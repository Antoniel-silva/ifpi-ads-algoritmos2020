#5. Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é
#sempre pelo mais barato.

#entradas
preco1 = float(input("Digite o preço do 1° produto: "))
preco2 = float(input("Digite o preço do 2° produto: "))
preco3 = float(input("Digite o preço do 3° produto: "))

if preco1 > preco2 > preco3:
	print(f'{preco3} é o mais barato.')


elif preco1 > preco2 < preco3:
        print(f'{preco2} é o mais barato.')

elif preco1 < preco2 < preco3:
        print(f'{preco1} é o mais barato.')


elif preco1 < preco2 > preco3 and preco1 > preco3:
        print(f'{preco3} é o mais barato.')

elif preco1 < preco2 > preco3 and preco1 < preco3:
        print(f'{preco1} é o mais barato.')

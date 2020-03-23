#11. Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
#número. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplos:
#o 326 = 3 centenas, 2 dezenas e 6 unidades
#o 12 = 1 dezena e 2 unidades

#entradas
num = int(input("Digite um número inteiro menor que 1000: "))

if num < 1000:
        c = num // 100
        d = num // 10 % 10
        u = num % 10

        if c == 1 and d == 1 and u == 1:
                print(f'{c} centena, {d} dezena e {u} unidade.')

        elif c == 1 and d == 0 and u == 0:
                print(f'{c} centena.')

        elif c == 1 and d == 1 and u == 0:
                print(f'{c} centena, {d} dezena')

        elif c == 0 and d == 0 and u == 1:
                print(f'{u} unidade.')


        elif c > 1 and d == 0 and u == 0:
                print(f'{c} centenas.')

        elif c == 1 and d > 1 and u == 0:
                print(f'{c} centena, {d} dezenas')

        elif c == 0 and d == 0 and u > 1:
                print(f'{u} unidades.')

        elif c == 0 and d > 1 and u == 0:
                print(f'{d} dezenas')

        elif c == 0 and d == 1 and u == 0:
                print(f'{d} dezena')

        elif c > 1 and d > 1 and u == 0:
                print(f'{c} centenas, {d} dezenas')



        elif c > 1 and d == 1 and u == 1:
                print(f'{c} centenas, {d} dezena e {u} unidade.')

        elif c > 1 and d > 1 and u == 1:
                print(f'{c} centenas, {d} dezenas e {u} unidade.')

        elif c > 1 and d > 1 and u > 1:
                print(f'{c} centenas, {d} dezenas e {u} unidades.')

        elif c == 1 and d > 1 and u == 1:
                print(f'{c} centena, {d} dezenas e {u} unidade.')

        elif c == 1 and d == 1 and u > 1:
                print(f'{c} centena, {d} dezena e {u} unidades.')

        elif c == 1 and d > 1 and u > 1:
                print(f'{c} centena, {d} dezenas e {u} unidades.')

        elif c > 1 and d == 1 and u > 1:
                print(f'{c} centenas, {d} dezena e {u} unidades')

        elif c > 1 and d == 0 and u > 1:
                print(f'{c} centenas e {u} unidades')


        elif c == 0 and d == 1 and u == 0:
                print(f'{d} dezena')

        elif c == 0 and d == 0 and u == 1:
                print(f'{u} unidade')

        elif c == 0 and d == 1 and u == 1:
                print(f'{d} dezena e {u} unidade')

        elif c == 0 and d == 1 and u > 1:
                print(f'{d} dezena e {u} unidades')

        elif c == 1 and d == 0 and u == 1:
                print(f'{c} centena e {u} unidade')

        elif c == 1 and d == 0 and u > 1:
                print(f'{c} centena e {u} unidades')

else:
        print("Numero fora do intervalo!")


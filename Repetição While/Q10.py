#10. Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.
limiteinf = int(input("Digite um limite inferior: "))
limitesupe = int(input("Digite um limite superior: "))
con = 0
while limiteinf <= limitesupe:
    a = limiteinf % 2
    if a != 0:
        print(limiteinf)

    limiteinf += 1
    con += 1

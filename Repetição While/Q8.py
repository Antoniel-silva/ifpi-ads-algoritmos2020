#8. Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.
n = int(input("Digite um número: "))
limite1 = int(input("Digite o valor inicial: "))
limite2 = int(input("Digite o valor final: "))

while limite1 <= limite2:
    if limite1 % n == 0:
        print(n)
        limite1+=1

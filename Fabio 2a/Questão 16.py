#16. Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
#ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
#final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
#escreva “Reprovado”.

#entradas
		
n1 = float(input("escreva a primeira nota: "))
n2 = float(input("escreva a segunda nota: "))
med = (n1 + n2)/2


if med >= 7:
    print("Aprovado")

elif med < 7 and med >= 5:
    exame = float(input("Digite a nota do exame: "))
    media_final = (med + exame) / 2
    if media_final >= 5:
        print("Aprovado")
    else:
        print("REPROVADO NOVAMENTE EM ALGORITMO!!")

else:
    print("REPROVADO NOVAMENTE EM ALGORITMO!!")

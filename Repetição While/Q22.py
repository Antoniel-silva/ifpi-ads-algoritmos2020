#22. Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
#nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
#numero de identificação e o peso do boi mais magro e do boi mais gordo.

n = int(input("Digite o valor de N: "))
con = 1
p1 = 0
nome1 = ""
p2 = 0
nome2 = ""

while con<= n:
    boi = str(input("Digite o nome: "))
    peso = float(input("Digite o peso: "))

    if peso > p1:
        p1 = peso
        nome1 = boi

    elif peso < p1:
        p2 = peso
        nome2 = boi

    
    con+=1

print(f' O nome do boi mais pesado é {nome1} e possue {p1} KGs')
print(f' O nome do boi mais maneiro é {nome2} e pesa {p2} KGs')

#8. Leia um vetor com N elementos, encontre e escreva o maior e o menor elemento e suas respectivas
#posições no vetor.
v = [9,2,3,4,5,6,1]

maior = 0
menor = 0

for i in range(len(v)):
    b = v[i]
    
    if i == 0:
        maior = v[i]
        menor = v[i]
    else:
        if v[i] > maior:
                maior = v[i]

        if v[i] < menor:
                menor = v[i]

print(f' O maior dos números digitados é {maior} e o menor é {menor}')

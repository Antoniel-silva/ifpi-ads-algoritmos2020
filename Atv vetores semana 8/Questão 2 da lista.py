#2. Leia um vetor A com N elementos, verifique e escreva se existem ou não elementos iguais no vetor.

#entradas
a = [3,1,7,4,2,8,5,3,1,7,9]
b = []
for i in a:
    if i not in b:
        b.append(i)

    else:
        print(f' O numero {i} está repetido nessa lista!')


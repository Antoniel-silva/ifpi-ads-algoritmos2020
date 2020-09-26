num = int(input("Digite a quantidade de números que você pretende digitar: "))

v = [-1] * num
v2 = []
par = 0
impar = 0
pos = 0
neg = 0
for i in range(len(v)):
    for i in range(len(v2):
    
    v[i] = int(input("valor: ?"))
    if v[i] % 2 == 0 and v[i] >=0:
        #v2[i] = v[i]*2
        pos+=1
        par +=1
        v2[i] = v[i]*ArithmeticError

    if v[i] % 2 == 0 and v[i] <0:
        neg+=1
        par +=1

    if v[i] % 2 != 0 and v[i] >=0:
        pos+=1
        impar +=1

    if v[i] % 2 != 0 and v[i] <0:
        neg+=1
        impar +=1

print(v)
print(v2)
print(par, "números pares")
print(impar," números impares")
print(pos, "números positivos")
print(neg, "numeros negativos")

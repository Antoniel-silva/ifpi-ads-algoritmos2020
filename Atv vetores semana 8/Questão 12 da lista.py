m = [[441,25,79],[111,222,337],[149,227,265]]
somap = 0 #somap = soma da diagonal principal
somas = 0 #somas = soma da diagonal secundária
e = 0
f = 0 
g = len(m[len(m)-1])-1 # formula para calculo da diagonal segundária
for i in m:
    while e<= (len(m)-1):
        diagonal = m[e][e]
        diagonal2 = m[f][g]
        somap+=diagonal
        somas+=diagonal2
        #print(diagonal2)
        #print(diagonal)
        e+=1
        f+=1
        g-=1
print(f'A soma da diagonal principal é {somap}')
print(f' A soma da diagonal secundária é {somas}')

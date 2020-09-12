#Uri 1024

n = int(input("Digite a quantidade de palavras: "))


for i in range(1, n+1):
    palavra = ""
    
    a = str(input("Digite a palavra: "))
    for b in a:
         
        ordletra = ord(b)
        if (ordletra > 64 and ordletra <= 90) or (ordletra > 96 and ordletra <= 122):
            orddesloca = ordletra + 3
            palavracrip = chr(orddesloca)
            palavra += palavracrip

        else:
            orddesloca = ordletra + 0
            palavracrip = chr(orddesloca)
            palavra += palavracrip
            
    print(palavra)

v = palavra[::-1]
print("A palavra invertida é: ",v)
    

    

print("Acabou")

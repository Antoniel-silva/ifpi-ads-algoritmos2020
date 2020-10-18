#Questão hack hanc - Camel case
palavra = str(input("Digite uma palavra: "))
contador = 1
for i in palavra:
    ordpalavra = ord(i)
    if ordpalavra >= 65 and ordpalavra <= 90:
        contador += 1

print(f'Essa frase tem {contador} palvras!')
        

print("Acabou")

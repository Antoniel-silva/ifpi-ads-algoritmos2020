#3. Leia uma letra e verifique se a letra digitada é vogal ou consoante.

#entradas
letra = str(input("Digite uma letra: "))

#processamento
if letra == 'A' or letra =='E' or letra =='I' or letra =='O' or letra =='U' or letra =='a' or letra =='e' or letra =='i' or letra =='o' or letra =='u':
	print("È vogal.")


else:
	print("É consoante!")

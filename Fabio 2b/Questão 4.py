#4. Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
#o "Aprovado", se a média alcançada for maior ou igual a sete;
#o "Reprovado", se a média for menor do que sete;
#o "Aprovado com Distinção", se a média for igual a dez.

#entradas
nota1 = int(input("Digite uma nota: "))
nota2 = int(input("Digite uma nota: "))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
	print("Aprovado")

elif media < 7:
	print("Reprovado")

else:
	print("Aprovado com Distinção.")

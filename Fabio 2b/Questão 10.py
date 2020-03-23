#10. Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a
#sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento Conceito
#Entre 9.0 e 10.0 A
#Entre 7.5 e 9.0 B
#Entre 6.0 e 7.5 C
#Entre 4.0 e 6.0 D
#Entre 4.0 e zero E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
#“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

#entradas
nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
	print(f'A 1° nota foi: {nota1} e a 2° nota foi {nota2}')
	print(f'A média das notas foi: {media}')
	print("O conceito da sua nota foi (A)")
	print("“APROVADO”")


elif media >= 7.5 and media < 9:
	print(f'A 1° nota foi: {nota1} e a 2° nota foi {nota2}')
	print(f'A média das notas foi: {media}')
	print("O conceito da sua nota foi (B)")
	print("“APROVADO”")


elif media >= 6 and media < 7.5:
	print(f'A 1° nota foi: {nota1} e a 2° nota foi {nota2}')
	print(f'A média das notas foi: {media}')
	print("O conceito da sua nota foi (C)")
	print("“APROVADO”")


elif media >= 4 and media < 6:
	print(f'A 1° nota foi: {nota1} e a 2° nota foi {nota2}')
	print(f'A média das notas foi: {media}')
	print("O conceito da sua nota foi (D)")
	print("“REPROVADO”")


elif media >= 0 and media < 4:
	print(f'A 1° nota foi: {nota1} e a 2° nota foi {nota2}')
	print(f'A média das notas foi: {media}')
	print("O conceito da sua nota foi (E)")
	print("“REPROVADO”")
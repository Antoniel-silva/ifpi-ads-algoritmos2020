#13. Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a) "Telefonou para a vítima ?"
#b) "Esteve no local do crime ?"
#c) "Mora perto da vítima ?"
#d) "Devia para a vítima ?"
#e) "Já trabalhou com a vítima ?"
#O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
#responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
#"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

#entradas

contador = 0
pergunta1 = str(input("Telefonou para a vítima ? "))
pergunta2 = str(input("Esteve no local do crime ? "))
pergunta3 = str(input("Mora perto da vítima ? "))
pergunta4 = str(input("Devia para a vítima ? "))
pergunta5 = str(input("Já trabalhou com a vítima ? "))

if pergunta1 == "s" and pergunta2 == "s" and pergunta3 == "s" and pergunta4 == "s" and pergunta5 == "s":
	print("Assassino")

elif pergunta1 == "s" and pergunta2 == "s":
        print("Suspeita")


elif pergunta2 == "s" and pergunta3 == "s":
        print("Suspeita")

elif pergunta1 == "s" and pergunta3 == "s":
        print("Suspeita")

elif pergunta3 == "s" and pergunta4 == "s":
        print("Suspeita")

elif pergunta4 == "s" and pergunta5 == "s":
        print("Suspeita")

elif pergunta3 == "s" and pergunta5 == "s":
        print("Suspeita")

elif pergunta1 == "s" and pergunta5 == "s":
        print("Suspeita")

elif pergunta1 == "s" and pergunta4 == "s":
        print("Suspeita")

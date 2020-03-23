#8. Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva
#sua idade exata (em anos).

#entradas
dia_atual = int(input("Digite a dia atual: "))
mes_atual = int(input("Digite o mes ztual: "))
ano_atual = int(input("Digite o ano atual: "))

dia_nasc = int(input("Digite o dia do nascimento"))
mes_nasc = int(input("Digite o mês do nascimento"))
ano_nasc = int(input("Digite o ano do nascimento"))



#processamento

idade = ano_atual - ano_nasc

#saida
print(f'A sua idade é {idade} anos.')

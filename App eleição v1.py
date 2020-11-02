import os

def main():

    partidos = []
    vereadores = []
    vagas = 29

    menu = '<<<<<<< APP ELEICÔES Teresina>>>>>>>\n'
    menu += '1 - Total de partidos\n'
    menu+= '2 - Listar todos os candidatos e seus dados\n'
    menu += '3 - Total de votos\n'
    menu += '4 - Quoeficiente eleitoral QE\n'
    menu += '5 - Eleitos\n'
    menu += '6 - Listar todos os partidos\n'
    menu+= '0 - Sair\n'
    menu += '----------------------------------\n'
    menu += 'Digite sua opcão: \n'

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            a = importar_partidos("partidos_coligacoes_the_2012.csv")
            b = importar_vereadores("candidatos_e_votos_vereador_THE_2012.csv")
            print("O total de partidos é: ",len(a),"partidos e",len(b), "candidatos.")

        elif opcao == 2:
             print(mostrar_todos(vereadores))
            

        elif opcao == 3:
            print("O total de votos nessa eleição foi de: ",total_votos(vereadores), "votos.")

        elif opcao == 4:
            a = total_votos(vereadores)
            b = a // vagas
            
            print("O coeficiente eleitoral dessa eleição é: ", b)

        elif opcao == 5:
            print()

        elif opcao == 6:
            mostrar_partidos(partidos)
            

        else:
            print("Opcão inválida! Digite uma opcão válida")

        input("Enter para continuar...")
        os.system('cls')

        opcao = int(input(menu))



def importar_partidos(arquivo):
    
    arquivo = open(arquivo)

    registros = []
    for i in arquivo.readlines():
        registros.append(i.strip())

    return registros


def importar_vereadores(arquivo):
    
    arquivo = open(arquivo)

    registros = []
    for i in arquivo.readlines():
        registros.append(i.strip().split(';'))

    return registros



def mostrar_todos(vereador):
    
    arquivo = open("candidatos_e_votos_vereador_THE_2012.csv")
    
    for a in arquivo.readlines():
        registro = {}
        b = a.split(";")
        registro['nome'] = b[0]
        registro['numero'] = b[1]
        registro['partido'] = b[2]
        registro['coligacao'] = b[3]
        registro['total_votos'] = int(b[4])
        vereador.append(registro)
        print(registro)
        
def total_votos(vereadores):
    soma = 0
    arquivo = open("candidatos_e_votos_vereador_THE_2012.csv")
    
    for a in arquivo.readlines():
        b = a.split(";")
        c = int(b[4])
        soma = soma + c

    return soma


def mostrar_partidos(partidos):
    
    arquivo = open("partidos_coligacoes_the_2012.csv")

    for a in arquivo:
        registro = {}
        
        #print(a)
        registro['Coligação'] = a
        registro['Total de votos'] = 0
        registro['Qtd_vagas'] = 0
        registro['Votos_sobra_total'] = 0

        print(registro)
        
        

main()

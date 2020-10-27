def main():

    arquivo = []
    menu = tela_inicial()
    opcao = int(input(menu))
    

    while opcao != 0:
        if opcao == 1:
            listacel = cadastrar()
            arquivo.append(listacel)
            
            

        elif opcao == 2:
            lista = listar(arquivo)
            print(lista)

        elif opcao == 3:
            print("Voce selecionou a busca por celulares cadastrados!")
            a = str(input("Digite uma palavra chave: "))
            for a in arquivo[0]["marca"] == True:
                print(a)
                

                
            

        else:
            print("""
Essa opção não é válida!
________________________

""")
        input("Precione enter e continue a execução. . . ")

        opcao = int(input(menu))
    

def tela_inicial():
    menu = "<<<<<<<<<< App Celular >>>>>>>>>>\n"
    print()
    menu += '1 - Cadastre um novo modelo de celular\n'
    menu += '2 - Lista todos os modelos cadastrados\n'
    menu += '3 - Fazer busca nos celulares cadastrados\n'
    menu += '0 - para sair\n'
    
    menu += 'Digite sua opção: '

    return menu

def cadastrar():
    listacell = {}
    print()
    print("Voce selecionou cadastro de novos celulares!")
    print()
    marca = str(input("Digite a fabricante do dispositivo: "))
    modelo = str(input("Digite o modelo do dispositivo: "))
    tela = str(input("Digite o tamaho da tela do dispositivo: "))
    valor = float(input("Digite quanto custa o dispositivo: "))

    listacell["Marca"] = marca
    listacell["Modelo"] = modelo
    listacell["Tela"] = tela
    listacell["Valor"] = valor

    #arquivo.append(listacell)
    print("Dados gravados com sucesso!")
    return listacell

def listar(tamanho):
    print()
    print("Foram localizados", len(tamanho), "cadastros!")
    print()
    print("<<<<<Mostrando lista de dispositivos cadastrados>>>>>")
    print()
    for i in tamanho:
        print(i)
        print()
    

    
main()

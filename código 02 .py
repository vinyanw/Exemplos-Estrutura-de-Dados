def adicionar(lista):
    nome=str(input("Adicione um nome na lista: "))

    if(nome in lista):
        print('Esse nome já está registrado!')
    else:   
        lista.append(nome)

def verificar(lista,elemento):
    for item in lista:
        if item == elemento:
            print(f'{elemento} está na lista.')
            return True
    
    print(f'{elemento} não está na lista.')
    return False

def menu():
    print("# LISTA DE PRESENÇA #")
    print("1- Adicionar nome")
    print("2- Remover nome do sistema")
    print("3- Verificar se nome está no sistema")
    print('4- Ver lista de nomes')
    print('0-sair')
    opc=input('Escolha uma opção: ')
    return opc

sistema=list()

while True:
    opc=menu()

    if(opc=="1"):
        adicionar(sistema)

    elif(opc=="2"):
        nome=str(input("Remova um nome da lista: "))
        if(verificar(sistema,nome)==True):
            sistema.remove(nome)
            print('Agora o nome foi removido!')
        
    elif(opc=="3"):
        nome=str(input("Qual nome deseja verificar: "))
        verificar(sistema, nome)

    elif(opc=="4"):
        nome_ordenados = sorted(sistema)

        print("\nLista de frequência:")
        for i in range(len(nome_ordenados)):
            nome = nome_ordenados[i]
            print(f"{i + 1}. {nome}")


    elif(opc=="0"):
        break

    else:
        print('Opção inválida.')
    print(' ')
       
print('Fim do programa')

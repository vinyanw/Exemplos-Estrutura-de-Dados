import time

lista_contatos = []

def adicionar_contato():
    nome = input("\nNome: ").title()
    telefone = input("Número: ")
    lista_contatos.append({'nome': nome, 'telefone': telefone})
    print("\nAdicionando Contato...")
    time.sleep(2)
    print(f"\nContato '{nome}' adicionado com sucesso!")
    
def exibir_contatos():
    if not lista_contatos:
        print("\nA lista de contatos está vazia.")
    else:
        contatos_ordenados = sorted(lista_contatos, key=lambda x: x['nome'])

        print("\nLista de contatos:")
        for i in range(len(contatos_ordenados)):
            contato = contatos_ordenados[i]
            print(f"{i + 1}. {contato['nome']}, Número: {contato['telefone']}")

def remover_contato():
    if not lista_contatos:
        print("\nLista Vazia. Não há contatos para remover.")
    else:
        exibir_contatos()
        nome = input("\nDigite o nome do contato que deseja remover: ").title()
        for contato in lista_contatos:
            if contato['nome'] == nome:
                lista_contatos.remove(contato)
                print("\nRemovendo Contato...")
                time.sleep(2)
                print(f"\nContato '{nome}' removido com sucesso!")
                return 
        print(f"\nContato com o nome '{nome}' não encontrado.")

def modificar_contato():
    if not lista_contatos:
        print("\nA lista de contatos está vazia.")
        return

    exibir_contatos()
    nome = input("\nDigite o nome do contato que deseja modificar: ").title()
    for contato in lista_contatos:
        if contato['nome'] == nome:
            print("\n1.DIGITE para MUDAR o telefone ou nome.\n2.Aperte ENTER para Manter os dados\n")
            contato['nome'] = input("Nome: ").title() or contato['nome']
            contato['telefone'] = input("Número: ") or contato['telefone']
            print("\nModificando Contato...")
            time.sleep(2)
            print("\nContato atualizado com sucesso!")
            return

    print("\nContato não encontrado.")

def menu():
    
    while True:
        print("\n===== Lista de Contatos =====")
        print("1. Adicionar Contato")
        print("2. Exibir Contatos")
        print("3. Remover contato")
        print("4. Modificar contato")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            adicionar_contato()
            continue
        elif opcao == "2":
            exibir_contatos()
            continue
        elif opcao== "3":
            remover_contato()
            continue
        elif opcao== "4":
            modificar_contato()
            continue
        elif opcao == "5":
            print("\nPrograma encerrado.")
            exit()
        else:
            print("\nOpção inválida! Tente novamente.\n")

menu()

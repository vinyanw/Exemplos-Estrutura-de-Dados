from collections import deque
import time

pedidos=deque()

def preparando_pedido(pedidos,a):
    if(len(pedidos)==0):
        print('Não há pedidos.')
    else:
        print(f'#{a.pop(0)} - {pedidos.popleft()}')
        print('Preparando pedido...')
        time.sleep(5)
        print("Pedido pronto!")

def menu():
    print("#### PEDIDOS ####")
    print("1- Adicionar pedido")
    print("2- Próximo pedido a ser preparado")
    print("3- Visualizar os pedidos na fila")
    print('0- Sair')
    opc=input('Escolha uma opção: ')
    return opc
a=[]
b=1
while True:
    print(' ') 
    opc=menu()
    
    if(opc=='1'):
        item= input('Pedido: ')
        pedidos.append(item)
        a.append(b)
        b+=1
    
    elif(opc=='2'):
        preparando_pedido(pedidos,a)

    elif(opc=='3'):
        if(len(pedidos)==0):
            print('Não há pedidos.')
        else:
            for i in range(len(pedidos)):
                print(f'#{a[i]} - {pedidos[i]}')

    elif(opc=='0'): break

    else:
        print('Opção inválida')

print('Fim do programa')




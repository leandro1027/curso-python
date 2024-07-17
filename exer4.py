"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []
while True:
    print("Escolha uma opção: ")
    opcao = input("[I]nserir [a]pagar [l]istar: ")

    if opcao == 'i':
        os.system('cls')
        valor = input("Digite o item: ")
        lista.append(valor)
    elif opcao == 'a':
        print('a')
        indice_str = (input("Digite o indice que deseja apagar: "))
    
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
                print('Por favor digite número int.')
        except IndexError:
                print('Índice não existe na lista')
        except Exception:
                print('Erro desconhecido')

    elif opcao == 'l': 
        print('l')
        os.system('cls')

        if len(lista) == 0:
            print("Nada a mostrar, lista vazia")
        
        for i, valor in enumerate(lista):
             print(i, valor)

    else:
        print("Por favor escolha alguma das opcôes!")
    

       
             

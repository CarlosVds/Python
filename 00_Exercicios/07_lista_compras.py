import os
print('*****LISTA DE COMPRAS*****\n')

print("Faça sua lista de compras\n")

print('1-Inserir')
print('2-Apagar')
print('3-Listar')
print('4-sair\n')

inserir = "1"
apagar = "2"
listar = "3"
sair = "4"

lista = []


while True:
    
    try: 
        usuario = input('Digite uma das opções: ')
        if usuario in (inserir, apagar, listar, sair):
            ...
        else:
            print('Opção inválida.')
            
                
        if usuario == inserir:
            os.system('cls')
            print('Para finalizar a compra, digite o número da opção SAIR')
            while True:   
                digito = input('Produto: ')
                lista.append(digito)
                if digito == sair:
                    lista.pop()
                    print('Compra finalizada.')
                    break
                    
        if usuario == apagar:
            escolherIndice = int(input('Escolha um indice: '))
            del lista[escolherIndice]
    
                        
        if usuario == listar and lista != '':
            os.system('cls')
            print('*****Item de sua lista.*****')
            for indice, produto in enumerate(lista):
                print(indice, produto)         
        else:
            print('Lista vazia.')         
                
        if usuario == sair:
            print('Sistema finalizado.')
            break
        
    except ValueError:
        print('Somente números inteiros.')
    except IndexError:
        print('Opção inexistente.')
       

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
    usuario = input('Digite uma das opções: ')   
    while True:
        if usuario == inserir:
            digito = input()
            lista.append(digito)
        elif usuario == sair:
            break    

    if usuario == apagar:
        escolherIndece = int(input('Escolha um indece: '))
        del lista[escolherIndece]
                
    if usuario == listar:
        for indice, produto in enumerate(lista):
            print(indice, produto)
            
    if usuario == sair:
        break
       

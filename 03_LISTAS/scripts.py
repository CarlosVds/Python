# lista_a = ['Carlos', 'Enzo']
# lista_b = lista_a.copy()
# # lista.append('Erika')
# # lista.insert(3, True)
# # lista.pop(3)
# # del lista[3]
# # lista.clear()
# # lista2 = ['Marcella']
# # lista.extend(lista2)

# lista_a[1] = 'Lista A, alterada'
# lista_b.append('Lista A copiada')
# print(lista_a)
# print(lista_b)

salas = [
    ['Maria ', 'Elena'],
    ['Elaine'],
    ['Carlos', 'Enzo', 'Erika']
]

number = 1

for nomes in salas:
    print("*********************")
    print(f'Sala {number}')
    number += 1
    
    for i, sala in enumerate(nomes):
        print(i + 1, sala)
        
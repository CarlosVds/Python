# table = 2

# list = [
#     f'{table} X {number} = {table * number} ' 
#     for number in range(11)
# ]

# print(*list, sep='\n')

# person = {
#     'name':'Carlos',
#     'surname':'Santos'
# }

# data_person = {
#     'age':99,
#     'adress':'Rua Teresa'
# }

# # data_complete = {**person, **data_person}

# # print(data_complete)
# def show_data(*args, **kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} {value}')

# show_data(**person, **data_person)

# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]

# new_product = [
#     {**product, 'preco':product['preco'] * 1.05}
#     if product['preco'] > 20 else product
#     for product in produtos 
#     if product['preco'] > 20
# ]

# print(*new_product, sep='\n')  

list = [
    [[x,y] for y in 'Carlos']
    for x in range(3) 
]

print(list)


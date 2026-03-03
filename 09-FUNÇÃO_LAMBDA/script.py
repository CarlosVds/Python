list = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def order_list(itens):
#     return itens['nome']

# list.sort(key=order_list)

# for itens in list:
#     print(itens)

# def show(itens):
#     for show in itens:
#         print(show)
#     print()
    
# l1 = sorted(list, key=lambda itens:itens['nome'])
# l2 = sorted(list, key=lambda itens:itens['sobrenome'])

# show(l1)
# show(l2)

def execute(fuction, *args):
    return fuction(*args)

def sum(x, y):
    return x + y

print(
    execute(
        lambda x , y: x + y,
        2, 3
    )
)
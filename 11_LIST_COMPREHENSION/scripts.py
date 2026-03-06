# table = 2

# list = [
#     f'{table} X {number} = {table * number} ' 
#     for number in range(11)
# ]

# print(*list, sep='\n')

person = {
    'name':'Carlos',
    'surname':'Santos'
}

data_person = {
    'age':99,
    'adress':'Rua Teresa'
}

# data_complete = {**person, **data_person}

# print(data_complete)
def show_data(*args, **kwargs):
    for key, value in kwargs.items():
        print(f'{key} {value}')

show_data(**person, **data_person)
  
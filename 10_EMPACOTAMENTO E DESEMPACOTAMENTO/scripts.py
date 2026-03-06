person = {
    'name':'Carlos',
    'surname': 'Santos'
}

data_person ={
    'age': 99,
    'height': 1.65
}

def packaging(**Kwargs):
    for key, value in Kwargs.items():
        print (f'{key}: {value}')
    

print(packaging(**person, **data_person))


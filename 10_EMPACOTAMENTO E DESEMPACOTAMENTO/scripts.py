person = {
    'name':'Carlos',
    'surname': 'Santos'
}

data_person ={
    'age': 99,
    'height': 1.65
}

complete_data = {**person, **data_person}

print(complete_data)
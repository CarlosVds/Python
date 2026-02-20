# def soma(*args):
#     total = 1
#     for multle in args:
#         total *= multle
#     return total

# print(soma(2,3,4))
# def parImpar(x):
    
#     if x % 2 == 0:
#         return f'Número {x} é PAR'
#     else:
#         return f'Número {x} é IMPAR'

# print(parImpar(832))

# def multiplier(multiplier):
#     def multiply(number):
#         return number * multiplier
#     return multiply 

# duplicate = multiplier(2)   
# triple = multiplier(3)   
# quadruple = multiplier(4)

# print(duplicate(2))   
# print(triple(2))   
# print(quadruple(2)) 

# person = {
#     'name': 'Carlos',
#     'surname': 'Santos'
# }

# print(len(person))
# print(list(person.keys()))
# print(list(person.items()))
# print(list(person.items()))

# for values in person.values():
#     print(values)

# for items in person.items():
#     print(items)

# import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'li':[1,2,3]
} 

d2 = d1.copy()

d1['c1'] = 1000

d2['li'][1] = 9999

print(d1)
print(d2)
# def soma(*args):
#     total = 1
    
#     for i in args:
#         total *= i
#     return total

# print(soma(2,3))

# def parImpar(x):
    
#     if x % 2 == 0:
#         return f'Número {x} é PAR'
#     else:
#         return f'Número {x} é IMPAR'

# print(parImpar(832))

def multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply 

duplicate = multiplier(2)   
triple = multiplier(3)   
quadruple = multiplier(4)

print(duplicate(2))   
print(triple(2))   
print(quadruple(2))   
def soma(*args):
    total = 1
    
    for i in args:
        total *= i
    return total

print(soma(2,3))

def parImpar(x):
    
    if x % 2 == 0:
        return f'Número {x} é PAR'
    else:
        return f'Número {x} é IMPAR'

print(parImpar(832))    
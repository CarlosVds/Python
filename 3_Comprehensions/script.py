numeros = range(10)

list_numeros = []

for n in numeros:
    list_numeros.append(n ** 2)

print(f'Lista usando FOR:\n{list_numeros}')

print("*" * 35)

quadrados = [x ** 2 for x in range(10)]

print(f'Lista usando COMPREHENSIONS:\n{quadrados}')

print("*" * 35)

numeros_pares = [x for x in range(20) if x % 2 == 0]

print(f'Somemte números pares:\n{numeros_pares}')

print("*" * 35)

numero_dic = {x : (x ** 2) for x in range(10)}

print(f'Dicionário:\n{numero_dic}')

print("*" * 35)

numeros_duplicados = {x ** 2 for x in [1,2,2,3,3,4]}

print(f'Numeros duplicados:\n{sorted(numeros_duplicados)}')

print("*" * 35)

gen = tuple(x ** 2 for x in range(6))

print(f'Generetor:\n{gen}')


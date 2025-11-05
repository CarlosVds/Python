dobro = lambda x: x ** 2

digito = 97

print(f'O dobro do numero {digito} é {dobro(digito)}')

print('*' * 55)

numero = [1,2,3,4,5,6]

quadrados = list(map(lambda x: x ** 2, numero))

print(f'Calculando o quadrado dos números: {numero}')
print(f'Quadrado dos números acima é: {quadrados}')

print('*' * 55)

quadrados_pares = list(filter(lambda x: x % 2 == 0, quadrados))

print(f'Lista numerica: {quadrados}')
print(f'Numeros PARES da lista acima: {quadrados_pares}')

print('*' * 55)


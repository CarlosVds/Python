# frutas = ['maça','banana','abacate']

# print('LISTA')
# for fruta in frutas:
#     print(fruta)
    
# print(30 * '*')    

# print('TUPLA')
# frutas = ('maça','banana','abacate')

# for fruta in frutas:
#     print(fruta)
    
# print(30 * '*')    

# print('DICIONÁRIO')
# frutas = {'maça':'vermelha','banana':'amarela','abacate': 'verde'}

# for chave, valor in frutas.items():
#     print(chave,":",valor)
    
# print(30 * '*')    

# print('RANGE')

# for numero in range(6):
#     print(numero)

# print(30 * '*')    

# print('WHILE')

# cont = 0

# while cont <= 10:
#     print(cont)
#     cont += 1  
    
# print(30 * '*')    

# print('FOR')

# numeros = [23,45,7,88,90,7543]

# for n in numeros:
#     if n % 2 == 1:
#         print(f'{n} é IMPAR') 

# print('FOR')

# nomes = ['Carlos','Enzo','Cleide','Alcino']

# for nome in nomes:
#     if nome.startswith('C'):
#         print(f'Nomes encontrado com C: {nome}')

# print(40 * '*') 

# print('FOR')

# nomes = {'Carlos':44,'Enzo': 11,'Cleide': 17,'Alcino': 64}

# for nome, idade in nomes.items():
#     if idade < 18:
#         print(f'Nomes de pessoa menores de idade: {nome} {idade} anos')

# print(40 * '*')

numeros = [1,2,3,4,5,6,7,8,9,10]
print('Encontra o número 5\n')

for numero in numeros:
    if numero == 5:
        print(f'Número encontrado: {numero}')
        continue
    print(f'Verificando...{numero}')
                                           
print(40 * '*')

numeros = [1,2,3,4,5,6,7,8,9,10]
print('Encontra o número 5\n')

for numero in numeros:
    if numero == 5:
        print(f'Número encontrado: {numero}\n')
        break
    print(f'Verificando...{numero}')                                           
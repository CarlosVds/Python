import random, math
import utilitarios

raizQuadrada = math.sqrt(25)

print(f'A raiz quadrada de 25: {raizQuadrada}\n')

print('*' * 35)

aleatorio = random.randint(1, 100)

if aleatorio % 2 == 0:
    print(f'Número {aleatorio} é PAR')
else:
    print(f'Número {aleatorio} é IMPAR ')
    
print('*' * 35)

nomeAleatorio = random.choice(['Carlos','Enzo','Erika'])

print(nomeAleatorio)

print('*' * 35)

print(f'{utilitarios.saudacao('Carlos')} falou que o valor do PI é {utilitarios.PI}')
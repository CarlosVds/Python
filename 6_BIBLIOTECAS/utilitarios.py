import math
import random

PI = 1314159 

def saudacao(nome):
    return f'Olá tudo bem, {nome}'

def raizQuadrada(numeroInt):
    print(f'A raiz quadrada de {numeroInt}: {int(math.sqrt(numeroInt))}\n')
    print("*" * 50)
    
def parImpar()    :
    print("Execute o modulo parImpar para saber se o número aleatório é PAR ou IMPAR: ")
    aleatorio = random.randint(1, 1000)
    
    if aleatorio % 2 == 0:
        print(f"\nNúmero digitado foi {aleatorio} é PAR\n")
    else:
        print(f"\nNúmero digitado foi {aleatorio} é IMPAR\n")
    print("*" * 50)
    
def nomeEscolhidoAleoatorio():
    print('Lista de nomes: [Carlos, Enzo, Erika]')
    print('Use o modulo nomeEscolhidoAleoatorio para gerar nomes aleatórios.\n')
    lista = random.choices(['Carlos','Enzo','Erika'])
    print(lista)                
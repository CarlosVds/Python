def saudacao():
    print('Hello, World!!!')

saudacao()

print('*' * 35)

def soma(a, b):
    return a + b

print(f'A soma de 10 + 5 = {soma(10, 5)}')

print('*' * 35)

def nomeCompleto(nome, sobrenome, idade = 99):
    return (f'{nome} {sobrenome}, idade: {idade}')    

print(f'Meu nome completo: {nomeCompleto('Carlos','Santos')}')
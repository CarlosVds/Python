# def saudacao():
#     print('Hello, World!!!')

# saudacao()

# print('*' * 35)

# def soma(a, b):
#     return a + b

# print(f'A soma de 10 + 5 = {soma(10, 5)}')

# print('*' * 35)

# def nomeCompleto(nome, sobrenome, idade = 99):
#     return (f'{nome} {sobrenome}, idade: {idade}')    

# print(f'Nome completo: {nomeCompleto('Carlos','Santos')}')

# print('*' * 35)

# def semParametro(*args):
    
#     total = 0
    
#     for numero in args:
#         total += numero
        
#     return total
        
# print(semParametro(2,4,6,8,10,4))   

# print('*' * 35)

def exibe_info_pessoa(**kwargs):
    
    print('\nInformação da pessoa:\n')
    
    for chave, valor in kwargs.items():
        print(f'- {chave}: {valor}')     

exibe_info_pessoa(nome = 'Carlos', profissao = 'Desenvolvedor')
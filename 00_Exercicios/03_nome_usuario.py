primeiroNome = input('Digite seu primeiro nome: ')

if len(primeiroNome) <= 4:
    print(f'Seu nome é curto, só tem {len(primeiroNome)} letras')
elif len(primeiroNome) >= 5 and len(primeiroNome) <= 6:
     print(f'Seu nome é normal')
else:
    print(f'Seu nome é muito grande, tem {len(primeiroNome)} letras')        
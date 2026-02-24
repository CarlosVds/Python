perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    
    for indice, opcao in enumerate(opcoes):
        print(f'{indice}) {opcao}')
    
    try:
        escolha = input('Escolha uma opção: ')
        
        acertou = False
        qtd_opcoes = len(opcoes) 
        escolha_int = int(escolha)    

        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

        if acertou:
            print('Acertou👍')
        else:
            print('Errou ❌')
    except:
        print('Somente os números da opções')
        print('Errou')            
  

   
    
try:
    tempo1 = 'manhã'
    tempo2 = 'tarde'
    tempo3 = 'noite'
    
    print(f'Que horas são? ')
    
    horas = input()
    
    saudacaoHoras = int(horas)
    
    if saudacaoHoras >= 0 and saudacaoHoras <= 11:
        print(f'São {horas} horas da {tempo1}, Bom dia.')
    elif saudacaoHoras > 11 and saudacaoHoras <= 17:
        print(f'São {horas} horas, Boa {tempo2}.')
    else:
        print(f'São {horas} horas, Boa {tempo3}.')       
except:
    print('Somente números inteiros')        
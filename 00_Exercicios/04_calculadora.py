print('*****CALCULADORA SIMPLES*****\n')

print('1-SOMA')
print('2-SUBTRAÇÃO')
print('3-MULTIPLICAÇÃO')
print('4-SUBTRAÇÃO')
print('5-Sair\n')

soma = '1'
subtracao = '2'
multiplicao = '3'
divisao = '4'
sair = '5'


while True:
    
    operacao = input('Escolha uma operação: ')
    print()
    
    if operacao == '1':
       print(f'Você escolheu a operação de SOMAR \n')
    elif operacao == '2':
        print(f'Você escolheu a operação de SUBTRAÇÃO \n')
    elif operacao == '3':
        print(f'Você escolheu a operação de MULTIPLICAÇÃO \n')
    elif operacao == '4':
        print(f'Você escolheu a operação de DIVISÃO \n')
    elif operacao == '5':
        print(f'Opção SAIR, Calculadora encerrada. \n')
        break
    else:
        print('Opção inválida')
        continue
            
   
    try:
        digito_1 = input('Digite primeiro valor: ')
        digito_2 = input('Digite segundo valor: ')
        print()
    
        calcular_1 = float(digito_1)
        calcular_2 = float(digito_2)
        
        if operacao == '1':        
            resultado = calcular_1 + calcular_2
            print(f'A soma entre {digito_1} e {digito_2}: {resultado:.2f}\n')
        elif operacao == '2':
            resultado = calcular_1 - calcular_2
            print(f'A subtração entre {digito_1} e {digito_2}: {resultado:.2f}\n')   
        elif operacao == '3':
            resultado = calcular_1 * calcular_2
            print(f'A multiplição entre {digito_1} e {digito_2}: {resultado:.2f}\n')   
        else:
            resultado = calcular_1 / calcular_2
            print(f'A divisão entre {digito_1} e {digito_2}: {resultado:.2f}\n')
        
    except:
        print('Somente números')        
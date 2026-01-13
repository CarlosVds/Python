digitNumber = input('Digite um número: ')

try:
    numberDigit = int(digitNumber) 
    if numberDigit % 2 == 0:
        print(f'Número digitado foi {numberDigit}, é PAR')
    else:
        print(f'Número digitado foi {numberDigit}, é IMPAR')
except:
    print('Somente números inteiros')        
      
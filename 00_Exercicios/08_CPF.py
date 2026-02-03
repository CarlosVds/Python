number = range(9)
cpf = '74682489070'

regresso = 10
soma = 0

for i in number:
    soma += int(cpf[i]) * regresso
    regresso -= 1

valorTotal = soma * 10

resto = valorTotal % 11

digito = 0

if resto > 9:
    digito += 0
else:
    digito += resto   

print(digito)

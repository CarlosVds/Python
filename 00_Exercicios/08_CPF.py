# cpf = '74682489070'
cpf = '36275927003'
nove_digito = cpf[:9]
regresso = 10
resultado = 0

for digito in nove_digito:
    resultado += int(digito) * regresso
    regresso -= 1

print(resultado)    

primeiroDigito = resultado * 10 % 11

print(primeiroDigito)

digito_1 = primeiroDigito if primeiroDigito <= 9 else 0

print(digito)
  
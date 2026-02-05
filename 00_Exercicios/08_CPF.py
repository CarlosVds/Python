cpf_digitado = '30190699809'

nove_digito = cpf_digitado[:9]
regresso_1 = 10
resultado_1 = 0

for digito in nove_digito:
    resultado_1 += int(digito) * regresso_1
    regresso_1 -= 1  

primeiro_digito = (resultado_1 * 10) % 11

digito_1 = primeiro_digito if primeiro_digito <= 9 else 0

dez_digito = cpf_digitado[:10]
regresso_2 = 11
resultado_2 = 0

for digito in dez_digito:
    resultado_2 += int(digito) * regresso_2
    regresso_2 -= 1   

segundo_digito = (resultado_2 * 10) % 11

digito_2 = segundo_digito if segundo_digito <= 9 else 0

cpf_calculado = f'{nove_digito}{digito_1}{digito_2}'

if cpf_calculado == cpf_digitado:
    print(f'CPF digitado é válido.')
else:
    print('CPF digitado é inválido.')    
 
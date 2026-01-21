frase = 'Carlos Saaantoss'

i = 0

qtd_numero_apareceu_mais_vezes = 0
qtd_letra_apareceu_mais_vezes = ''

while i < len(frase):
    
    sequencia_letra = frase[i]    
    
    cont_letra_vezes_numerica = frase.count(sequencia_letra)
    
    if sequencia_letra == '':
        i += 1
        continue
    
    if qtd_numero_apareceu_mais_vezes < cont_letra_vezes_numerica:
        qtd_numero_apareceu_mais_vezes = cont_letra_vezes_numerica
        qtd_letra_apareceu_mais_vezes = sequencia_letra
    
    i += 1

print('A letra apareceu mais vezes foi'
      f' "{qtd_letra_apareceu_mais_vezes}" que apareceu'
      f' {qtd_numero_apareceu_mais_vezes}x') 
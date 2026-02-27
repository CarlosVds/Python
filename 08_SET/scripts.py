#Removing duplicates
s1 = set()

s1.add('Carlos')
s1.add(1)
s1.update(('Ola mundo', 1,2,3))
s1.discard('Ola mundo')

# print(s1)

#Useful methods

s1 = {1,2,3}
s2 = {2,3,4}

s3 = s1 | s2 #Elimina osduplicado e pega o que tem de diferente em cada variavel
s3 = s1 & s2 #Pega itens iguais em cada variavel
s3 = s1 - s2
s3 = s2 - s1 #Pega item unico na variavel
s3 = s2 ^ s1 #Pega item unico de cada variavel

print(s3)


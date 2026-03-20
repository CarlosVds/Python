# from soma import soma
# from sys import path

# print('Ola, sou o modulo principal.')

# print(soma(2,5))

# print(*path, sep='\n')

# import modulo
# import importlib

# print(modulo.name)

# for i in range(10):
#     importlib.reload(modulo)
#     print(i)

from sys import path
from Escopo.file import name_completed
from soma import soma
import modulo

print(name_completed('Carlos', 'Santos'))
print(soma(1,2))
print(modulo.name)
print(*path, sep='\n')
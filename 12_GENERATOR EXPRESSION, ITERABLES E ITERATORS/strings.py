# def gerenator(n=0, maximum=10):
#     while True:
        
#         yield n
        
#         if n >= maximum:
#             return 
        
#         n += 1
# v = 2        
# gen = gerenator()

# for n in gen:
#     print(f'{v} X {n} = {v * n}')

def gen1():
    yield 1    
    yield 2    
    yield 3    
    
def gen2():
    yield from gen1()
    yield 4    
    yield 5   
    yield 6  
     
def gen3():
    yield from gen1()
    yield 4    
    yield 5   
    yield 6   
    
gen = gen2()

for g in gen:
    print(g)    
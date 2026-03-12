try:
    a = 20
    b = 0
    
    c = 20 / 0
    
    print(2)
    
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)        
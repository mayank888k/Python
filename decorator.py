def decorator(func):                                  # A function is passed into decorator
    def inner(a,b):                                   # function{abc} passed in decorator is replaced
        print("This will execute before function")    # by inner function argument passed in inner
        if a>b :                                      # are same of func{abc here}
            z=func(a,b)
        else:                                         # function{abc} get modified some code before
            z=func(a,b)                               # some after    
        
        
        print("This will execute after function")
        return z
    return inner
@decorator                                            # how to make a function{abc} a decorator
def abc(a,b):
    print("This is actual function")
    return a
print(abc(7,9))

    
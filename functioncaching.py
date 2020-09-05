from functools import lru_cache
import time

@lru_cache(maxsize=3)                 #lru_cache decorator is used for function caching
def func(n):                           #Lru_caache will store recent 3(maxsixe) function returned
    time.sleep(n)                       #value to the cache
    print("Function called")
    return n

print("Calling Function 1st time")
print(func(3))
print("Returned Succesfully")
print(func(6))
print("Returned Succesfully")
print(func(6),"Function Not called only Return Value is printed From cache")                  
                                
#                               this one printed instantly because its returned value is stored
#                                in the cache memory so this time function is not called, only
#                                returned value is printed

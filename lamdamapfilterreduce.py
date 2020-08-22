lst=[x for x in range(10,0,-1)]
print(lst)

a=lambda a: a**3
print(a(3))

lst1=list(map(lambda x:x*2,lst))            #map func apply given fuct to
print(lst1)                                 #every value of list

lst2=list(filter(lambda x: (x%2==0),lst))   #filter function return that value from list
print(lst2)                                 #for which the function return true vale

from functools import reduce

z=reduce(lambda x,y: x+y,lst)                #x, y: x+y, [1, 2, 3, 4, 5]) 
print(z)                                          #calculates ((((1+2)+3)+4)+5).

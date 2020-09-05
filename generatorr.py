
#generator (generator is a iterable ehich generate value(that is in yeild) as we call next)
def gen(a):
    for a in range(a): 
        yield a          #yield value at run time
    yield 566

abc=gen(3)                              #generator object need to create it is not a function

print(next(abc))                     #We go to next yeild using next()
print(next(abc))
print(next(abc))
print(next(abc))

genn=(a  for a in range(10))   #generator comprehension , () are used

for i in genn:
    print(i, end=" ")

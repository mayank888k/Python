x="Mayank Kumar   "
y="is a good boy"
count=0
j=0
for i in x :
    j=j+1
    if i == "a" :
       count+=1
       print("a is at pos",j)
print(count)

a=x.find(' ')
b=x.find("ar")
print(x[a+1:b])
print(x.upper())
print(x.lower())
print(x.count("a"))
print(x.index("K"))
print(x[::-1])
print(x+y)


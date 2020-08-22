lst=[5,6,7,8,9]          #tuple is Immutable like strings
tple=(1,2,3,4)           #you cant append or remove like list
tple2=tuple(lst)
tple3=tple + tple2

print(tple3)
print(tple3[5:10])       #you can access it by index
print(tple3[::-1])
print(max(tple3))

del tple3                #You can delete whole tuple
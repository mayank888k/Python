filename=input("Enter File name to open:")
fhandle=open(filename,"r")
print(fhandle.read())       # read all the lines
fhandle.seek(0)
print()
print(fhandle.readline())   # read single line
print(fhandle.readline())   # read single line
fhandle.seek(0)
print(fhandle.readlines())  # read and return in the form of list
fhandle.seek(0)
line=0
word=0
for i in fhandle:           # i takes value of a single line
    a=i.split()
    word += len(a)
    line=line+1
print("No of lines is",line)
print("No of words is",word)
fhandle.close()




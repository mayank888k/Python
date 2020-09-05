import os

print(os.getcwd())                            #to get current working directory
os.chdir(r"C:\Users\JXX\Desktop\New folder")  #to change current working directory

print(os.getcwd())
#os.rename("kallu","asdfg")                   #to rename kallu to asdfg
print(os.listdir())

#os.mkdir("jack")                              to make directory jack
#os.makedirs(r"c/c++")                         to make directories c and in c c++
dirlist=os.listdir()

for item in dirlist:
    if item.endswith("jpg"):
        os.rename(item,item.lower())
        pass
    else:
        os.rename(item,item.upper())

print(os.listdir())
print(os.path.exists(r"C:\Users\JXX\Desktop\New folder")) #to check if path exist
print(os.path.isfile("picture 380.jpg")) #to check if file exist in cwd
#os.removedirs("ASDFG") #to remove file
print(os.listdir())

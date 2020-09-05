import time

def courotine():
    a="Mayank"
    time.sleep(3)
    print("Coroutine is strated")     

    while True:
        name=(yield)
        if name is a:
            print(a)
        else:
            print("Name not found")

coro=courotine()       #creating a generator object we cant directly call courotine
next(coro)            #to start the corotine executed till encountered while true (yeild)
 
print("function Execution stoped before while\n")
print("Execution stated after while no delay occured this time")
coro.send("Mayank")
coro.send("Rahul")
coro.close()    #closing courotine
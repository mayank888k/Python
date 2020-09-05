class father():                             #Derived class can access all the attributes and
                                            # methods of Base class
    age=45                                  #Constructor is first called of derived class
    def __init__(self,name):                #so in order to call Base class const we call it in
                                            #derived class constructor
        self.fname=name
    
class son(father):

    age=19
    def __init__(self,aname,sname):
        father.__init__(self,aname)
        self.name=sname

fa=father("Roopram")                        #Base class object thats why age=45
mayank=son("Arvindra Kumar", "Mayank")      #Derived class object age is overwrited by 19

print(fa.age)
print(f"Mayanks age is {mayank.age}")
print(f"Mayanks name is {mayank.name}")
print(f"Mayanks father namw is {mayank.fname}")
print(f"Mayanks father age is {fa.age}")
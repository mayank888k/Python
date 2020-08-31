class A():
    var="Class variable of A"
    def __init__(self):
        self.var="Constructor instance variable in A"
        self.aconsvar="Constructor instance variable of A"

class B(A):
    var="Class Variable of B"
    def __init__(self):
        super().__init__()
        self.var="Constructor instance variable in B"
        self.bconvar="Constructor instance variable of B"
        A.__init__(self)

b=B()               #first variable is checked in instace varible of B class if not found then it go
                    #to the A class and check in instance variables of it if it is not found there
print(b.var)        #then it check the class variable of B class if it is not found
                    #then it checks in class variable of Class A

#Constructor is called only of that class whose object is created so in order to access
#instace variable of Base class(A) we have to call it in constructor of Derived class(B)
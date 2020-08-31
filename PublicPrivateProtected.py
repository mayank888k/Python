class A():
    _X=10                          #Protected can be accessed inside of derived class but not
    def __init__(self):           #outside the class it tell only programmer but can be accessed      
        self._z=40                #actually
        self.__name="Mayank"      #Private can't be accessed inside of derived and outside of class

class B(A):
    Y=2
    print(A._X)
    def __init__(self):
        A.__init__(self)
        #print(self.__name)
        self.age=19

obj=B()
abj1=A()

#print(abj1.__name)
print(abj1._z)
#print(obj.__name)
print(obj._X)


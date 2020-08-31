class A():
    A=1
    def __init__(self):
        self.name="Mayank"                        #In Multiple inheritence C can access
                                                  #variables of both A and B
class B():
    B=2
    def __init__(self):
        self.age=19                             

class C(A,B):
    C=3
    def __init__(self):
        B.__init__(self)               #Constructor is called only of class whose obj is created
        A.__init__(self)               
        self.course="BTECH CSE"
    
person=C()
print(person.name,person.A)
print(person.age,person.B)
print(person.course,person.C)
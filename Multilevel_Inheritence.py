class Grandfather():
    A=1                                     #In Multilevel inheritence Father can access GrandFather
    def __init__(self):                     #son can access father so {both Grandfather and father}
        self.gfname="Late Roopram"

class Father(Grandfather):
    B=2
    def __init__(self):
        Grandfather.__init__(self)
        self.fname="Arvind Kumar"

class Me(Father):
    C=3
    def __init__(self):
        Father.__init__(self)
        self.name="Mayank Kumar"

person=Me()

print(person.name,person.A)
print(person.fname,person.B)
print(person.gfname,person.C)
    
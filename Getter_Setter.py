class Company():
    def __init__(self,name,):
        self.__name=name            #it is a private variable(property) it can't be accessed outside

    @property                               #@property is a decorator which makes method as getter
    def companyname(self):                  #getter gets the value of the property
        print("@property method is called")
        return self.__name
    
    @companyname.setter                     #@setter sets the value to the property
    def companyname(self, value):
        print("@Setter is called")
        self.__name=value
        return self.__name
    
cmp=Company("Amazon")
print("="*35)
print(cmp.companyname)                      #@Getter and @setter are called without parenthesis
print("="*35)
cmp.companyname="Google"                    #Setter sets the value to "Google"
print(cmp.companyname)
print("="*35)
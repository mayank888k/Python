class Employee():
    employee_no=54
    def __init__(self,name,enroll,desig):           #instance method, takes self as first argument
        self.name=name                              
        self.enroll=enroll
        self.desig=desig
    
    @classmethod                      #class method used to change class vbariable using instace
    def changeempno(cls, newempno):   #it takes first argument as cls
        cls.employee_no=newempno
    
    @classmethod                # class method as alternative constructor to create object
    def objcreation(cls, str):
        a=str.split('/')
        return cls(a[0],int(a[1]),a[2])         #return a class object
    
    @staticmethod           #static mathod takes niether self nor cls as first argument
    def checkempno():
        if Employee.employee_no>64:print("Greater than 64")
    
emp1=Employee("Mayank",62,"SDE")
emp2=Employee.objcreation("Astha/31/SDE")

emp1.changeempno(85)   #changinge class variable using instance using class method
print(f"Employee name = {emp1.name} Employee enroll = {emp1.enroll} Employee Dsignation = {emp1.desig}")
print(f"Employee name = {emp2.name} Employee enroll = {emp2.enroll} Employee Dsignation = {emp2.desig}")
emp1.checkempno()

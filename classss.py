class Employee():
    employee_no=5                         #Class variable or attributes
    def __init__(self,aname,srno):        #Constructor 
        self.name=aname                   #Instance variable or attributes
        self.srno=srno

Mayank=Employee("Mayank",62)            #INSTANCE OR OBJECT
Astha=Employee("Astha",31)              
Mayank.package=23

print(f"Employee name is {Mayank.name} and SrNo. is {Mayank.srno} and Package {Mayank.package} LPA")
print(f"Employee name is {Astha.name} and SrNo. is {Astha.srno}")
print(f"Total Employee is {Mayank.employee_no} {Astha.employee_no} {Employee.employee_no}")


#FUNCTIONS ARE KNOWN AS METHODS IN CLASS 
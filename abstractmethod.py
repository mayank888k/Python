from abc import ABC,abstractmethod

class shape(ABC):           #ABC is a metaclass, class is an instance of metaclass
    @abstractmethod         #@abstractmethod makes the method compulsory to inherited class
    def area(self):
        return 0

class rectangle(shape):
    def __init__(self):
        self.length=50
        self.breadth=60
    
    def area(self):                         #this is compulsory as it is a abstract method
        return self.length*self.breadth

rect1=rectangle()
print(rect1.area(),type(shape),type(rectangle))
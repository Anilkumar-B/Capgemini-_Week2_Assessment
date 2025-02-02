"""•	16. Create an interface `IShape` with an abstract method `calculate_area()`.
 Implement it in `Rectangle` and `Circle` classes."""

from abc import ABC,abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
class Rectangle(IShape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def calculate_area(self):
        return self.length*self.breadth
    
class Circle(IShape):
    def __init__(self,radius):
        self.radius=radius
        
    def calculate_area(self):
        return 3.14*self.radius**2
    
length=float(input("enter length of rectangle: "))
breadth=float(input("enter breadth of rectangle: "))
rectangle=Rectangle(length,breadth)
print("Area of rectangle:",rectangle.calculate_area())

radius=float(input("Enter radius of the circle: "))
circle=Circle(radius)
print("Area of Circle:",circle.calculate_area())

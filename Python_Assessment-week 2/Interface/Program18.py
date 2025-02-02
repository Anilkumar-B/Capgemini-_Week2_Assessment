"""•	18. Implement an abstract class `ICalculator` with methods 
`add()`, `subtract()`, `multiply()`, and `divide()`.
 Create a `BasicCalculator` class that implements these methods."""


from abc import ABC,abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    @abstractmethod
    def subtract(self,a,b):
        pass
    @abstractmethod
    def multiply(self,a,b):
        pass
    @abstractmethod
    def divide(self,a,b):
        pass
    
class BasicCalculator(ICalculator):
    def add(self,a,b):
        return a+b
    def subtract(self, a, b):
        return a-b
    def multiply(self, a, b):
        return a*b
    def divide(self, a, b):
        return a//b
    
a=int(input("Enter a value: "))
b=int(input("enter b value: "))
calculation=BasicCalculator()
print("ADdition od a,b is: ",calculation.add(a,b))
print("SUbtraction of a,b is: ",calculation.subtract(a,b))
print("Multiplication of a,b: ",calculation.multiply(a,b))
print("Division of a,b: ",calculation.divide(a,b))

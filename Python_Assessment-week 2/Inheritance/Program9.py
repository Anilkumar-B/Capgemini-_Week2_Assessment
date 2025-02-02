"""•	9. Simulate multiple inheritance where `FlyingCar` inherits 
from both `Car` and `Airplane`. Handle potential conflicts in the `move()` method."""



class Car():
    def __init__(self,name):
        self.name=name
        
    def move(self):
        return f"{self.name} is moving"
        
class Airplane():
    def __name__(self,name):
        self.name=name
        
    def move(self):
        return f'{self.name} is flying'
        
class Flyingcar(Car,Airplane):
    def __init__(self,name):
        self.name=name
    
    def move(self):
        road=super().move()
        air=Airplane.move(self)
        return f'{road} and {air}'
    
name=input("enter name: ")
flyingcar=Flyingcar(name)
print(flyingcar.move())
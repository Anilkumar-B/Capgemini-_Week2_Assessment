"""•	6. Implement a multi-level inheritance example where `Vehicle` is a base class, 
`Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`."""



class Vechile():
    def __init__(self,name):
        self.name=name
        
    def display(self):
        print(f"It is a Vechile  {self.name}")
    
class Car(Vechile):
    def __init__(self,name):
        super().__init__(name)
        
    def display(self):
        print(f"It is a car {self.name}")
        
class Bike(Vechile):
    def __init__(self,name):
        super().__init__(name)
        
    def display(self):
        print(f"It is a bike {self.name}")
        
class Electriccar(Car):
    def __init__(self,name):
        super().__init__(name)
        
    def display(self):
        print(f"It is an electric car {self.name}")

vechile=Vechile("Vechile")
car=Car("Tata")
bike=Bike("Honda")
electriccar=Electriccar("Tata Electric")

vechile.display()
car.display()
bike.display()
electriccar.display()
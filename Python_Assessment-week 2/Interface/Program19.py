"""•	19. Develop an interface `IVehicle`
 with abstract methods `start_engine()` and `stop_engine()`.
 Implement it in `Car`, `Bike`, and `Truck` classes."""


from abc import ABC,abstractmethod

class IVechile(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    
class Car(IVechile):
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"

class Bike(IVechile):
    def start_engine(self):
        return "Bike engine started"

    def stop_engine(self):
        return "Bike engine stopped"

class Truck(IVechile):
    def start_engine(self):
        return "Truck engine started"

    def stop_engine(self):
        return "Truck engine stopped"

car = Car()
print(car.start_engine())
print(car.stop_engine())

bike = Bike()
print(bike.start_engine())
print(bike.stop_engine())

truck = Truck()
print(truck.start_engine())
print(truck.stop_engine())
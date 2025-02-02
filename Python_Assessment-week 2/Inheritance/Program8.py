"""•	8. Design a system where a base class `Animal` 
has a method `speak()`, and subclasses `Dog` and `Cat` override it."""


class Animal():
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        pass
        
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        print(f'{name} it is a dog')
    
        
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
        print(f'{name} it is a cat')

dog=Dog("Snoofy")
cat=Cat("harry")

dog.speak()
cat.speak()
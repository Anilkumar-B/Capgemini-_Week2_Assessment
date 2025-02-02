"""1. Create a class `Employee` with properties `name`, `id`, and `department`.
 Instantiate an object and assign values dynamically."""


class Employee():
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
        
employee1=Employee("Anil","22H55A7303","AIML")
print(f" Employee details {employee1.name}, {employee1.id}, {employee1.department}")
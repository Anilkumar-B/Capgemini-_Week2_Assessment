"""•	7. Create a multi-level class structure with 
`Person` → `Employee` → `Manager`, where `Manager` has an additional method
 `approve_leave()`."""


class Person():
    def __init__(self,name):
        self.name=name
        
class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id=emp_id

class Manager(Employee):
    def __init__(self,name,emp_id,m_name):
        super().__init__(name,emp_id)
        self.m_name=m_name 
    
    def approve_leave(self,name,days,m_name):
        return f'{name} has took {days} holidays approved by {self.m_name}'
 
name=input("enter name of employee: ")
emp_id=int(input("Enter employ id:"))
m_name=input("enter manager name :")
days=int(input("enter number of days for leave:"))
manager=Manager(name,emp_id,m_name)
print(manager.approve_leave(name,days,m_name))       
        
        
           
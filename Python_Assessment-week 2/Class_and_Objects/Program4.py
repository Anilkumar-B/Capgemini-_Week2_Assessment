"""	4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`.
 Write a method to return student details."""



class Student():
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
        
    def display(self):
        return f'Student name {self.name} along with roll number {self.roll_number}'

student=Student("Anil",7303)
print(student.display())
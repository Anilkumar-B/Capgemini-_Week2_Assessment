"""•	13. Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` 
classes that provide specific implementations for `area()`."""

class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
def get_input():
    side=float(input("Enter the side of the square: "))
    base=float(input("Enter the base of the triangle: "))
    height=float(input("Enter the height of the triangle: "))
    return side,base,height
def main():
    side,base,height=get_input()
    square=Square(side)
    triangle=Triangle(base,height)
    print(f"Square area:{square.area()}")
    print(f"Triangle area:{triangle.area()}")
main()
"""•	5. Create a `Product` class with attributes `name`, `price`, and `stock`.
 Write a method `check_availability(quantity)` 
that returns whether the requested quantity is available."""


class Product():
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        
    def check_availability(self,quantity):
        return quantity<=self.stock
    
product=Product("products",2000,10)
#if product is available it returns true otherwise return false
print(product.check_availability(10))
print(product.check_availability(11))
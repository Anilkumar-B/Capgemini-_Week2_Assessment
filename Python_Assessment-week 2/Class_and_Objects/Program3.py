"""3. You are building a Library Management System. Create a `Book` class with
 properties like `title`, `author`, and `isbn`.
 Write a method to display book details."""

 #Library management system
class Book():
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        
    def display(self):
        print(f'Details of book: Title of Book {self.title} author is {self.author} and isbn is {self.isbn}')
        
book=Book("Ramayana","valmiki",191)
book.display()
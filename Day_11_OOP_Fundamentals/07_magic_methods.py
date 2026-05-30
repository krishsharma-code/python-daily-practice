# Day 11: Magic Methods (Dunder Methods)
# Concept: Implementing dunder methods like __str__ and __len__.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # Controls what is shown when the object is printed
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        # Controls what len() returns for this object
        return self.pages

my_book = Book("Python OOP Fundamentals", "Guido van Rossum", 350)
print(my_book)      # Calls __str__
print(len(my_book)) # Calls __len__

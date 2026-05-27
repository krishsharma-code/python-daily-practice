class Animal:
    """Parent Class"""
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    """Child Class inheriting from Animal"""
    def speak(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    """Child Class inheriting from Animal"""
    def speak(self):
        print(f"{self.name} meows!")

# Using Inheritance
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

my_dog.speak()
my_cat.speak()

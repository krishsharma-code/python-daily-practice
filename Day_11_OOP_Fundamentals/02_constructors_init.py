# Day 11: Constructors (__init__)
# Concept: Using the __init__ method to initialize object attributes.

class Car:
    def __init__(self, brand, year, color="White"):
        # The constructor initializes the object's state
        self.brand = brand
        self.year = year
        self.color = color
        self.is_running = False
        print(f"A new {self.color} {self.brand} has been created.")

    def start_engine(self):
        self.is_running = True
        print(f"The {self.brand}'s engine is now running.")

# Creating an object with positional and default arguments
my_car = Car("Tesla", 2024, "Midnight Blue")
my_car.start_engine()

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Demonstrating Abstract Base Classes (ABC).
    Classes inheriting from Shape MUST implement the abstract methods.
    """
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Testing the implementation
if __name__ == "__main__":
    shapes = [Square(5), Circle(3)]
    
    for shape in shapes:
        print(f"Shape: {type(shape).__name__}")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
        print("-" * 20)
    
    # Attempting to instantiate the abstract class will fail
    try:
        s = Shape()
    except TypeError as e:
        print(f"Error: {e}")

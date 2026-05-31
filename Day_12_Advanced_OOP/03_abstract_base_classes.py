from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract Base Class for geometric shapes.
    Enforces that all child classes implement area() and perimeter() methods.
    """
    
    @abstractmethod
    def area(self):
        """Must be overridden in subclasses."""
        pass

    @abstractmethod
    def perimeter(self):
        """Must be overridden in subclasses."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    import math
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# --- Testing the implementation ---
if __name__ == "__main__":
    shapes = [Rectangle(10, 5), Circle(7)]
    
    for shape in shapes:
        print(f"Shape: {type(shape).__name__}")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
        print("-" * 20)
    
    # Attempting to instantiate ABC will raise TypeError
    try:
        s = Shape()
    except TypeError as e:
        print(f"Error instantiating Shape: {e}")

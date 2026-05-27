class Shape:
    """Base class for shapes."""
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Overriding the parent area method
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        # Overriding the parent area method
        return self.side * self.side

# Demonstrating Polymorphism
shapes = [Circle(5), Square(4), Circle(2)]

for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area()}")

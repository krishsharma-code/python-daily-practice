def greet_user(name="Developer"):
    """
    Greets the user with a default or provided name.
    """
    return f"Hello, {name}! Welcome to Day 7 of Python Basics."

def calculate_area(length, width):
    """
    Calculates and returns the area of a rectangle.
    """
    area = length * width
    return area

# Main execution block
if __name__ == "__main__":
    # Positional and default arguments
    print(greet_user("Krish"))
    print(greet_user())

    # Storing return values
    rect_area = calculate_area(10, 5)
    print(f"Rectangle Area: {rect_area}")

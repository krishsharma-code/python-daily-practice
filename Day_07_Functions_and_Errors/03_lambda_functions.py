# Lambda functions are small, anonymous functions defined with the 'lambda' keyword.

# Basic lambda for squaring a number
square = lambda x: x**2

# List of numbers for demonstration
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map() with lambda to square all numbers in a list
squared_numbers = list(map(lambda x: x**2, numbers))

# Using filter() with lambda to extract only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Main execution block
if __name__ == "__main__":
    print(f"Original Numbers: {numbers}")
    print(f"Square of 5: {square(5)}")
    print(f"Squared List: {squared_numbers}")
    print(f"Even Numbers Filtered: {even_numbers}")

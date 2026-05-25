# 06_lambda_functions.py
# Concept: Basic anonymous functions

# Regular function
def square(x):
    return x * x

# Equivalent Lambda function
# syntax: lambda arguments: expression
square_lambda = lambda x: x * x

print(f"Square of 5 (regular): {square(5)}")
print(f"Square of 5 (lambda): {square_lambda(5)}")

# Lambda with multiple arguments
add = lambda a, b: a + b
print(f"Addition using lambda: {add(10, 20)}")

# Often used with map(), filter(), etc.
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda n: n * 2, numbers))
print(f"Doubled list: {doubled}")

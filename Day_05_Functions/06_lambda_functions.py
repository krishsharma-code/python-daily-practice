# 06_lambda_functions.py
# Concept: Basic anonymous functions (Lambda)

# A standard function
def square(x):
    return x * x

# An equivalent lambda function
# Syntax: lambda arguments: expression
square_lambda = lambda x: x * x

print(f"Square using function: {square(5)}")
print(f"Square using lambda: {square_lambda(5)}")

# Lambda with multiple arguments
adder = lambda a, b: a + b
print(f"Sum using lambda: {adder(10, 20)}")

# Lambda functions are often used for quick, one-line logic.

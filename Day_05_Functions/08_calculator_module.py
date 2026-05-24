# 08_calculator_module.py
# Concept: A math calculator built entirely with functions

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    print("--- Function-Based Calculator ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == '+':
        print(f"Result: {add(num1, num2)}")
    elif op == '-':
        print(f"Result: {subtract(num1, num2)}")
    elif op == '*':
        print(f"Result: {multiply(num1, num2)}")
    elif op == '/':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid Operation!")

# We wrap the call in a check to see if the script is run directly
if __name__ == "__main__":
    # Skipping interactive call for automated environments, 
    # but demonstrating how it would work.
    print("Calculator Module Loaded. Example: add(5,3) =", add(5,3))
    # calculator() 

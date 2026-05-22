# 03_basic_calculator.py
# Day 1: Simple Arithmetic Calculator

print("--- Simple Python Calculator ---")

# Taking two numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing basic arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (Cannot divide by zero)"

# Printing the results
print(f"\nResults for {num1} and {num2}:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

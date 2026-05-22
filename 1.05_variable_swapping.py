# Day 2: Variable Swapping
# Demonstrating how to swap two numbers

a = 10
b = 20

print(f"Original: a = {a}, b = {b}")

# Method 1: Using a temporary variable
temp = a
a = b
b = temp
print(f"After temp swap: a = {a}, b = {b}")

# Method 2: Python's direct shortcut
a, b = b, a
print(f"After Pythonic shortcut: a = {a}, b = {b}")

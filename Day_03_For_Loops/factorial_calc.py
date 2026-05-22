# factorial_calc.py
# This script calculates the factorial of a number using a for loop.
# Factorial of 5 (5!) = 5 * 4 * 3 * 2 * 1 = 120

num = 5
factorial = 1

# If the number is negative, factorial doesn't exist.
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    # We loop from 1 up to 'num' (inclusive).
    for i in range(1, num + 1):
        factorial = factorial * i
    
    print(f"The factorial of {num} is {factorial}")

# beginner-friendly tip: We use a 'running product' variable (factorial = 1) 
# and update it in each step of the loop.

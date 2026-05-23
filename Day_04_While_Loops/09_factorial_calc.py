# 09_factorial_calc.py
# Demonstrates calculating a factorial using a while loop.

try:
    num = int(input("Enter a non-negative integer for factorial calculation: "))
    
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        original_num = num
        factorial = 1
        
        # Multiply until num reaches 1
        while num > 0:
            factorial *= num
            num -= 1
            
        print(f"The factorial of {original_num} is {factorial}")

except ValueError:
    print("Invalid input! Please enter an integer.")

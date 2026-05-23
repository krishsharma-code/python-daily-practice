# 05_even_number_filter.py
# Demonstrates using a while loop and modulo operator to filter even numbers.

number = 1

print("Even numbers between 1 and 20:")

while number <= 20:
    # Check if the number is divisible by 2
    if number % 2 == 0:
        print(number, end=" ")
    number += 1

print("\nProcessing complete.")

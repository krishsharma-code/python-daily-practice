# table_generator.py
# This script generates a multiplication table for a given number using a for loop.

# We can take input from the user or define a number directly.
# Let's use 5 for this example.
number = 5

print(f"Multiplication Table for {number}:")

# The range(1, 11) function generates numbers from 1 to 10.
# We iterate through each number 'i' and multiply it by our target 'number'.
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

# beginner-friendly tip: range(start, stop) includes 'start' but excludes 'stop'.

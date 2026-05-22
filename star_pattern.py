# star_pattern.py
# This script prints a right-angled triangle star pattern using nested loops (or multiplication).

rows = 5

print("Right-angled triangle pattern:")

# We loop from 1 to 'rows'.
for i in range(1, rows + 1):
    # In Python, we can multiply a string by an integer to repeat it.
    # This is a concise way to handle simple patterns.
    print("*" * i)

# beginner-friendly tip: For more complex patterns, you might use 
# a 'nested loop' (a loop inside another loop).

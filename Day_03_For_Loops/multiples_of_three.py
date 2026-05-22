# multiples_of_three.py
# This script finds and prints all multiples of 3 between 1 and 30.

print("Multiples of 3 between 1 and 30:")

# We can use an if statement inside the loop to check for divisibility.
for i in range(1, 31):
    if i % 3 == 0:  # The % (modulo) operator returns the remainder of a division.
        print(i)

# beginner-friendly tip: i % 3 == 0 means i is perfectly divisible by 3.
# Alternatively, you could use range(3, 31, 3) for the same result!

# sum_of_numbers.py
# This script calculates the sum of the first N natural numbers.

n = 10
total_sum = 0

# We loop from 1 to n.
for i in range(1, n + 1):
    total_sum += i

print(f"The sum of the first {n} natural numbers is: {total_sum}")

# beginner-friendly tip: 'total_sum += i' is shorthand for 'total_sum = total_sum + i'.
# This is called an augmented assignment operator.

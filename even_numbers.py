# even_numbers.py
# This script prints even numbers from 1 to 50 using the 'step' parameter in range().

print("Even numbers from 1 to 50:")

# range(start, stop, step)
# start: 2 (the first even number)
# stop: 51 (so it includes 50)
# step: 2 (skips every other number)
for i in range(2, 51, 2):
    print(i, end=" ")

# beginner-friendly tip: The third argument in range() is the 'step'. 
# It tells Python how much to increment the loop variable in each iteration.

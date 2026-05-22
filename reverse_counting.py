# reverse_counting.py
# This script prints numbers from 10 down to 1 using a reverse loop step.

print("Reverse counting from 10 down to 1:")

# range(start, stop, step)
# start: 10
# stop: 0 (exclusive, so it stops at 1)
# step: -1 (decrements by 1 in each step)
for i in range(10, 0, -1):
    print(i)

# beginner-friendly tip: When the step is negative, the loop runs 'backwards'.
# Ensure your 'start' is greater than your 'stop' in this case!

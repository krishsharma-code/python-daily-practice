# 01_basic_counter.py
# Demonstrates a simple while loop counting from 1 to 10.

# Initialize the counter variable
counter = 1

print("Counting from 1 to 10:")

# The loop continues as long as the condition (counter <= 10) is True
while counter <= 10:
    print(f"Number: {counter}")
    # Increment the counter to eventually make the condition False
    counter += 1

print("Loop finished.")

# 03_sentinel_value.py
# Demonstrates a while loop that stops when a specific 'sentinel' value (0) is entered.

print("Enter numbers to print them. Enter '0' to stop.")

# Initialize user_input with a non-sentinel value to start the loop
user_input = -1

while user_input != 0:
    try:
        user_input = int(input("Enter a number (0 to quit): "))
        if user_input != 0:
            print(f"You entered: {user_input}")
    except ValueError:
        print("Invalid input! Please enter an integer.")

print("Sentinel value reached. Goodbye!")

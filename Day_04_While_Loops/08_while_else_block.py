# 08_while_else_block.py
# Demonstrates the Python-specific 'while...else' structure.

# The 'else' block executes ONLY if the loop finishes normally (without a 'break').

target = 5
counter = 0

print(f"Searching for {target} in a range up to 10...")

while counter < 10:
    if counter == target:
        print(f"Found {target}! Exiting search.")
        break
    counter += 1
else:
    # This will NOT run because the loop was broken by the 'break' statement
    print("Target not found.")

print("---")

# Example where else block executes
counter = 0
print("Searching for 15 (which isn't there) up to 10...")
while counter < 10:
    if counter == 15:
        break
    counter += 1
else:
    # This WILL run because the loop finished without hitting 'break'
    print("Loop finished naturally: 15 was not found.")

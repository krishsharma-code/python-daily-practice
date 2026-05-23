# 06_break_statement.py
# Demonstrates an infinite loop exited safely using the 'break' statement.

counter = 0

print("Loop starting...")

# 'while True' creates an infinite loop
while True:
    print(f"Counter: {counter}")
    
    # Check if we should exit the loop
    if counter >= 5:
        print("Break condition met! Exiting loop.")
        break  # The 'break' statement terminates the current loop immediately
    
    counter += 1

print("Loop exited safely.")

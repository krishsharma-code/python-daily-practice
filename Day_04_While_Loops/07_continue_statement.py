# 07_continue_statement.py
# Demonstrates skipping an iteration using the 'continue' statement.

counter = 0

print("Counting from 1 to 10, but skipping 5:")

while counter < 10:
    counter += 1
    
    # If counter is 5, skip the rest of this iteration
    if counter == 5:
        print("Skipping number 5...")
        continue  # The 'continue' statement jumps back to the start of the loop
    
    print(f"Number: {counter}")

print("Loop finished.")

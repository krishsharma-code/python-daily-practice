# 02_countdown_timer.py
# Demonstrates a while loop counting down from 10 to 1, using 'time' module for delay.

import time

# Initialize the countdown variable
count = 10

print("Starting countdown...")

# Loop runs while count is greater than 0
while count > 0:
    print(f"Time remaining: {count} seconds")
    # Wait for 1 second to simulate a real timer
    time.sleep(1)
    # Decrement the count
    count -= 1

print("Blast off! 🚀")

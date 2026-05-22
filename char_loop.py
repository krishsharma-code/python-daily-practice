# char_loop.py
# This script iterates through a string and prints each character individually.

word = "PYTHON"

print(f"Iterating through the characters of '{word}':")

# Strings in Python are iterable! This means we can loop directly over them.
for char in word:
    print(f"Character: {char}")

# beginner-friendly tip: You don't always need range(). If you have a sequence 
# (like a string or a list), you can loop through its items directly.

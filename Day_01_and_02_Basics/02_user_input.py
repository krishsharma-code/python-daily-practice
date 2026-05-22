# 02_user_input.py
# Day 1: Personalized Welcome Script

# Taking user input for name
name = input("Enter your name: ")

# Taking user input for age
# Note: input() returns a string, so we can convert it to int if needed, 
# but for a welcome message, a string is fine.
age = input("Enter your age: ")

# Printing a personalized welcome message
print(f"Hello {name}!")
print(f"It's great to know that you are {age} years old.")
print("Welcome to the world of Python programming!")

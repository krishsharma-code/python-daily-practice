# 06_dict_comprehensions.py
# Concept: Creating dictionaries dynamically

# Example 1: Creating a dictionary from two lists
keys = ['name', 'age', 'job']
values = ['Krish', 24, 'Developer']
# Using zip() and comprehension
profile = {k: v for k, v in zip(keys, values)}
print(f"User Profile: {profile}")

# Example 2: Modifying an existing dictionary
prices = {'apple': 1.2, 'banana': 0.5, 'cherry': 2.5}
# Increase all prices by 10%
new_prices = {fruit: price * 1.1 for fruit, price in prices.items()}
print(f"Inflated prices: {new_prices}")

# Example 3: Filtering a dictionary
# Keep only items with price > 1.0
expensive_fruits = {fruit: price for fruit, price in prices.items() if price > 1.0}
print(f"Expensive fruits: {expensive_fruits}")

# Example 4: Creating a dictionary of squares
number_squares = {x: x**2 for x in range(1, 6)}
print(f"Number squares: {number_squares}")

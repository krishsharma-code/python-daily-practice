# 05_list_comprehensions.py
# Concept: Concise creation of lists

# Example 1: Creating a list of squares
# Traditional way:
squares_old = []
for x in range(10):
    squares_old.append(x**2)

# Using List Comprehension:
# [expression for item in iterable]
squares_new = [x**2 for x in range(10)]
print(f"Squares: {squares_new}")

# Example 2: Filtering with list comprehension
# [expression for item in iterable if condition]
numbers = [1, 5, 12, 18, 22, 35, 42]
evens = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {evens}")

# Example 3: String manipulation
words = ["hello", "world", "python", "data"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase words: {uppercase_words}")

# Example 4: Complex logic (Conditional Expression)
# [expression_if_true if condition else expression_if_false for item in iterable]
status = ["Pass" if n >= 20 else "Fail" for n in numbers]
print(f"Status results: {status}")

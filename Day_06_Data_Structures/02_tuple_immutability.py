# 02_tuple_immutability.py
# Concept: Tuples - The Immutable Sequence

# 1. Creating a Tuple (using parentheses)
dimensions = (1920, 1080)
print(f"Screen Dimensions: {dimensions}")

# 2. Accessing elements
print(f"Width: {dimensions[0]}")
print(f"Height: {dimensions[1]}")

# 3. Immutability: This will cause an error if uncommented
# dimensions[0] = 2560 

# 4. Tuple Unpacking
# Assigning values from a tuple to multiple variables at once
width, height = dimensions
print(f"Unpacked -> Width: {width}, Height: {height}")

# 5. Single element tuple (requires a trailing comma)
singleton = (50,)
print(f"Singleton tuple: {singleton} Type: {type(singleton)}")

# 6. Converting between list and tuple
points_list = [10, 20, 30]
points_tuple = tuple(points_list)
print(f"Converted Tuple: {points_tuple}")

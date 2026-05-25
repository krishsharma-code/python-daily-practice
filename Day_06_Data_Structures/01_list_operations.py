# 01_list_operations.py
# Concept: Mastering Lists - Mutability and Sequence Operations

# 1. Creating a list
fruits = ["apple", "banana", "cherry"]
print(f"Initial list: {fruits}")

# 2. Append: Adding to the end
fruits.append("orange")
print(f"After append: {fruits}")

# 3. Insert: Adding at a specific index
fruits.insert(1, "blueberry")
print(f"After insert at index 1: {fruits}")

# 4. Remove: Deleting by value
fruits.remove("banana")
print(f"After removing 'banana': {fruits}")

# 5. Pop: Deleting by index (returns the removed item)
last_fruit = fruits.pop()
print(f"Popped item: {last_fruit}")
print(f"After pop: {fruits}")

# 6. Slicing: Accessing sub-parts of the list [start:stop:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nNumbers: {numbers}")
print(f"Slice [2:7]: {numbers[2:7]}")
print(f"Every second number [::2]: {numbers[::2]}")
print(f"Reversed list [::-1]: {numbers[::-1]}")

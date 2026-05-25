# 03_set_mathematics.py
# Concept: Sets - Uniqueness and Mathematical Operations

# 1. Creating sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# 2. Uniqueness (Duplicates are automatically removed)
duplicates = {1, 2, 2, 3, 3, 3}
print(f"Unique set: {duplicates}")

# 3. Union: All items from both sets (no duplicates)
print(f"Union (A | B): {set_a | set_b}")

# 4. Intersection: Only items present in both sets
print(f"Intersection (A & B): {set_a & set_b}")

# 5. Difference: Items in A but not in B
print(f"Difference (A - B): {set_a - set_b}")

# 6. Symmetric Difference: Items in either A or B, but not both
print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}")

# 7. Membership Testing (Sets are highly optimized for this)
print(f"Is 3 in Set A? {3 in set_a}")

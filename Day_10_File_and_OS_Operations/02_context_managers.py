"""
Day 10: Context Managers
Concept: Using the 'with' statement for safe and efficient file handling.
"""

# The 'with' statement automatically handles file closing even if errors occur.
# This is the industry standard for file operations in Python.

file_path = "context_example.txt"

# Writing with context manager
with open(file_path, "w") as f:
    f.write("Using 'with' statement is safer.\n")
    f.write("No need to call f.close() explicitly.\n")

print(f"Successfully wrote to {file_path}")

# Reading with context manager
with open(file_path, "r") as f:
    data = f.readlines()  # Reads all lines into a list
    print("\nFile Content as List:")
    for line in data:
        print(f"-> {line.strip()}")

# The file is already closed here automatically.

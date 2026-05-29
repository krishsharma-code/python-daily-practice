"""
Day 10: File Handling Basics
Concept: Opening, reading, and writing basic text files.
"""

# 1. Writing to a file
# 'w' mode: overwrites if file exists, creates if not
file_name = "example.txt"
file = open(file_name, "w")
file.write("Hello, Day 10 of Python Basics!\n")
file.write("We are learning File Handling today.\n")
file.close()  # Always close the file to free system resources

print(f"File '{file_name}' written successfully.")

# 2. Reading from a file
# 'r' mode: default mode for reading
file = open(file_name, "r")
content = file.read()
print("\nReading entire content:")
print(content)
file.close()

# 3. Reading line by line
file = open(file_name, "r")
print("\nReading line by line:")
for line in file:
    print(f"Line: {line.strip()}")
file.close()

# 4. Appending to a file
# 'a' mode: adds content to the end of the file
file = open(file_name, "a")
file.write("Appending this new line to the file.\n")
file.close()

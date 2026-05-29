"""
Day 10: OS Module Navigation
Concept: Creating directories, listing files, and checking paths.
"""

import os

# 1. Get current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# 2. Listing files and directories
print("\nFiles in current directory:")
files = os.listdir('.')
for f in files:
    print(f"- {f}")

# 3. Checking if a path exists
target_file = "example.txt"
if os.path.exists(target_file):
    print(f"\n'{target_file}' exists.")
    
    # 4. Getting file details
    size = os.path.getsize(target_file)
    print(f"File size: {size} bytes")
else:
    print(f"\n'{target_file}' does not exist.")

# 5. Creating a sub-directory
sub_dir = "test_subfolder"
if not os.path.exists(sub_dir):
    os.mkdir(sub_dir)
    print(f"\nDirectory '{sub_dir}' created.")
else:
    print(f"\nDirectory '{sub_dir}' already exists.")

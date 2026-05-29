"""
Day 10: Shutil File Backup
Concept: Using 'shutil' to copy and archive files securely.
"""

import shutil
import os

source = "example.txt"
destination = "example_backup.txt"

# 1. Copying a single file
if os.path.exists(source):
    shutil.copy(source, destination)
    print(f"Backup created: {destination}")

# 2. Creating a zip archive of the current directory
# format options: 'zip', 'tar', 'gztar', 'bztar', 'xztar'
archive_name = "day_10_backup"
shutil.make_archive(archive_name, 'zip', '.')
print(f"Archive '{archive_name}.zip' created successfully.")

# 3. Moving a file (can also be used for renaming)
# shutil.move("example_backup.txt", "archived_example.txt")

"""
Day 10: CSV Data Parser
Concept: Reading and writing tabular data using the 'csv' module.
"""

import csv

csv_file = "data.csv"

# 1. Writing to a CSV file
data = [
    ["Name", "Role", "Level"],
    ["Krish", "Admin", "Expert"],
    ["John", "User", "Beginner"],
    ["Sarah", "Dev", "Intermediate"]
]

with open(csv_file, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print(f"CSV data written to {csv_file}")

# 2. Reading from a CSV file
print("\nReading CSV data:")
with open(csv_file, mode="r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"Row: {row}")

# 3. Using DictReader (Maps columns to a dictionary)
print("\nUsing DictReader:")
with open(csv_file, mode="r") as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        print(f"{row['Name']} is a {row['Role']} ({row['Level']})")

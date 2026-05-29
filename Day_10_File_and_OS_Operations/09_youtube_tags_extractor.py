"""
Day 10: YouTube Tags Extractor (Rise and Shine)
Concept: Extracting hashtags from a text file of video descriptions.
"""

import os

# Create a mock description file for demonstration
description_file = "video_description.txt"
with open(description_file, "w") as f:
    f.write("Welcome to the Rise and Shine vlog! #MorningRoutine #Vlog #Python #Productivity\n")
    f.write("Today we are exploring file handling in Python. #CodingLife #Day10\n")

def extract_tags(file_path):
    tags = []
    if not os.path.exists(file_path):
        print("Description file not found.")
        return tags

    with open(file_path, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if word.startswith("#"):
                    tags.append(word)
    return tags

print(f"Extracting tags from {description_file}...")
found_tags = extract_tags(description_file)

if found_tags:
    print("Found Hashtags:")
    for tag in found_tags:
        print(f"- {tag}")
else:
    print("No tags found.")

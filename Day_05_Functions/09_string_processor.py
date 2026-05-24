# 09_string_processor.py
# Concept: Functions to process and analyze strings

def reverse_string(text):
    """Returns the string reversed."""
    return text[::-1]

def count_vowels(text):
    """Counts the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def capitalize_words(text):
    """Capitalizes the first letter of each word."""
    return text.title()

# Testing our string processor functions
sample = "python functions are powerful"

print(f"Original: {sample}")
print(f"Reversed: {reverse_string(sample)}")
print(f"Vowel Count: {count_vowels(sample)}")
print(f"Title Case: {capitalize_words(sample)}")

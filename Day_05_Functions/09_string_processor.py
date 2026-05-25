# 09_string_processor.py
# Concept: Functions to reverse, capitalize, and count vowels

def reverse_string(text):
    """Returns the string reversed."""
    return text[::-1]

def capitalize_words(text):
    """Capitalizes the first letter of each word."""
    return text.title()

def count_vowels(text):
    """Counts the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    return count

# Demonstration
sample_text = "python programming is fun"

print(f"Original: {sample_text}")
print(f"Reversed: {reverse_string(sample_text)}")
print(f"Capitalized: {capitalize_words(sample_text)}")
print(f"Vowel Count: {count_vowels(sample_text)}")

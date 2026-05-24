# 04_return_values.py
# Concept: Returning single and multiple values from a function

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def get_arithmetic_stats(num1, num2):
    """Return multiple values as a tuple."""
    addition = num1 + num2
    product = num1 * num2
    return addition, product # Python packs these into a single tuple

# Receiving a single return value
musician = get_formatted_name('jimi', 'hendrix')
print(f"Artist: {musician}")

# Receiving multiple return values (unpacking)
my_sum, my_prod = get_arithmetic_stats(10, 5)
print(f"Sum: {my_sum}, Product: {my_prod}")

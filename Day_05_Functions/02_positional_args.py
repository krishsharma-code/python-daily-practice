# 02_positional_args.py
# Concept: Passing basic positional arguments

def greet_person(first_name, last_name):
    """
    This function takes two positional arguments.
    The order in which you pass arguments matters.
    """
    print(f"Hello, {first_name} {last_name}!")
    print("Positional arguments are assigned based on their order.")

# Correct order: 'Krish' -> first_name, 'Sharma' -> last_name
greet_person("Krish", "Sharma")

# Swapping the order will change the assignment
greet_person("Sharma", "Krish")

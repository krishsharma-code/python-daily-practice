# 03_keyword_args.py
# Concept: Keyword arguments and Default values

def describe_pet(pet_name, animal_type='dog'):
    """
    animal_type has a default value of 'dog'.
    If no value is provided for animal_type, it uses 'dog'.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Positional and default
describe_pet(pet_name='willie')

# Overriding the default value using positional argument
describe_pet('harry', 'hamster')

# Using keyword arguments (order doesn't matter here)
describe_pet(animal_type='cat', pet_name='whiskers')

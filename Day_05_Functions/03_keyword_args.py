# 03_keyword_args.py
# Concept: Keyword arguments and default values

def describe_pet(pet_name, animal_type='dog'):
    """
    Displays information about a pet.
    'animal_type' has a default value of 'dog'.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# 1. Calling using default value for animal_type
describe_pet(pet_name='willie')

# 2. Overriding the default value
describe_pet(pet_name='harry', animal_type='hamster')

# 3. Using keyword arguments out of order
describe_pet(animal_type='cat', pet_name='mimi')

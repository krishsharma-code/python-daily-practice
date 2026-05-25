# 07_args_kwargs.py
# Concept: Handling variable number of arguments

def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    *toppings collects as many positional arguments as the caller provides into a tuple.
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.
    **user_info collects arbitrary keyword arguments into a dictionary.
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Using *args
make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Using **kwargs
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(f"\nUser Profile: {user_profile}")

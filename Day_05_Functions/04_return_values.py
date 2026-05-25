# 04_return_values.py
# Concept: Returning single and multiple values

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def get_user_stats():
    """Returns multiple values as a tuple."""
    username = "krish_dev"
    level = 25
    score = 4500
    return username, level, score # Packing into a tuple

# Receiving a single return value
musician = get_formatted_name('jimi', 'hendrix')
print(f"Musician: {musician}")

# Receiving multiple return values (Unpacking)
user, lvl, pts = get_user_stats()
print(f"User: {user} | Level: {lvl} | Score: {pts}")

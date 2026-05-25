# 04_dictionary_basics.py
# Concept: Dictionaries - Key-Value Mapping

# 1. Creating a Dictionary
player = {
    "name": "Krish",
    "level": 20,
    "inventory": ["sword", "shield", "potion"],
    "is_online": True
}
print(f"Initial Player: {player}")

# 2. Accessing values
print(f"Player Name: {player['name']}")
# Safe access using .get() (avoids KeyError if key doesn't exist)
print(f"Health: {player.get('health', 100)}")

# 3. Modifying and Adding values
player["level"] = 21 # Update existing
player["class"] = "Warrior" # Add new
print(f"Updated Player: {player}")

# 4. Removing items
removed_val = player.pop("is_online")
print(f"Removed is_online: {removed_val}")

# 5. Iterating through a dictionary
print("\n--- Player Stats ---")
for key, value in player.items():
    print(f"{key.capitalize()}: {value}")

# 6. Nested Dictionary
studio_data = {
    "Studio_A": {"project": "Alpha", "team": 12},
    "Studio_B": {"project": "Beta", "team": 8}
}
print(f"\nStudio A Project: {studio_data['Studio_A']['project']}")

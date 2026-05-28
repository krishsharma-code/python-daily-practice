class Inventory:
    """
    Demonstrating practical dunder methods for a game inventory.
    Using __add__ to add items and __sub__ to remove items.
    """
    def __init__(self, owner, items=None):
        self.owner = owner
        self.items = items if items else []

    def __add__(self, item):
        """Allows adding an item using the '+' operator."""
        new_items = self.items + [item]
        return Inventory(self.owner, new_items)

    def __sub__(self, item):
        """Allows removing an item using the '-' operator."""
        if item in self.items:
            new_items = self.items.copy()
            new_items.remove(item)
            return Inventory(self.owner, new_items)
        print(f"Item '{item}' not found in inventory.")
        return self

    def __str__(self):
        return f"{self.owner}'s Inventory: {', '.join(self.items) if self.items else 'Empty'}"

# Testing the implementation
if __name__ == "__main__":
    player_inv = Inventory("Krish")
    
    # Adding items using '+'
    player_inv = player_inv + "Sword"
    player_inv = player_inv + "Shield"
    player_inv = player_inv + "Health Potion"
    
    print(player_inv)
    
    # Removing items using '-'
    player_inv = player_inv - "Shield"
    print(f"After removing Shield: {player_inv}")
    
    # Attempting to remove non-existent item
    player_inv = player_inv - "Mana Potion"

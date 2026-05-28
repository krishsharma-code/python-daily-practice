class Player:
    """
    Demonstrating @classmethod as alternative constructors.
    Class methods have access to the class itself via 'cls'.
    """
    def __init__(self, name, level):
        self.name = name
        self.level = level

    @classmethod
    def from_string(cls, data_string):
        """Creates a Player object from a 'Name-Level' string format."""
        name, level = data_string.split("-")
        return cls(name, int(level))

    @classmethod
    def from_dict(cls, data_dict):
        """Creates a Player object from a dictionary."""
        return cls(data_dict['name'], data_dict['level'])

    def __str__(self):
        return f"Player: {self.name} (Level {self.level})"

# Testing the implementation
if __name__ == "__main__":
    # Standard constructor
    p1 = Player("Archer", 10)
    
    # Alternative constructor: from_string
    p2 = Player.from_string("Mage-15")
    
    # Alternative constructor: from_dict
    p3 = Player.from_dict({"name": "Warrior", "level": 20})
    
    print(p1)
    print(p2)
    print(p3)

from dataclasses import dataclass, field
from typing import List

@dataclass(order=True)
class User:
    """Demonstrates @dataclass decorator for clean data storage objects.
    Automatically generates __init__, __repr__, __eq__, and more.
    """
    sort_index: int = field(init=False, repr=False)
    username: str
    email: str
    age: int
    is_active: bool = True
    preferences: List[str] = field(default_factory=list)

    def __post_init__(self):
        """Called after __init__ is generated. Used here for custom sorting logic."""
        self.sort_index = self.age

# --- Testing the implementation ---
if __name__ == "__main__":
    # Automatic __init__
    user1 = User("krish_sharma", "krish@example.com", 25, preferences=["Python", "AI"])
    user2 = User("alice_dev", "alice@example.com", 22)
    
    # Automatic __repr__
    print(f"User 1: {user1}")
    print(f"User 2: {user2}")
    
    # Comparison logic (enabled by order=True and sort_index)
    print(f"Is user1 older than user2? {user1 > user2}")
    
    # Equality check
    user3 = User("alice_dev", "alice@example.com", 22)
    print(f"Are user2 and user3 equal? {user2 == user3}")

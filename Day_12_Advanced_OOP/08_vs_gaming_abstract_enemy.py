from abc import ABC, abstractmethod

class Enemy(ABC):
    """Abstract Base Class 'Enemy' with enforced attack methods for different game bosses."""
    
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = 100 * level

    @abstractmethod
    def attack(self):
        """Must be implemented by specific enemy types."""
        pass

    @abstractmethod
    def special_move(self):
        """Unique high-damage move for each boss."""
        pass

    def take_damage(self, amount):
        """Shared logic for taking damage."""
        self.health -= amount
        print(f"{self.name} took {amount} damage. Health: {self.health}")

class FrostGiant(Enemy):
    def attack(self):
        print(f"❄️ {self.name} swings a massive ice club!")

    def special_move(self):
        print(f"🌪️ {self.name} casts 'Blizzard Storm'!")

class FireDrake(Enemy):
    def attack(self):
        print(f"🔥 {self.name} bites with scorching fangs!")

    def special_move(self):
        print(f"🌋 {self.name} unleashes 'Magma Breath'!")

# --- Testing the implementation ---
if __name__ == "__main__":
    bosses = [
        FrostGiant("Ymir", 5),
        FireDrake("Ignis", 7)
    ]
    
    print("--- Boss Encounter Started ---")
    for boss in bosses:
        print(f"\nA wild {type(boss).__name__} appeared!")
        boss.attack()
        boss.special_move()
        boss.take_damage(30)

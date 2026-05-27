class GameCharacter:
    """Base class for all characters in the VS Gaming Studio project."""
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def describe(self):
        print(f"Character: {self.name} | Health: {self.health}")

class Player(GameCharacter):
    def __init__(self, name, health, level):
        super().__init__(name, health)
        self.level = level

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.health -= 10

class Enemy(GameCharacter):
    def __init__(self, name, health, type):
        super().__init__(name, health)
        self.type = type

    def roar(self):
        print(f"The {self.type} {self.name} roars menacingly!")

# Gaming Studio Simulation
hero = Player("Krish", 100, 5)
villain = Enemy("Dark Knight", 50, "Warrior")

hero.describe()
villain.roar()
hero.attack(villain)
villain.describe()

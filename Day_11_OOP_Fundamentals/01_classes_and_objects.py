# Day 11: Classes and Objects
# Concept: Defining basic classes, creating instances, and understanding 'self'.

class Robot:
    """A simple class representing a Robot."""
    
    def __init__(self, name, model):
        # 'self' refers to the specific instance of the class
        self.name = name
        self.model = model
    
    def greet(self):
        """Method to make the robot greet."""
        print(f"Hello! I am {self.name}, a {self.model} model.")

# Creating instances (objects) of the Robot class
bot1 = Robot("Atlas", "v1.0")
bot2 = Robot("Spot", "v2.5")

# Accessing attributes and calling methods
bot1.greet()
bot2.greet()

# 05_variable_scope.py
# Concept: Local vs Global Variables

# Global variable: Defined outside any function
player_score = 100

def update_score():
    """Demonstrates local vs global scope."""
    # Local variable: Only exists inside this function
    bonus_points = 50
    
    # Accessing global variable (Read-only by default)
    print(f"Current score inside function: {player_score}")
    print(f"Bonus points: {bonus_points}")
    
    # To modify a global variable, use the 'global' keyword
    global player_score
    player_score += bonus_points

print(f"Initial global score: {player_score}")
update_score()
print(f"Updated global score: {player_score}")

# This would cause an error because bonus_points is local to update_score()
# print(bonus_points)

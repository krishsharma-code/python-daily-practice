# 10_gaming_stats_updater.py
# Concept: Logic script simulating player score updates using functions

# Global game state
player_score = 0

def add_points(points):
    """
    Demonstrates using the 'global' keyword to modify a global variable.
    """
    global player_score
    player_score += points
    print(f"Points added: {points}. Current Score: {player_score}")

def reset_score():
    global player_score
    player_score = 0
    print("Score reset to zero.")

def check_rank(score):
    """Returns rank based on score."""
    if score >= 100:
        return "Pro"
    elif score >= 50:
        return "Amateur"
    else:
        return "Noob"

# Simulating gameplay
add_points(20)
add_points(45)
print(f"Player Rank: {check_rank(player_score)}")

add_points(40)
print(f"Final Score: {player_score}")
print(f"Final Rank: {check_rank(player_score)}")

reset_score()

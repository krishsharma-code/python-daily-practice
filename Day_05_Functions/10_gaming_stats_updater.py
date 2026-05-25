# 10_gaming_stats_updater.py
# Concept: Simulating player score updates using functions

# Initial player stats
player_data = {
    'name': 'Krish',
    'score': 0,
    'health': 100,
    'level': 1
}

def update_score(stats, points):
    """Updates the player's score and handles level-ups."""
    stats['score'] += points
    print(f"Added {points} points. Total Score: {stats['score']}")
    
    # Simple level-up logic
    if stats['score'] >= 100 * stats['level']:
        stats['level'] += 1
        print(f"CONGRATS! You reached Level {stats['level']}!")

def take_damage(stats, damage):
    """Reduces player health."""
    stats['health'] -= damage
    if stats['health'] < 0:
        stats['health'] = 0
    print(f"Took {damage} damage. Health: {stats['health']}")

# Simulating gameplay
print(f"Starting Game: {player_data}")

update_score(player_data, 50)
take_damage(player_data, 20)
update_score(player_data, 60) # Should trigger level up

print(f"Final Stats: {player_data}")

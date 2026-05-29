"""
Day 10: VS Gaming Studio - Save Data Manager
Concept: A script that saves and loads player progress using JSON.
"""

import json
import os

SAVE_FILE = "player_save.json"

def save_game(player_data):
    with open(SAVE_FILE, "w") as f:
        json.dump(player_data, f, indent=4)
    print("Game Progress Saved Successfully!")

def load_game():
    if not os.path.exists(SAVE_FILE):
        return {"player_name": "Guest", "level": 1, "inventory": []}
    
    with open(SAVE_FILE, "r") as f:
        return json.load(f)

# Mocking a game session
player = load_game()
print(f"Welcome back, {player['player_name']}!")
print(f"Current Level: {player['level']}")

# Simulating level up and inventory gain
player['level'] += 1
player['inventory'].append("Diamond Sword")

save_game(player)
print(f"Next session start level: {player['level']}")

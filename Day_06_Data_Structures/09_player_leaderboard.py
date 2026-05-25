# 09_player_leaderboard.py
# Concept: Sorting and complex data manipulation

# List of tuples: (Player Name, Score, Level)
leaderboard = [
    ("ShadowBlade", 4500, 22),
    ("KrishDev", 5200, 25),
    ("NeonGamer", 3800, 18),
    ("CyberWiz", 6100, 28),
    ("PixelPulse", 4900, 21)
]

print("--- Unsorted Leaderboard ---")
for player in leaderboard:
    print(player)

# 1. Sorting by Score (second element in tuple, index 1)
# Using a lambda function as the key for sorting
sorted_by_score = sorted(leaderboard, key=lambda p: p[1], reverse=True)

print("\n--- Leaderboard Sorted by Score (Descending) ---")
for i, (name, score, lvl) in enumerate(sorted_by_score, 1):
    print(f"{i}. {name:<12} | Score: {score} | Level: {lvl}")

# 2. Filtering: Players above level 20
pro_players = [p for p in leaderboard if p[2] > 20]

print("\n--- Pro Players (Level > 20) ---")
for name, score, lvl in pro_players:
    print(f"{name} (Level {lvl})")

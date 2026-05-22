# Day 2: Traffic Light Bot
# Simulating traffic light logic

light = input("Enter traffic light color (Red/Yellow/Green): ").strip().capitalize()

if light == "Red":
    print("Stop")
elif light == "Yellow":
    print("Wait")
elif light == "Green":
    print("Go")
else:
    print("Invalid color!")

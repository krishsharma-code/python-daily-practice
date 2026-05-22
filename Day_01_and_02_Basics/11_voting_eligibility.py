# Day 2: Voting Eligibility
# Checking age for voting

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote!")
else:
    print(f"You are not eligible to vote. Wait {18 - age} more year(s).")

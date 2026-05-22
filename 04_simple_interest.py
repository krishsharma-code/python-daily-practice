# 04_simple_interest.py
# Day 1: Simple Interest Calculator

print("--- Simple Interest Calculator ---")

# Taking Principal, Rate, and Time as input
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Annual Interest Rate (in %): "))
time = float(input("Enter the Time (in years): "))

# Calculating Simple Interest
# Formula: SI = (P * R * T) / 100
simple_interest = (principal * rate * time) / 100

# Printing the calculated interest and the total amount
print(f"\nCalculated Simple Interest: {simple_interest}")
print(f"Total Amount (Principal + Interest): {principal + simple_interest}")

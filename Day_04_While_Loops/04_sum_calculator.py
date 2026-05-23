# 04_sum_calculator.py
# Demonstrates a while loop calculating the sum of positive numbers until a negative is entered.

total_sum = 0
print("Positive Number Sum Calculator")
print("Enter positive numbers. Enter a negative number to see the total.")

while True:
    try:
        num = float(input("Enter a number: "))
        # Exit condition: if the number is negative
        if num < 0:
            break
        total_sum += num
        print(f"Current total: {total_sum}")
    except ValueError:
        print("Invalid input! Please enter a number.")

print(f"\nFinal sum of all positive numbers: {total_sum}")

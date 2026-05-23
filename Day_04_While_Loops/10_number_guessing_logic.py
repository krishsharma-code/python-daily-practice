# 10_number_guessing_logic.py
# Demonstrates a basic guessing game with limited attempts using logic control.

secret_number = 7
attempts_left = 3

print("--- Number Guessing Logic ---")
print("I'm thinking of a number between 1 and 10.")
print(f"You have {attempts_left} attempts.")

while attempts_left > 0:
    try:
        guess = int(input("\nEnter your guess: "))
        
        if guess == secret_number:
            print("Congratulations! You guessed it correctly! 🎉")
            break  # Exit the loop on success
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Keep trying! Attempts remaining: {attempts_left}")
            
    except ValueError:
        print("Please enter a valid number.")

if attempts_left == 0:
    print(f"\nGame Over. The secret number was {secret_number}.")

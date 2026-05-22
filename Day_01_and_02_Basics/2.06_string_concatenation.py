# Day 2: String Concatenation
# Taking user inputs and joining them

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Using + operator
full_name_plus = first_name + " " + last_name
print("Full Name (using +): " + full_name_plus)

# Using f-strings
print(f"Full Name (using f-string): {first_name} {last_name}")

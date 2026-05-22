# Day 2: Simple BMI Math
# Calculating BMI and classifying it

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Classification: Underweight")
elif 18.5 <= bmi < 25:
    print("Classification: Normal")
else:
    print("Classification: Overweight")

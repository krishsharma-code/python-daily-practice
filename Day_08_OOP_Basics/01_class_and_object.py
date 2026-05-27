class Car:
    """
    A simple class representing a Car.
    """
    pass

# Creating an instance (object) of the Car class
my_car = Car()

# Printing the object and its type
print(f"Object: {my_car}")
print(f"Type: {type(my_car)}")

# Adding attributes dynamically (not recommended for production, but possible in Python)
my_car.brand = "Toyota"
my_car.model = "Corolla"

print(f"My car is a {my_car.brand} {my_car.model}.")

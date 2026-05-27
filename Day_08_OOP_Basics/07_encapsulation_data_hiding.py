class Laptop:
    """
    Class demonstrating Encapsulation using private attributes.
    """
    def __init__(self, brand, price):
        self.brand = brand
        # Private attribute (prefixed with double underscore)
        self.__price = price

    # Getter method
    def get_price(self):
        return self.__price

    # Setter method
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

# Encapsulation in action
my_laptop = Laptop("Dell", 1200)

print(f"Brand: {my_laptop.brand}")
# print(my_laptop.__price)  # This would raise an AttributeError

print(f"Original Price: ${my_laptop.get_price()}")
my_laptop.set_price(1100)
print(f"Updated Price: ${my_laptop.get_price()}")

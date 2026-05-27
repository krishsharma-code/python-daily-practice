class Smartphone:
    """
    Class to demonstrate the __init__ constructor.
    """
    def __init__(self, brand, model, ram):
        # Initializing instance attributes
        self.brand = brand
        self.model = model
        self.ram = ram
        print(f"New Smartphone object created: {self.brand} {self.model}")

# Instantiating objects with different values
phone1 = Smartphone("Apple", "iPhone 15", "6GB")
phone2 = Smartphone("Samsung", "Galaxy S23", "8GB")

print(f"Phone 1: {phone1.brand} with {phone1.ram} RAM")
print(f"Phone 2: {phone2.brand} with {phone2.ram} RAM")

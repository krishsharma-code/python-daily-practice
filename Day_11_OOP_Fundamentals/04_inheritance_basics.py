# Day 11: Inheritance Basics
# Concept: Creating parent and child classes to reuse code.

class Device:
    """Parent Class"""
    def __init__(self, brand, power_status=False):
        self.brand = brand
        self.power_status = power_status

    def toggle_power(self):
        self.power_status = not self.power_status
        status = "ON" if self.power_status else "OFF"
        print(f"{self.brand} device is now {status}.")

class Laptop(Device):
    """Child Class inheriting from Device"""
    def __init__(self, brand, ram, storage):
        # Initializing the parent class using super()
        super().__init__(brand)
        self.ram = ram
        self.storage = storage

    def show_specs(self):
        print(f"Laptop Brand: {self.brand}, RAM: {self.ram}GB, Storage: {self.storage}GB")

# Creating an instance of the child class
my_laptop = Laptop("Dell", 16, 512)
my_laptop.show_specs()
my_laptop.toggle_power() # Inherited method

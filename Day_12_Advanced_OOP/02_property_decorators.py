class Temperature:
    """Demonstrates @property (getters, setters, and deleters)."""
    
    def __init__(self, celsius):
        self._celsius = celsius  # Protected attribute

    @property
    def celsius(self):
        """Getter: returns the value of the protected _celsius attribute."""
        print("Fetching temperature...")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter: validates input before updating the attribute."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero (-273.15°C) is impossible!")
        print(f"Setting temperature to {value}°C")
        self._celsius = value

    @celsius.deleter
    def celsius(self):
        """Deleter: cleans up or handles the deletion of the attribute."""
        print("Warning: Deleting temperature record.")
        del self._celsius

# --- Testing the implementation ---
if __name__ == "__main__":
    temp = Temperature(25)
    
    # Access via getter
    print(f"Current temp: {temp.celsius}°C")
    
    # Update via setter
    temp.celsius = 32
    print(f"New temp: {temp.celsius}°C")
    
    # Triggering validation error
    try:
        temp.celsius = -300
    except ValueError as e:
        print(f"Error: {e}")
    
    # Deleting the attribute
    del temp.celsius

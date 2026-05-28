class Employee:
    """
    Demonstrating @property for managed attribute access.
    Allows defining getter, setter, and deleter methods for an attribute.
    """
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected attribute

    @property
    def salary(self):
        """Getter: returns the salary."""
        print(f"Fetching salary for {self.name}...")
        return self._salary

    @salary.setter
    def salary(self, value):
        """Setter: adds validation logic before updating the salary."""
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        print(f"Updating salary for {self.name} to {value}...")
        self._salary = value

    @salary.deleter
    def salary(self):
        """Deleter: handles attribute deletion."""
        print(f"Deleting salary record for {self.name}...")
        del self._salary

# Testing the implementation
if __name__ == "__main__":
    emp = Employee("Alice", 50000)
    
    # Accessing like a regular attribute (calls the getter)
    print(emp.salary)
    
    # Setting like a regular attribute (calls the setter)
    emp.salary = 60000
    print(emp.salary)
    
    # Attempting to set an invalid salary
    try:
        emp.salary = -100
    except ValueError as e:
        print(f"Error: {e}")
    
    # Deleting the attribute (calls the deleter)
    del emp.salary

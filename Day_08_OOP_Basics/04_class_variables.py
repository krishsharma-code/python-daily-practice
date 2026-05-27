class Employee:
    """
    Class demonstrating Class Variables vs Instance Variables.
    """
    # Class Variable (shared by all instances)
    company_name = "Tech Solutions Corp"
    employee_count = 0

    def __init__(self, name, designation):
        # Instance Variables (unique to each instance)
        self.name = name
        self.designation = designation
        # Incrementing the class variable whenever a new object is created
        Employee.employee_count += 1

# Creating instances
emp1 = Employee("Alice", "Software Engineer")
emp2 = Employee("Bob", "Data Scientist")

print(f"Employee 1: {emp1.name}, Company: {emp1.company_name}")
print(f"Employee 2: {emp2.name}, Company: {emp2.company_name}")
print(f"Total Employees: {Employee.employee_count}")

# Changing company name at class level
Employee.company_name = "Global Innovations"
print(f"Updated Company Name: {emp1.company_name}")

# Day 11: Instance vs Class Variables
# Concept: Understanding the scope and difference between class-level and instance-level data.

class Employee:
    # Class Variable: Shared by all instances
    company_name = "Global Tech Solutions"
    total_employees = 0

    def __init__(self, name, role):
        # Instance Variables: Unique to each instance
        self.name = name
        self.role = role
        Employee.total_employees += 1 # Accessing class variable to track total count

# Creating different instances
emp1 = Employee("Alice", "Senior Developer")
emp2 = Employee("Bob", "System Architect")

print(f"Employee 1: {emp1.name} works at {emp1.company_name}")
print(f"Employee 2: {emp2.name} works at {emp2.company_name}")
print(f"Total Employees: {Employee.total_employees}")

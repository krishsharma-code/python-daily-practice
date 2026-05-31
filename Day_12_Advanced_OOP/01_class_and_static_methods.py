class Employee:
    """Demonstrates @classmethod and @staticmethod decorators."""
    company = "TechCorp"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @classmethod
    def change_company(cls, new_company):
        """Class method to change the company name for all employees.
        It takes 'cls' as the first argument, representing the class itself.
        """
        cls.company = new_company
        print(f"Company updated globally to: {cls.company}")
        
    @staticmethod
    def is_work_day(day):
        """Static method to check if a day is a work day.
        Static methods don't take 'self' or 'cls' and behave like regular functions
        but are scoped within the class for logical grouping.
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# --- Testing the implementation ---
if __name__ == "__main__":
    import datetime
    
    # Instance creation
    emp1 = Employee("Alice", 50000)
    print(f"Initial Company: {emp1.company}")
    
    # Updating class-level variable via @classmethod
    Employee.change_company("GlobalTech")
    print(f"Company for emp1: {emp1.company}")
    
    # Using @staticmethod for a utility check
    today = datetime.date.today()
    print(f"Is today ({today}) a work day? {Employee.is_work_day(today)}")

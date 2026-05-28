class MathUtils:
    """
    Demonstrating @staticmethod for utility functions.
    Static methods do not take 'self' or 'cls' as arguments.
    They behave like regular functions but are namespaced within a class.
    """
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def calculate_tax(amount, rate=0.15):
        return amount * rate

# Testing the implementation
if __name__ == "__main__":
    # Accessing static methods via the class name
    print(f"Is 10 even? {MathUtils.is_even(10)}")
    
    amount = 1000
    tax = MathUtils.calculate_tax(amount)
    print(f"Tax on ${amount} at 15% is: ${tax}")
    
    # Static methods can also be accessed via an instance (though less common)
    utils = MathUtils()
    print(f"Is 7 even? {utils.is_even(7)}")

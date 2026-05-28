class Currency:
    """
    Demonstrating Operator Overloading using __add__ and __eq__.
    Allows custom objects to interact using standard Python operators.
    """
    def __init__(self, amount, code="USD"):
        self.amount = amount
        self.code = code

    def __add__(self, other):
        # Overloading the '+' operator
        if isinstance(other, Currency) and self.code == other.code:
            return Currency(self.amount + other.amount, self.code)
        raise ValueError("Cannot add different currencies or non-currency types.")

    def __eq__(self, other):
        # Overloading the '==' operator
        if isinstance(other, Currency):
            return self.amount == other.amount and self.code == other.code
        return False

    def __str__(self):
        return f"{self.amount} {self.code}"

# Testing the implementation
if __name__ == "__main__":
    c1 = Currency(50, "USD")
    c2 = Currency(30, "USD")
    c3 = Currency(50, "USD")
    
    # Adding two Currency objects
    total = c1 + c2
    print(f"Total: {total}") # Output: 80 USD
    
    # Comparing Currency objects
    print(f"Is c1 equal to c2? {c1 == c2}") # False
    print(f"Is c1 equal to c3? {c1 == c3}") # True

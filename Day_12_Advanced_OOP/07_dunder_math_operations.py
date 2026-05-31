class Currency:
    """Demonstrates Operator Overloading using dunder methods."""
    
    def __init__(self, amount, symbol="$"):
        self.amount = amount
        self.symbol = symbol

    def __repr__(self):
        return f"{self.symbol}{self.amount:.2f}"

    def __add__(self, other):
        """Overloads the + operator."""
        if isinstance(other, Currency) and self.symbol == other.symbol:
            return Currency(self.amount + other.amount, self.symbol)
        raise ValueError("Cannot add different currencies or non-currency types.")

    def __sub__(self, other):
        """Overloads the - operator."""
        if isinstance(other, Currency) and self.symbol == other.symbol:
            return Currency(self.amount - other.amount, self.symbol)
        raise ValueError("Cannot subtract different currencies.")

    def __mul__(self, factor):
        """Overloads the * operator (e.g., currency * multiplier)."""
        if isinstance(factor, (int, float)):
            return Currency(self.amount * factor, self.symbol)
        return NotImplemented

    def __eq__(self, other):
        """Overloads the == operator."""
        return self.amount == other.amount and self.symbol == other.symbol

# --- Testing the implementation ---
if __name__ == "__main__":
    wallet1 = Currency(50.0)
    wallet2 = Currency(25.5)
    
    print(f"Wallet 1: {wallet1}")
    print(f"Wallet 2: {wallet2}")
    
    # Addition
    total = wallet1 + wallet2
    print(f"Total: {total}")
    
    # Multiplication (Tax simulation)
    with_tax = total * 1.15
    print(f"Total with 15% tax: {with_tax}")
    
    # Equality
    bonus = Currency(50.0)
    print(f"Is wallet1 equal to bonus? {wallet1 == bonus}")

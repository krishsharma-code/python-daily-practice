class InsufficientFundsError(Exception):
    """Custom exception for bank account errors."""
    def __init__(self, balance, amount):
        self.message = f"Attempted to withdraw ${amount} but balance is only ${balance}."
        super().__init__(self.message)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}")

# Testing the implementation
if __name__ == "__main__":
    acc = BankAccount("Krish", 1000)
    
    try:
        acc.withdraw(500)
        acc.withdraw(700) # This should trigger the custom exception
    except InsufficientFundsError as e:
        print(f"Transaction Failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

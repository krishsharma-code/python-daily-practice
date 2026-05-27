class BankAccount:
    """
    Class representing a Bank Account with deposit and withdraw methods.
    """
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the account balance."""
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        """Subtracts money from the account balance if funds are available."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

# Working with instance methods
account = BankAccount("Krish Sharma", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)

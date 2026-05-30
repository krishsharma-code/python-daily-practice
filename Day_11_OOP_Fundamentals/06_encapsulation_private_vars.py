# Day 11: Encapsulation & Private Variables
# Concept: Using single (_) and double (__) underscores to protect data.

class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        # Double underscore makes it 'private' (name mangling occurs)
        self.__balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def get_balance(self):
        # Public method to safely access private data
        return self.__balance

account = BankAccount("Krish", 1000)
print(f"Account Owner: {account.owner}")
account.deposit(500)
print(f"Balance: ${account.get_balance()}")

# print(account.__balance) # This would raise an AttributeError

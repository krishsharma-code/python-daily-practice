class InsufficientBalanceError(Exception):
    """Exception raised for errors in withdrawal amounts."""
    pass

def withdraw_credits(balance, amount):
    if amount > balance:
        # Raising a custom exception
        raise InsufficientBalanceError(f"Attempted to withdraw {amount}, but only {balance} is available.")
    
    new_balance = balance - amount
    return new_balance

# Main execution block
if __name__ == "__main__":
    current_credits = 100
    
    try:
        withdrawal = 150
        print(f"Attempting to withdraw {withdrawal} credits...")
        current_credits = withdraw_credits(current_credits, withdrawal)
    except InsufficientBalanceError as e:
        print(f"Transaction Failed: {e}")
    else:
        print(f"Transaction Successful! New Balance: {current_credits}")

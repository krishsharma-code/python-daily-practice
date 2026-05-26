def safe_divide():
    try:
        # Requesting input from the user
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
        
        # This might raise a ZeroDivisionError
        result = numerator / denominator
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter valid numerical values.")
    else:
        # Runs if no exception occurs
        print(f"Result of division: {result}")
    finally:
        # Always runs regardless of an error
        print("Division operation concluded.")

# Main execution block
if __name__ == "__main__":
    safe_divide()

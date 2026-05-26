def robust_calculator():
    """
    A calculator that handles bad inputs, division by zero,
    and unknown operations gracefully.
    """
    print("--- Robust Calculator ---")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("\nEnter first number (or '000' to exit): "))
            if num1 == 000: break
            
            op = input("Enter operator (+, -, *, /): ")
            
            num2 = float(input("Enter second number: "))
            
            if op == '+':
                print(f"Result: {num1 + num2}")
            elif op == '-':
                print(f"Result: {num1 - num2}")
            elif op == '*':
                print(f"Result: {num1 * num2}")
            elif op == '/':
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Invalid Operator.")
                
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Main execution block
if __name__ == "__main__":
    robust_calculator()

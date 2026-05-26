import os

def clean_dataset(file_path):
    """
    Mocks the cleaning of a Kaggle dataset.
    Handles FileNotFoundError and simulates null removal.
    """
    print(f"Attempting to process: {file_path}")
    
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset '{file_path}' not found on local disk.")
            
        print("Reading CSV data...")
        # Mocking data read
        data = ["User1, 25, None", "User2, None, Developer", "User3, 30, Designer"]
        
        print("Cleaning null values...")
        cleaned_data = [row.replace("None", "N/A") for row in data]
        
        return cleaned_data
        
    except FileNotFoundError as e:
        print(f"Data Source Error: {e}")
    except Exception as e:
        print(f"Processing Error: {e}")
    finally:
        print("Cleanup process finished.")

# Main execution block
if __name__ == "__main__":
    # Case 1: File does not exist
    clean_dataset("kaggle_titanic.csv")
    
    # Case 2: Simulating success (manually creating file would work, but this demonstrates the error handling)
    print("\nNote: In a real scenario, this would load the actual CSV.")

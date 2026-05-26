def list_studio_members(*args):
    """
    *args allows passing a variable number of positional arguments.
    Useful when we don't know how many members we might have.
    """
    print("--- VS Gaming Studio Members ---")
    for member in args:
        print(f"Member: {member}")

def project_details(**kwargs):
    """
    **kwargs allows passing a variable number of keyword arguments (key-value pairs).
    """
    print("\n--- Project Configuration ---")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# Main execution block
if __name__ == "__main__":
    # Using *args
    list_studio_members("Krish", "Alex", "Jordan", "Sam")

    # Using **kwargs
    project_details(title="Skyline Quest", engine="Unreal", version=2.5, status="Alpha")

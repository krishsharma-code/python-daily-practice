# Global variable
studio_name = "VS Gaming Studio"

def update_studio_status():
    # Local variable
    status = "Active"
    
    # Accessing global variable inside a function
    print(f"Studio {studio_name} is currently {status}.")

def change_studio_name(new_name):
    # To modify a global variable inside a function, use the 'global' keyword
    global studio_name
    studio_name = new_name
    print(f"Studio name updated to: {studio_name}")

# Main execution block
if __name__ == "__main__":
    update_studio_status()
    
    change_studio_name("VS Gaming Labs")
    
    # Verify the global change
    update_studio_status()
    
    # print(status) # This would cause a NameError because 'status' is local to update_studio_status()

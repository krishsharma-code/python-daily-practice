# Demonstrating basic file operations (Reading and Writing)

file_name = "day_07_notes.txt"

def write_to_file(text):
    # 'w' mode overwrites. 'a' mode appends.
    with open(file_name, "w") as file:
        file.write(text + "\n")
    print(f"Successfully wrote to {file_name}")

def append_to_file(text):
    with open(file_name, "a") as file:
        file.write(text + "\n")
    print(f"Successfully appended to {file_name}")

def read_file_content():
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print("--- File Content ---")
            print(content)
    except FileNotFoundError:
        print(f"Error: {file_name} does not exist yet.")

# Main execution block
if __name__ == "__main__":
    write_to_file("Day 7: Functions, Scope, and Errors.")
    append_to_file("Learning about File I/O today.")
    read_file_content()

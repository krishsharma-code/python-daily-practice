# 05_variable_scope.py
# Concept: Local vs Global variables

# This is a global variable
message = "I am a Global Message"

def show_message():
    # This is a local variable, it only exists inside this function
    local_msg = "I am a Local Message"
    print(f"Inside function: {local_msg}")
    print(f"Inside function (accessing global): {message}")

show_message()

print(f"Outside function (accessing global): {message}")

# print(local_msg) # This would raise a NameError because local_msg is not defined globally

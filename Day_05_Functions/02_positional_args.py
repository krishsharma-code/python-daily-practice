# 02_positional_args.py
# Concept: Passing basic arguments (positional arguments)

def celebrate_achievement(name, task_name):
    """
    Greets a user by name and mentions their completed task.
    These are positional arguments: their order matters.
    """
    print(f"Congratulations {name}!")
    print(f"You have successfully mastered: {task_name}")

# Calling the function with values (arguments) matching the parameters' order.
celebrate_achievement("Krish", "Positional Arguments")
celebrate_achievement("Student", "Basic Functions")

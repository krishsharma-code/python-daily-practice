"""
Day 10: CLI Arguments with sys.argv
Concept: Building a basic command-line tool that accepts arguments.
"""

import sys

def main():
    # sys.argv is a list containing command-line arguments
    # sys.argv[0] is always the script name
    
    args = sys.argv
    count = len(args)
    
    print(f"Script Name: {args[0]}")
    print(f"Number of arguments: {count - 1}")
    
    if count < 2:
        print("Usage: python 07_sys_args_cli.py [name] [age]")
        return

    name = args[1]
    print(f"Hello, {name}!")

    if count > 2:
        age = args[2]
        print(f"You are {age} years old.")

if __name__ == "__main__":
    main()

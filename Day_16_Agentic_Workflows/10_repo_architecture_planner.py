import argparse
import os
import sys
import subprocess
from google import genai
from dotenv import load_dotenv

load_dotenv()

def get_dir_structure(path="."):
    """Gets the directory structure using the 'tree' command or a recursive walk."""
    try:
        # Try using 'tree /f' on Windows
        result = subprocess.run(['tree', '/f', path], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
    except:
        pass
    
    # Fallback to os.walk
    output = []
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        output.append(f'{indent}{os.path.basename(root)}/')
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            output.append(f'{sub_indent}{f}')
    return "\n".join(output)

def plan_architecture(path="."):
    structure = get_dir_structure(path)
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    prompt = f"""
    Analyze the following project directory structure and provide a structural markdown plan for scaling the project.
    Suggest improvements in organization, modularity, and best practices.
    
    Directory Structure:
    {structure}
    """

    try:
        print("=== Generating Architecture Plan ===")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        print(response.text)

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Repo Architecture Planner CLI")
    parser.add_argument("path", nargs="?", default=".", help="Path to the repository root")
    args = parser.parse_args()

    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    plan_architecture(args.path)

if __name__ == "__main__":
    main()

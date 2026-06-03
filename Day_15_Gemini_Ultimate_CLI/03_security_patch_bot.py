import os
import argparse
import shutil
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def refactor_code(file_path):
    """
    Reads a file, asks Gemini for a secure refactor, and overwrites the file safely.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    with open(file_path, "r", encoding="utf-8") as f:
        original_code = f.read()
    
    # Create a backup before overwriting
    backup_path = f"{file_path}.bak"
    shutil.copy2(file_path, backup_path)
    print(f"Backup created at {backup_path}")

    prompt = (
        "Refactor the following code to improve its security, fix potential vulnerabilities, "
        "and ensure best practices. Return ONLY the refactored code without any markdown formatting "
        "or explanations if possible, or wrap it in a single code block.\n\n"
        f"Code:\n{original_code}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        
        # Extract code from response (handling potential markdown blocks)
        refactored_code = response.text
        if "```python" in refactored_code:
            refactored_code = refactored_code.split("```python")[1].split("```")[0].strip()
        elif "```" in refactored_code:
            refactored_code = refactored_code.split("```")[1].split("```")[0].strip()
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(refactored_code)
        
        print(f"Successfully refactored and updated {file_path}")
    except Exception as e:
        print(f"Error during refactoring: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Gemini Security Patch Bot")
    parser.add_argument("file", help="Path to the code file to refactor for security")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File {args.file} does not exist.")
        return

    print(f"Analyzing {args.file} for security patches...")
    refactor_code(args.file)

if __name__ == "__main__":
    main()

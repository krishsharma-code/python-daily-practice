import argparse
import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()

def write_tests(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    prompt = f"""
    Write edge-case unit tests using pytest for the following Python code.
    Include tests for normal operation, invalid inputs, and boundary conditions.
    Return ONLY the executable Python test code.
    
    Code:
    {code}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        
        test_code = response.text.replace("```python", "").replace("```", "").strip()
        
        test_file_path = f"test_{os.path.basename(file_path)}"
        with open(test_file_path, 'w', encoding='utf-8') as f:
            f.write(test_code)
            
        print(f"Tests written to {test_file_path}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Automated Test Writer CLI")
    parser.add_argument("file", help="Path to the Python file to test")
    args = parser.parse_args()

    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    write_tests(args.file)

if __name__ == "__main__":
    main()

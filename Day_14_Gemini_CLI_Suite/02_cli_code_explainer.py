import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """
    Reads a code file path from CLI arguments, sends its content to Gemini,
    and returns a structured technical explanation.
    """
    # Check if a file path was provided
    if len(sys.argv) < 2:
        print("Usage: python 02_cli_code_explainer.py <path_to_code_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    # Configure Gemini
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set.")
        sys.exit(1)
    
    genai.configure(api_key=api_key)

    try:
        # Read file content
        with open(file_path, 'r', encoding='utf-8') as f:
            code_content = f.read()

        print(f"--- Analyzing '{file_path}' ---\n")

        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"""
        Please provide a structured explanation of the following code.
        Include sections for:
        1. Overview
        2. Key Components (Functions, Classes)
        3. Logic Flow
        4. Complexity Analysis (Time/Space)

        Code Content:
        ```
        {code_content}
        ```
        """

        response = model.generate_content(prompt)
        print(response.text)

    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    main()

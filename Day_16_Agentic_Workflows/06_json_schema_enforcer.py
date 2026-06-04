import argparse
import json
import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()

def enforce_json(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        dirty_json = f.read()

    try:
        # Check if it's already valid
        json.loads(dirty_json)
        print("JSON is already valid.")
        return
    except json.JSONDecodeError:
        print("JSON is invalid. Asking Gemini to fix it...")

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    prompt = f"""
    The following JSON is malformed or "dirty". Fix all structural errors and return ONLY the valid, strictly typed JSON string.
    
    Dirty JSON:
    {dirty_json}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                'response_mime_type': 'application/json',
            }
        )
        
        clean_json = response.text
        # Validate the output from Gemini
        json.loads(clean_json)
        
        print("=== Cleaned JSON ===")
        print(clean_json)

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="JSON Schema Enforcer CLI")
    parser.add_argument("file", help="Path to the dirty JSON log file")
    args = parser.parse_args()

    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    enforce_json(args.file)

if __name__ == "__main__":
    main()

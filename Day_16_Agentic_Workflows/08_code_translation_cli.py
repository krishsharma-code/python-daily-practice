import argparse
import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()

def translate_code(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        python_code = f.read()

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    prompt = f"""
    Translate the following Python code into idiomatic JavaScript (Node.js).
    Maintain the same logic and functionality.
    Return ONLY the JavaScript code.
    
    Python Code:
    {python_code}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        
        js_code = response.text.replace("```javascript", "").replace("```js", "").replace("```", "").strip()
        
        js_file_path = file_path.replace(".py", ".js")
        if js_file_path == file_path:
            js_file_path += ".js"
            
        with open(js_file_path, 'w', encoding='utf-8') as f:
            f.write(js_code)
            
        print(f"Translated code saved to {js_file_path}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Code Translation CLI (Python -> JS)")
    parser.add_argument("file", help="Path to the Python script")
    args = parser.parse_args()

    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    translate_code(args.file)

if __name__ == "__main__":
    main()

import os
import argparse
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def sanitize_env(file_path):
    """
    Analyzes an environment file and scrubs sensitive data or standardizes formatting.
    """
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        env_content = f.read()

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    prompt = (
        "Analyze the following environment configuration. Create a 'template' version "
        "of this file by replacing all sensitive values (passwords, keys, tokens) "
        "with placeholders like 'YOUR_API_KEY_HERE'. Standardize the formatting. "
        "Return ONLY the sanitized template content.\n\n"
        f"Config:\n{env_content}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        
        template_content = response.text
        template_file = f"{file_path}.template"
        
        with open(template_file, "w", encoding="utf-8") as f:
            f.write(template_content)
        
        print(f"Sanitized template created at {template_file}")
    except Exception as e:
        print(f"Error during sanitization: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Gemini ENV Variable Sanitizer")
    parser.add_argument("file", help="Path to the .env or config file to sanitize")
    args = parser.parse_args()

    print(f"Sanitizing {args.file}...")
    sanitize_env(args.file)

if __name__ == "__main__":
    main()

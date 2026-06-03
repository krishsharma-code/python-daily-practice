import os
import argparse
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_dependencies(file_path):
    """
    Parses requirements.txt and queries Gemini for deprecated or outdated packages.
    """
    if not os.path.exists(file_path):
        return f"Error: {file_path} not found."

    with open(file_path, "r", encoding="utf-8") as f:
        dependencies = f.read()

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    # Token counting
    try:
        token_count = client.models.count_tokens(
            model="gemini-2.0-flash",
            contents=dependencies
        ).total_tokens
        print(f"Tokens in requirements.txt: {token_count}")
    except Exception as e:
        print(f"Could not count tokens: {e}")

    prompt = (
        "Analyze the following list of Python dependencies from requirements.txt. "
        "Identify any packages that are deprecated, have known security vulnerabilities, "
        "or have significant newer versions available. Provide a clean text report.\n\n"
        f"Dependencies:\n{dependencies}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error querying Gemini: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Gemini Dependency Version Checker")
    parser.add_argument("file", nargs="?", default="requirements.txt", help="Path to requirements.txt")
    args = parser.parse_args()

    print(f"Checking dependencies in {args.file}...")
    report = check_dependencies(args.file)
    
    print("\n--- DEPENDENCY REPORT ---\n")
    print(report)

if __name__ == "__main__":
    main()

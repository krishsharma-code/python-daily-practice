import argparse
import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()

def resolve_error(traceback):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    prompt = f"""
    Analyze the following error traceback. Identify the root cause and provide a step-by-step fix.
    
    Traceback:
    {traceback}
    """

    try:
        print("=== Analyzing Error ===")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        print(response.text)

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Error Stack Resolver CLI")
    # Using nargs='?' to allow piping or direct argument
    parser.add_argument("traceback", nargs="?", help="The raw error traceback string")
    args = parser.parse_args()

    traceback = args.traceback
    if not traceback:
        if not sys.stdin.isatty():
            traceback = sys.stdin.read()
        else:
            print("Error: No traceback provided. Please provide it as an argument or pipe it.")
            sys.exit(1)

    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    resolve_error(traceback)

if __name__ == "__main__":
    main()

import os
import argparse
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def audit_repository(path):
    """
    Scans the directory and uses Gemini to find dead code or syntax errors.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    report = []
    
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                print(f"Auditing {file_path}...")
                
                prompt = f"Audit the following Python code for dead code, syntax errors, and potential improvements:\n\n```python\n{content}\n```"
                
                try:
                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=prompt
                    )
                    report.append(f"### Audit for {file_path}\n{response.text}\n")
                except Exception as e:
                    report.append(f"### Error auditing {file_path}\n{str(e)}\n")

    return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description="Gemini Repo Auditor CLI")
    parser.add_argument("path", help="Path to the repository or directory to audit")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: Path {args.path} does not exist.")
        return

    report = audit_repository(args.path)
    print("\n--- AUDIT REPORT ---\n")
    print(report)

if __name__ == "__main__":
    main()

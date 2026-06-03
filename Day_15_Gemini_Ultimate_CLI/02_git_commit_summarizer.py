import os
import subprocess
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_git_diff():
    """
    Retrieves the current staged changes (git diff --cached).
    """
    try:
        result = subprocess.run(
            ["git", "diff", "--cached"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error retrieving git diff: {e}"

def generate_commit_message(diff_text):
    """
    Uses Gemini to generate a conventional commit message based on the diff.
    """
    if not diff_text.strip():
        return "No staged changes found to summarize."

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    prompt = (
        "Analyze the following git diff and generate a perfectly formatted conventional commit message. "
        "Use the format: <type>(<scope>): <subject>\n\n<body>\n\n<footer>\n\n"
        "Types: feat, fix, docs, style, refactor, test, chore.\n\n"
        f"Diff:\n{diff_text}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error generating commit message: {str(e)}"

def main():
    print("Fetching staged changes...")
    diff = get_git_diff()
    
    if not diff.strip():
        print("No staged changes found. Use 'git add' to stage some changes.")
        return

    print("Generating conventional commit message...")
    commit_message = generate_commit_message(diff)
    
    print("\n--- SUGGESTED COMMIT MESSAGE ---\n")
    print(commit_message)

if __name__ == "__main__":
    main()

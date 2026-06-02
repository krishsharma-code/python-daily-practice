import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """
    Sets up a Gemini agent with a specialized System Instruction.
    Acts as a 'Strict Code Auditor' to identify security vulnerabilities.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set.")
        return
    
    genai.configure(api_key=api_key)

    # Vulnerable snippet for testing
    code_snippet = """
    import sqlite3

    def get_user(username):
        db = sqlite3.connect('users.db')
        cursor = db.cursor()
        # VULNERABLE: Direct string interpolation (SQL Injection)
        query = f"SELECT * FROM users WHERE username = '{username}'"
        cursor.execute(query)
        return cursor.fetchone()
    """

    # Configure model with system_instruction
    model = genai.GenerativeModel(
        model_name='gemini-2.5-flash',
        system_instruction="""
        You are a Senior Security Engineer and Strict Code Auditor.
        Your goal is to find critical vulnerabilities (OWASP Top 10) in provided code snippets.
        Be concise, professional, and provide clear remediation steps.
        """
    )

    try:
        print("Auditing code snippet for vulnerabilities...")
        response = model.generate_content(f"Audit this code:\n{code_snippet}")
        
        print("\n--- SECURITY AUDIT REPORT ---")
        print(response.text)

    except Exception as e:
        print(f"Error during audit: {e}")

if __name__ == "__main__":
    main()

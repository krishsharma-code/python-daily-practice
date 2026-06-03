import os
import sys
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def start_interactive_shell():
    """
    A terminal-based interactive shell loop powered by Gemini.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    chat = client.chats.create(model="gemini-2.0-flash")
    
    print("=== Gemini Interactive Shell ===")
    print("Type 'exit' or 'quit' to end the session.")
    print("-" * 30)

    while True:
        try:
            user_input = input("Gemini> ")
            
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue

            response = chat.send_message(user_input)
            print(f"\nAI: {response.text}\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")

def main():
    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found in environment variables.")
        sys.exit(1)
    
    start_interactive_shell()

if __name__ == "__main__":
    main()

import argparse
import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()

def chat_loop():
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    # The user specifically requested gemini-2.5-flash
    model_id = "gemini-2.5-flash" 
    
    # We will manually manage the history list as requested
    history = []
    
    print(f"=== Advanced Chat Memory Loop ({model_id}) ===")
    print("Type 'exit' or 'quit' to end the session.")
    print("-" * 30)

    while True:
        try:
            user_input = input("You> ")
            
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue

            # Add user message to history
            history.append({"role": "user", "parts": [{"text": user_input}]})
            
            # Send the entire history to maintain context
            response = client.models.generate_content(
                model=model_id,
                contents=history
            )
            
            ai_response = response.text
            print(f"\nGemini> {ai_response}\n")
            
            # Add AI response to history
            history.append({"role": "model", "parts": [{"text": ai_response}]})
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            # Fallback to 2.0-flash if 2.5-flash is not available
            if "not found" in str(e).lower() or "404" in str(e):
                print(f"Model {model_id} not found, falling back to gemini-2.0-flash...")
                model_id = "gemini-2.0-flash"
                continue
            print(f"\nError: {str(e)}\n")

def main():
    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found.")
        sys.exit(1)
    
    chat_loop()

if __name__ == "__main__":
    main()

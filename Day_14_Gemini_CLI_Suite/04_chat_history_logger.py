import os
import json
import datetime
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """
    Starts an interactive chat session with Gemini.
    Logs the entire conversation history to a JSON file upon exit.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set.")
        return
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    chat = model.start_chat(history=[])

    history_log = []
    
    print("--- Gemini Interactive Chat (Type 'quit' or 'exit' to end) ---")
    
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit']:
                break
            
            response = chat.send_message(user_input)
            print(f"Gemini: {response.text}")
            
            # Store history
            history_log.append({
                "timestamp": datetime.datetime.now().isoformat(),
                "role": "user",
                "text": user_input
            })
            history_log.append({
                "timestamp": datetime.datetime.now().isoformat(),
                "role": "model",
                "text": response.text
            })

    except KeyboardInterrupt:
        print("\nChat terminated by user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Save history to JSON
        if history_log:
            filename = f"chat_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(history_log, f, indent=4)
            print(f"\nConversation saved to {filename}")

if __name__ == "__main__":
    main()

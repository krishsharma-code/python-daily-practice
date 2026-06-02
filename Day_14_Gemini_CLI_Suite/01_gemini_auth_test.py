import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

def main():
    """
    Connects to the Gemini API using an API key from environment variables.
    Sends a basic test prompt to verify authentication and connectivity.
    """
    # Retrieve API Key
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    # Configure the SDK
    genai.configure(api_key=api_key)

    try:
        # Initialize the model (using gemini-2.5-flash as requested)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        print("Sending 'Hello' prompt to Gemini...")
        response = model.generate_content("Hello")
        
        # In the GenAI SDK, successful response objects contain the text.
        # If there's an error, it usually raises an exception or has a blocked attribute.
        if response.text:
            print(f"Status: Success")
            print(f"Response text: {response.text.strip()}")
        else:
            print("Status: Empty response (Check for safety filters)")
            
    except Exception as e:
        print(f"Status: Authentication or Connection Failed")
        print(f"Error detail: {e}")

if __name__ == "__main__":
    main()

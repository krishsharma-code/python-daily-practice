import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """
    Calculates the token count of a given prompt using Gemini's SDK.
    Useful for budget management and context window tracking.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set.")
        return
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    print("--- Gemini Token Counter Utility ---")
    user_prompt = input("Enter your prompt to count tokens: ")

    try:
        # Using count_tokens API
        token_count_response = model.count_tokens(user_prompt)
        total_tokens = token_count_response.total_tokens
        
        print(f"\nToken Statistics:")
        print(f"- Total Tokens: {total_tokens}")
        
        # Simple cost estimation (hypothetical rates)
        # Assuming $0.000125 per 1k tokens for flash
        estimated_cost = (total_tokens / 1000) * 0.000125
        print(f"- Estimated Cost: ${estimated_cost:.8f}")

        if total_tokens > 1000000:
            print("Warning: Payload exceeds 1M tokens.")
        else:
            print("Payload is within safe limits.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

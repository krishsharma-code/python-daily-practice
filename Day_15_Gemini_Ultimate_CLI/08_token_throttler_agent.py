import os
import argparse
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN_LIMIT = 5000  # Example limit for throttling

def process_with_throttle(prompt):
    """
    Counts tokens and only proceeds if within limits.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    try:
        # Count tokens
        count_response = client.models.count_tokens(
            model="gemini-2.0-flash",
            contents=prompt
        )
        total_tokens = count_response.total_tokens
        
        print(f"Token count: {total_tokens}")
        
        if total_tokens > TOKEN_LIMIT:
            print(f"BLOCKED: Input exceeds limit of {TOKEN_LIMIT} tokens.")
            return None
        
        print("Proceeding with request...")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
        
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Gemini Token Throttler Agent")
    parser.add_argument("prompt", help="The prompt to send to Gemini (will be throttled if too large)")
    args = parser.parse_args()

    result = process_with_throttle(args.prompt)
    if result:
        print("\n--- GEMINI RESPONSE ---\n")
        print(result)

if __name__ == "__main__":
    main()

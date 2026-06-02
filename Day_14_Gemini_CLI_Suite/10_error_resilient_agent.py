import os
import time
import google.generativeai as genai
from google.api_core import exceptions
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generate_with_retry(model, prompt, max_retries=5):
    """
    Attempts to generate content with exponential backoff for quota limits (429).
    """
    for i in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except exceptions.ResourceExhausted:
            wait_time = (2 ** i) + 2
            print(f"Quota exceeded. Retrying in {wait_time}s...")
            time.sleep(wait_time)
        except exceptions.InvalidArgument as e:
            print(f"Invalid arguments (check API key or parameters): {e}")
            break
        except exceptions.DeadlineExceeded:
            print("Request timed out. Retrying...")
            time.sleep(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
    return "Failed to generate content after multiple retries."

def main():
    """
    Demonstrates an error-resilient agent that handles common API failures gracefully.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set.")
        return
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = "Write a short summary of resilience in software engineering."

    print("Sending request with retry logic...")
    result = generate_with_retry(model, prompt)
    
    print("\n--- RESULT ---")
    print(result)

if __name__ == "__main__":
    main()

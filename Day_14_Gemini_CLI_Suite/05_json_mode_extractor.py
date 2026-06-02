import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """
    Demonstrates Gemini's JSON extraction capabilities.
    Parses unstructured text into a structured JSON object.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set.")
        return
    
    genai.configure(api_key=api_key)

    # Example unstructured text (e.g., an email snippet)
    unstructured_text = """
    Hi team, I just received a receipt from our lunch at 'The Daily Pythonist' on 2026-06-01. 
    The total was $45.50, and we had 3 people: Krish, Alice, and Bob. 
    Please reimburse Krish for this expense. Category: Food & Beverage.
    """

    # Using gemini-2.5-flash which supports response_mime_type="application/json"
    model = genai.GenerativeModel(
        'gemini-2.5-flash',
        generation_config={"response_mime_type": "application/json"}
    )
    
    prompt = f"""
    Extract the following entities from the text and return them in a JSON format:
    - vendor_name
    - date
    - total_amount (number)
    - attendees (list)
    - category
    - person_to_reimburse

    Text: {unstructured_text}
    """

    try:
        print("Extracting structured data from text...")
        response = model.generate_content(prompt)
        
        # Parse and print the JSON response
        data = json.loads(response.text)
        print("\nExtracted JSON Data:")
        print(json.dumps(data, indent=4))

    except Exception as e:
        print(f"Error during JSON extraction: {e}")

if __name__ == "__main__":
    main()

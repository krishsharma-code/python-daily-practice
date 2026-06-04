import argparse
import json
import os
import sys
import requests
from bs4 import BeautifulSoup
from google import genai
from dotenv import load_dotenv

load_dotenv()

def scrape_and_extract(url):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()
            
        raw_text = soup.get_text(separator=' ', strip=True)
        # Limit text size to avoid token limits if necessary
        raw_text = raw_text[:10000] 

        prompt = f"""
        Extract the main content from the following raw HTML text and return it as a structured JSON.
        The JSON should include fields like 'title', 'author', 'date', 'summary', and 'key_points'.
        
        Raw Text:
        {raw_text}
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                'response_mime_type': 'application/json',
            }
        )
        
        print(json.dumps(json.loads(response.text), indent=2))

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Smart Web Scraper CLI")
    parser.add_argument("url", help="URL of the website to scrape")
    args = parser.parse_args()

    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    scrape_and_extract(args.url)

if __name__ == "__main__":
    main()

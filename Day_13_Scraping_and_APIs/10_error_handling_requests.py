import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError

# Day 13: Web Scraping and APIs
# Concept 10: Robust Scraping (Error Handling and Timeouts)

def safe_api_fetch(url):
    print(f"--- Fetching with Error Handling: {url} ---")
    
    try:
        # Setting a timeout (in seconds) is critical to prevent scripts from hanging
        response = requests.get(url, timeout=5)
        
        # This will raise an HTTPError for 4xx or 5xx status codes
        response.raise_for_status()
        
        print("Success! Data received.")
        return response.json()
        
    except ConnectionError:
        print("Error: Could not connect to the server. Check your internet connection.")
    except Timeout:
        print("Error: The request timed out. The server took too long to respond.")
    except HTTPError as e:
        print(f"HTTP Error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return None

if __name__ == "__main__":
    # 1. Testing with a valid URL
    valid_url = "https://jsonplaceholder.typicode.com/todos/1"
    safe_api_fetch(valid_url)
    
    # 2. Testing with a non-existent URL (to trigger HTTPError)
    invalid_url = "https://jsonplaceholder.typicode.com/invalid-endpoint"
    print("\n")
    safe_api_fetch(invalid_url)
    
    # 3. Testing with a fake domain (to trigger ConnectionError)
    fake_url = "https://this-domain-does-not-exist-at-all.com"
    print("\n")
    safe_api_fetch(fake_url)

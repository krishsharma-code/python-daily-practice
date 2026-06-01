import requests

# Day 13: Web Scraping and APIs
# Concept 01: Requests Basics (GET/POST and Status Codes)

def demonstrate_requests():
    # 1. Making a simple GET request
    # Using JSONPlaceholder, a free online REST API for testing
    url_get = "https://jsonplaceholder.typicode.com/posts/1"
    print(f"--- GET Request to: {url_get} ---")
    
    try:
        response = requests.get(url_get)
        
        # Handling status codes
        if response.status_code == 200:
            print("Successfully fetched data!")
            # Parsing JSON response
            data = response.json()
            print(f"Title: {data['title']}")
        else:
            print(f"Failed with status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    print("\n" + "-"*30 + "\n")

    # 2. Making a POST request
    url_post = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        'title': 'Learning Python',
        'body': 'Mastering Day 13: Scraping and APIs',
        'userId': 1
    }
    
    print(f"--- POST Request to: {url_post} ---")
    
    try:
        response = requests.post(url_post, json=payload)
        
        # 201 is the standard 'Created' status code
        if response.status_code == 201:
            print("Successfully created resource!")
            print(f"Response: {response.json()}")
        else:
            print(f"Post failed: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    demonstrate_requests()

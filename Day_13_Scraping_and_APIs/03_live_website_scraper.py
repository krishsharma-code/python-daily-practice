import requests
from bs4 import BeautifulSoup

# Day 13: Web Scraping and APIs
# Concept 03: Live Website Scraper (Scraping a dummy news site)

def scrape_dummy_news():
    # Using a reliable test site (toscrape.com is a standard for learning)
    url = "https://quotes.toscrape.com/"
    print(f"--- Scraping Quotes and Authors from: {url} ---")
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Check if request was successful
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Finding all quote containers
        # On this site, each quote is in a div with class 'quote'
        quotes_containers = soup.find_all('div', class_='quote')
        
        for container in quotes_containers:
            # Extract text of the quote
            text = container.find('span', class_='text').text
            # Extract author
            author = container.find('small', class_='author').text
            # Extract tags (if any)
            tags = [tag.text for tag in container.find_all('a', class_='tag')]
            
            print(f'"{text}"')
            print(f"- By: {author}")
            print(f"Tags: {', '.join(tags)}")
            print("-" * 20)
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")

if __name__ == "__main__":
    scrape_dummy_news()

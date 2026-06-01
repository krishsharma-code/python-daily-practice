import requests
from bs4 import BeautifulSoup

# Day 13: Web Scraping and APIs
# Concept 04: CSS Selectors (Advanced Scraping with .select())

def scrape_with_css_selectors():
    # Scraping a sample bookstore website
    url = "https://books.toscrape.com/"
    print(f"--- Scraping Book Titles with CSS Selectors: {url} ---")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 1. Using .select() with CSS Selectors
        # Targeting the title attribute inside <a> tags which are inside <h3> tags
        # which are inside articles with class 'product_pod'
        books = soup.select('article.product_pod h3 a')
        
        print(f"Found {len(books)} books on the homepage:\n")
        
        for index, book in enumerate(books, 1):
            # Extracting 'title' attribute which contains the full book name
            full_title = book['title']
            print(f"{index}. {full_title}")
            
        # 2. Targeting prices with CSS selector
        # Targeting the .price_color class within .product_price div
        prices = soup.select('.product_pod .product_price .price_color')
        
        print("\n--- Book Prices ---")
        for index, price in enumerate(prices, 1):
            print(f"Book {index}: {price.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_with_css_selectors()

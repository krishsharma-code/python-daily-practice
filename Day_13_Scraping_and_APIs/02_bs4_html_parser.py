from bs4 import BeautifulSoup

# Day 13: Web Scraping and APIs
# Concept 02: BeautifulSoup HTML Parser (Parsing local HTML)

# Mock HTML content for local parsing demonstration
mock_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Learning Web Scraping</title>
</head>
<body>
    <h1 id="main-heading">Welcome to Day 13</h1>
    <p class="description">Today we are mastering web scraping with BeautifulSoup.</p>
    
    <div class="content">
        <ul id="topic-list">
            <li class="topic">HTTP Requests</li>
            <li class="topic">HTML Parsing</li>
            <li class="topic">CSS Selectors</li>
            <li class="topic">API Integration</li>
        </ul>
    </div>
    
    <a href="https://www.python.org" id="python-link">Visit Python.org</a>
</body>
</html>
"""

def parse_html_content(html):
    # Initialize BeautifulSoup with the html.parser
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Extracting the page title
    print(f"Page Title: {soup.title.string}")
    
    # 2. Finding an element by ID
    heading = soup.find(id="main-heading")
    print(f"Main Heading: {heading.text}")
    
    # 3. Finding an element by class name
    desc = soup.find('p', class_='description')
    print(f"Description: {desc.text}")
    
    # 4. Finding all elements of a certain type
    topics = soup.find_all('li', class_='topic')
    print("\nTopics covered:")
    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic.text}")
        
    # 5. Extracting attributes (like href)
    link = soup.find(id="python-link")
    print(f"\nLink Text: {link.text}")
    print(f"Link URL: {link['href']}")

if __name__ == "__main__":
    parse_html_content(mock_html)

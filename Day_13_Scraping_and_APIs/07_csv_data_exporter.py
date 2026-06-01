import csv

# Day 13: Web Scraping and APIs
# Concept 07: Data Export (Writing parsed data to CSV)

def export_to_csv():
    # Mock data representing items scraped from a website
    scraped_data = [
        {"Product": "Gaming Laptop", "Price": "₹85,000", "Availability": "In Stock"},
        {"Product": "Wireless Mouse", "Price": "₹1,200", "Availability": "Out of Stock"},
        {"Product": "Mechanical Keyboard", "Price": "₹4,500", "Availability": "In Stock"},
        {"Product": "27-inch Monitor", "Price": "₹18,000", "Availability": "In Stock"},
        {"Product": "USB-C Hub", "Price": "₹2,500", "Availability": "In Stock"}
    ]
    
    filename = "scraped_products.csv"
    
    # Define the headers based on the dictionary keys
    headers = scraped_data[0].keys()
    
    try:
        # Use newline='' to prevent extra blank lines on Windows
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            
            # Writing the header row
            writer.writeheader()
            
            # Writing all data rows
            writer.writerows(scraped_data)
            
        print(f"Data successfully exported to {filename}")
        
    except Exception as e:
        print(f"An error occurred during CSV export: {e}")

if __name__ == "__main__":
    export_to_csv()

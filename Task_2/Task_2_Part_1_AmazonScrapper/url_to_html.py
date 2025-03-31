import requests
from bs4 import BeautifulSoup

def extract_html(url, filename):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        
        # Extract full HTML content
        html_content = response.text
        
        # Save to file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(html_content)
        
        print(f"HTML content saved to {filename}")
        return html_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

if __name__ == "__main__":
    url = input("Enter the URL: ")
    filename = input("Enter the filename to save the HTML: ")
    html_content = extract_html(url, filename)
    
    if html_content:
        print("\nExtracted HTML saved successfully.")
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def setup_driver():
    """Set up ChromeDriver with automatic version management."""
    options = Options()
    # Remove headless to debug visually
    # options.add_argument("--headless")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")  # Reduce bot detection
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scroll_page(driver):
    """Scroll down the page to load more products."""
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Allow time for new items to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scrape_amazon_sponsored_products(search_query, num_pages=1):
    driver = setup_driver()
    url = f"https://www.amazon.in/s?k={search_query.replace(' ', '+')}"
    driver.get(url)
    time.sleep(5)  # Allow initial load

    products = []
    
    for _ in range(num_pages):
        scroll_page(driver)  # Ensure full content is loaded
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Look for product items
        product_cards = soup.find_all("div", {"data-component-type": "s-search-result"})

        for item in product_cards:
            sponsored_tag = item.find("span", text="Sponsored")
            if not sponsored_tag:
                continue  # Skip non-sponsored products

            title_tag = item.find("h2", class_="a-size-base-plus a-spacing-none a-color-base a-text-normal")
            brand_tag = item.find("a", id="bylineInfo")
            reviews = item.find("span", class_="a-size-base")
            rating = item.find("span", class_="a-icon-alt")
            price = item.find("span", class_="a-price-whole")
            image = item.find("img")
            product_url = item.find("a", class_="a-link-normal")

            products.append({
                "Title": title_tag.text.strip() if title_tag else "N/A",
                "Brand": brand_tag.text.replace("Brand: ", "").strip() if brand_tag else "N/A",
                "Reviews": reviews.text.strip() if reviews else "N/A",
                "Rating": rating.text.strip().split()[0] if rating else "N/A",
                "Selling Price": price.text.strip() if price else "N/A",
                "Image URL": image["src"] if image else "N/A",
                "Product URL": f"https://www.amazon.in{product_url['href']}" if product_url else "N/A"
            })
        
        # Go to next page
        next_page_button = driver.find_elements(By.XPATH, "//a[contains(@class, 's-pagination-next')]")
        if next_page_button:
            next_page_button[0].click()
            time.sleep(5)  # Allow next page to load
        else:
            break

    driver.quit()
    
    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(products)
    df.to_csv("amazon_sponsored_products.csv", index=False)
    print(f"Scraped {len(products)} sponsored products. Data saved to amazon_sponsored_products.csv")

if __name__ == "__main__":
    scrape_amazon_sponsored_products("soft toys", num_pages=3)

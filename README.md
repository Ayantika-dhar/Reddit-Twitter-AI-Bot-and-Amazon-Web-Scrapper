# Reddit-Twitter AI Bot and Amazon Web Scraper

## Task 1: Reddit and Twitter Topic Research Bot

This project is a Python-based automation tool that allows users to search for a topic across Reddit and Twitter and save the top results to a Google Sheet. It uses Reddit's PRAW API and Twitter's Tweepy API to fetch data, and Google Sheets API to store it.

### Features
- Accepts a user input topic.
- Fetches top 5 Reddit posts based on the query.
- Fetches top 10 recent tweets on the same topic.
- Combines and displays results from both platforms.
- Exports data (Title, URL, Comment count) to a Google Sheet.

### Dependencies
Install the required packages using:
```bash
pip install -r requirements.txt
```

### Setup Instructions

#### 1. Reddit API Setup
- Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
- Create a script-type app and note:
  - client_id
  - client_secret
  - user_agent

#### 2. Twitter API Setup
- Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
- Create a new project and app
- Generate and copy the Bearer Token

#### 3. Google Sheets API Setup
- Visit [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project
- Enable Google Sheets API and Google Drive API
- Create credentials → Service Account → JSON Key
- Rename the key to `credentials.json`
- Share your Google Sheet with the service account email

### Usage
- Clone the repository and upload `credentials.json` to your environment.
- Run the notebook or script.
- Enter a topic when prompted.
- The combined Reddit and Twitter results will be printed and stored in a Google Sheet named `Reddit_Twitter_Research`.

### File Structure
```
Task_1/
├── task_1_reddit_twitter_search.py          # Python script version
├── Task_1_Reddit_Twitter_Search.ipynb       # Notebook version
├── requirements.txt                         # Dependencies
├── Reddit_Twitter_Research - Sheet1.pdf     # Sample Google Sheet export
```

### Output Format (in Google Sheet)
| Platform | Title | URL | Comments |

---

## Task 2 (Part 1): Amazon Sponsored Products Scraper

This project is a web scraper for extracting sponsored products from Amazon India. The scraper retrieves product details such as Title, Brand, Reviews, Rating, Selling Price, Image URL, and Product URL using Selenium & BeautifulSoup.

### Features
- Extracts sponsored product details from Amazon search results
- Handles dynamic content using Selenium
- Stores data in CSV format
- Dockerized setup for easy deployment on any machine
- Bypasses bot detection with user-agent spoofing

### Installation & Setup

#### Clone the Repository
```bash
git clone https://github.com/Ayantika-dhar/Reddit-Twitter-AI-Bot-and-Amazon-Web-Scrapper.git
cd Reddit-Twitter-AI-Bot-and-Amazon-Web-Scrapper/Task_2/Task_2_Part_1_AmazonScrapper
```

#### Install Dependencies

##### Using Python (Locally)
```bash
pip install -r requirements.txt
```

##### Using Docker (Recommended)
```bash
docker build -t Task_2_Part_1_AmazonScrapper .
```

### Running the Scraper

#### Run Locally (Python)
```bash
python scrapper.py
```

#### Run in Docker (Recommended)
```bash
docker run --rm Task_2_Part_1_AmazonScrapper
```

### Output
The scraped data will be stored in `amazon_sponsored_products.csv` with the following columns:
| Title | Brand | Reviews | Rating | Selling Price | Image URL | Product URL |
|-------|-------|---------|--------|----------------|-----------|--------------|
| Example Product | Example Brand | 500 | 4.5 | ₹799 | Image | Amazon Link |

### Troubleshooting

#### No Products Scraped?
- Ensure your IP is not blocked by Amazon (Use VPN if needed)
- Run without headless mode (`--headless` disabled in Dockerfile)

#### ChromeDriver Version Mismatch?
```bash
pip install --upgrade webdriver-manager
```

---

## Task 2 (Part 2 and 3): Data Cleaning and Analysis of Scrapped Data

- Clone the repository and upload `Amazon_sponsored_products` to your environment.
- Run the notebook either in Colab or in local environment (Jupyter/Anaconda should be available)
- You will get the clean data, visualizations as output.

# Use Python 3.13 as the base image
FROM python:3.13-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Chrome & ChromeDriver for Selenium
RUN apt-get update && apt-get install -y wget unzip \
    && wget -qO- https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb > /tmp/chrome.deb \
    && apt-get install -y /tmp/chrome.deb \
    && rm /tmp/chrome.deb \
    && wget -qO- https://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip > /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Copy all project files into the container
COPY . .

# Run the scraper script
CMD ["python", "scrapper.py"]

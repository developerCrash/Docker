Pull selenium standalone chrome and run this container 
=======================================================
docker pull selenium/standalone-chrome

docker run -d -p 4444:4444 --name selenium-hub selenium/standalone-chrome

Dockerfile
===========
FROM python:3.9

# Install dependencies
RUN pip install --no-cache-dir selenium

# Copy the script into the container
WORKDIR /app
COPY selenium_script.py .

# Run the script
CMD ["python", "selenium_script.py"]


Docker build selenium script 
============================
docker build -t selenium-app .


Run Selenium app 
=================
docker run --rm --add-host=selenium-hub:host-gateway --name selenium-app --network="host" selenium-app 

Selenium code 
==============

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Connect to Selenium running in Docker
driver = webdriver.Remote(
    command_executor="http://selenium-hub:4444/wd/hub",
    options=chrome_options
)

# Open a webpage
driver.get("https://www.python.org")

# Print page title
print("Page title:", driver.title)

# Close the browser
driver.quit()


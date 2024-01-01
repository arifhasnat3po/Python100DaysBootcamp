import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

chrome_options = Options()
option = chrome_options.add_argument("--headless")

chrome_driver_path = "C:\\Development\\chromedriver-win64\\chromedriver.exe"
service = ChromeService(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find the element representing the article count
article_number_element = driver.find_element(CSS_SELECTOR, "articlecount a")
article_number_element.click()


# # Get the text content of the element
# article_number = article_number_element.text
# print("Article Count:", article_number)

# Optional: Add a delay to see the printed article count before quitting the browser
time.sleep(50)

driver.quit()

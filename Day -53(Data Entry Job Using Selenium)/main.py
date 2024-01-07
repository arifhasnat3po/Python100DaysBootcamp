import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests

# response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
soup.title
print(soup.title)
# from selenium.webdriver.common.keys import Keys
# INSTAGRAM_ACCOUNT_PASSWORD = ""
# EMAIL = ""
# SIMILAR_ACCOUNT = ""
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
driver.get("https://www.instagram.com/")

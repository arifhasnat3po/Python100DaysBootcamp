import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
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

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Find the element representing the article count
# article_number_element = driver.find_element(CSS_SELECTOR, "articlecount a  ")
# article_number_element.click()
# encyclopedia = driver.find_element(LINK_TEXT, "encyclopedia")
# encyclopedia.click()
# search_text = driver.find_element(NAME, "search")
# search_text.send_keys("Python")
# search_text.submit()
# Find form elements by name and fill them out
driver.find_element(By.NAME, "fName").send_keys("Arif")
driver.find_element(By.NAME, "lName").send_keys("Hasnat")
driver.find_element(By.NAME, "email").send_keys("xyz@example.com")

# Submit the form
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# # Get the text content of the element
# article_number = article_number_element.text
# print("Article Count:", article_number)

# Optional: Add a delay to see the printed article count before quitting the browser
time.sleep(50)

driver.quit()

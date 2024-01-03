import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
ACCOUNT_PASSWORD = ""
PHONE = ""


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
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3784589880&f_AL=true&f_WT=2&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_JOB_FILTER")

sign_in_button = driver.find_element(LINK_TEXT, "Sign in")
sign_in_button.click()

# Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element(ID, "username")
email_field.send_keys("")
password_field = driver.find_element(ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.submit()


# Locate the apply button
time.sleep(7)
easy_apply_button = driver.find_element(CSS_SELECTOR, '.jobs-apply-button')
easy_apply_button.click()

# If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)

# phone = driver.find_element(CLASS_NAME, "fb-single-line-text__input")
# if phone.text == "":
#     phone.send_keys(PHONE)

# Submit the application
time.sleep(5)
next_button = driver.find_element(CSS_SELECTOR, '.artdeco-button--primary')
next_button.click()

time.sleep(5)
next_button = driver.find_element(CSS_SELECTOR, '.artdeco-button--primary')
next_button.click()

time.sleep(5)
next_button = driver.find_element(CSS_SELECTOR, '.artdeco-button--primary')
next_button.click()

time.sleep(100)

driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument("--headless")  # Set the --headless option directly

chrome_driver_path = "C:\\Development\\chromedriver-win64\\chromedriver.exe"

service = ChromeService(chrome_driver_path)

# Pass chrome_options directly
driver = webdriver.Chrome(service=service, options=chrome_options)
# Using different locators with find_element
driver.find_element(By.ID, "id_value")
driver.find_element(By.NAME, "name_value")
driver.find_element(By.XPATH, "xpath_value")
driver.find_element(By.LINK_TEXT, "link_text_value")
driver.find_element(By.PARTIAL_LINK_TEXT, "partial_link_text_value")
driver.find_element(By.TAG_NAME, "tag_name_value")
driver.find_element(By.CLASS_NAME, "class_name_value")
driver.find_element(By.CSS_SELECTOR, "css_selector_value")
# Using different locators with find_elements
driver.find_elements(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')


driver.get("http://www.python.org/")
time.sleep(5)

driver.quit()

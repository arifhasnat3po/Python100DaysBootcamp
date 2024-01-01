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


driver.get("http://www.python.org/")
# search_box = driver.find_element("name", "q")

# search_box.send_keys('ChromeDriver')

# search_box.submit()

# logo = driver.find_element(CLASS_NAME, "python-logo")

# print(logo.size)

# documentation = driver.find_element(CSS_SELECTOR, ".documentation-widget a")
# print(documentation.text)
event_times = driver.find_element(CSS_SELECTOR, ".event-widget last")
# print(search_box.find_element(TAG_NAME, "a"))
for time in event_times:

    print(event_times.text)


time.sleep(50000)
driver.quit()

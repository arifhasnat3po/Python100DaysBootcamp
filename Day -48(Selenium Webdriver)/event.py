import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
option = chrome_options.add_argument("--headless")

chrome_driver_path = "C:\\Development\\chromedriver-win64\\chromedriver.exe"
service = ChromeService(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=option)

driver.get("http://www.python.org/")

events = []

event_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget.last li")

for event_element in event_elements:
    time_element = event_element.find_element(By.TAG_NAME, "time")
    date_time = time_element.get_attribute("datetime")
    event_name = event_element.find_element(By.TAG_NAME, "a").text

    event = {"datetime": date_time, "name": event_name}
    events.append(event)
    # print(event.txt)

print(events)

# Optional: Add a delay to see the printed events before quitting the browser
time.sleep(5)

driver.quit()

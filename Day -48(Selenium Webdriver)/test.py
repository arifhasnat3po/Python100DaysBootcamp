import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Set the --headless option directly

chrome_driver_path = "C:\\Development\\chromedriver-win64\\chromedriver.exe"

service = ChromeService(chrome_driver_path)

# Pass chrome_options directly
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://www.python.org/")
search_bar = driver.find_element_by_name("q")
print(search_bar.get_attribute("placeholder"))

# Perform actions on the element (e.g., type something)
search_bar.send_keys("Selenium")

# Using a shorter sleep for demonstration purposes; adjust as needed
time.sleep(5)

driver.quit()

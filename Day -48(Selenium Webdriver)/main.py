import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
option = chrome_options.add_argument("--headless")


chrome_driver_path = "C:\\Development\\chromedriver-win64\\chromedriver.exe"

service = ChromeService(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=option)
driver.get("http://www.github.com/")

# driver.get("http://www.google.com/")


time.sleep(5000)

# Close the WebDriver session
driver.quit()

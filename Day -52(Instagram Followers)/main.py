import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
time.sleep(2)


email_id = driver.find_element(
    XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
email_id.send_keys('')
password = driver.find_element(
    XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys('')

login = driver.find_element(
    XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')

login.submit()
# Submit
time.sleep(8)
# notification_alert = driver.find_element(
#     XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
# notification_alert.submit()

search_text = driver.find_element(
    XPATH, '//*[@id="mount_0_0_mx"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div/svg')
search_text.send_keys("Python")
search_text.submit()

time.sleep(500)
driver.quit()

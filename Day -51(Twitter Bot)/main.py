import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
TWITTER_ACCOUNT_PASSWORD = ""
EMAIL = ""


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
driver.get("https://www.speedtest.net/")

# time.sleep(2)
speed_test = driver.find_element(
    XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
# speed_test = driver.find_element(CSS_SELECTOR, "start-text")
speed_test.click()


time.sleep(60)
result_id = driver.find_element(
    XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a')

print(result_id.text)

download_speed = driver.find_element(
    XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

upload_speed = driver.find_element(
    XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')


print(download_speed)
print(upload_speed)
download_speed_result = float(download_speed.text)
upload_speed_result = float(upload_speed.text)

if download_speed_result <= 100 or upload_speed_result <= 50:
    print('Test failed! Download Speed is less than 50 Mbps and Upload')
    twitter_driver = webdriver.Chrome(service=service, options=option)
    twitter_driver.get(
        "https://twitter.com/i/flow/login?redirect_after_login=%2Fhome")

    # Use find_element_by_xpath to get a single element for the email field
    login_element = twitter_driver.find_element(XPATH,
                                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    login_element.send_keys(EMAIL)
    login_element.submit()

    # The rest of your code for password and login button seems correct
    password_element = driver.find_element(XPATH,
                                           '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password_element.send_keys(TWITTER_ACCOUNT_PASSWORD)
    password_element.submit()

    login_button = twitter_driver.find_element(XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
    login_button.click()

driver.quit()

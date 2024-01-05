import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
# from selenium.webdriver.common.keys import Keys
FB_ACCOUNT_PASSWORD = ""
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
driver.get("https://tinder.com/")

# sign_in_button = driver.find_element(LINK_TEXT, "Sign in")
# sign_in_button.click()
# //*[@id="u-1919424827"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]
time.sleep(2)
login_button = driver.find_element(XPATH,
                                   '//*[@id="u-1919424827"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

time.sleep(2)
fb_login = driver.find_element(XPATH,
                               '//*[@id="u647161393"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
fb_login.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(XPATH, '//*[@id="email"]')
password = driver.find_element(XPATH, '//*[@id="pass"]')

email.send_keys(EMAIL)
password.send_keys(FB_ACCOUNT_PASSWORD)
password.submit()

driver.switch_to.window(base_window)
print(driver.title)

# Delay by 5 seconds to allow page to load.
time.sleep(5)

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)

allow_button = driver.find_element(
    XPATH, "//*[@id='o-1687095699']/div/div/div/div/div[3]/button[1]")
allow_button.submit()
time.sleep(2)
not_interested_button = driver.find_element(
    XPATH, "//*[@id='o-1687095699']/div/div/div/div/div[3]/button[2]")
not_interested_button.submit()
time.sleep(2)
accept_button = driver.find_element(
    XPATH, "//*[@id='o41285377']/div/div[2]/div/div/div[1]/button")
accept_button.submit()
time.sleep(7)
for i in range(20):
    print(i)
    try:
        dislike_button = driver.find_element(
            XPATH, "//*[@id='o41285377']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button")
        dislike_button.submit()

    except ElementNotInteractableException:
        try:
            dislike_button_2 = driver.find_element(XPATH,
                                                   "//*[@id='o41285377']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button")
            dislike_button_2.submit()
            time.sleep(3)
        except:
            not_interested = driver.find_element(
                XPATH, "//*[@id='o-1687095699']/div/div/div[2]/button[2]")
            not_interested.submit()
            time.sleep(3)

    except:
        # time.sleep(3)
        dislike_button_2 = driver.find_element(
            XPATH, "//*[@id='o41285377']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button")
        dislike_button_2.submit()
        time.sleep(3)

    else:
        time.sleep(3)

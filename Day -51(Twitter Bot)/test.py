from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "YOUR_CHROME_DRIVER_PATH"
TWITTER_EMAIL = "YOUR_TWITTER_EMAIL"
TWITTER_PASSWORD = "YOUR_TWITTER_PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        chrome_options = Options()
        chrome_options.headless = False  # Set to True if you want to run in headless mode
        self.driver = webdriver.Chrome(
            executable_path=driver_path, options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)

        go_button = self.driver.find_element(
            By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        time.sleep(60)

        self.up = self.get_speed("upload")
        self.down = self.get_speed("download")

    def get_speed(self, direction):
        xpath = f'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[{
            "2" if direction == "upload" else "3"}]/div/div[2]/span'
        return self.driver.find_element(By.XPATH, xpath).text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)

        email = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        tweet_compose = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {
            self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)

    def quit_driver(self):
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()

if int(bot.down) < PROMISED_DOWN or int(bot.up) < PROMISED_UP:
    bot.tweet_at_provider()

bot.quit_driver()

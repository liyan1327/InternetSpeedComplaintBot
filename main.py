from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 400
PROMISED_UP = 400
CHROME_DRIVE_PATH = "Your Chrome Drive Path"
TWITTER_EMAIL = "Your Twitter Account"
TWITTER_PASSWORD = "Your Twitter Password"
TWITTER_USERNAME = "Your Twitter Username"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        print("start initialization")
        self.driver = webdriver.Chrome(service=Service(driver_path))
        self.down = 0
        self.up = 0
        print("finish init")


    def get_internet_speed(self):
        
        self.driver.get("https://www.speedtest.net/")
        
        time.sleep(15)
        print("Starting click")

        self.go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        self.go_button.click()

        time.sleep(40)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(self.up.text)
        print(self.down.text)


    def tweet_at_providers(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(5)
        self.email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.email.send_keys(TWITTER_EMAIL)
        self.email.send_keys(Keys.TAB)
        self.email.send_keys(Keys.ENTER)
        time.sleep(8)

        self.username = self.driver.find_element(By.NAME, 'text')
        self.username.send_keys(TWITTER_USERNAME)
        self.username.send_keys(Keys.ENTER)

        time.sleep(8)

        self.pas=self.driver.find_element(By.NAME,'password')
        self.pas.send_keys(TWITTER_PASSWORD)
        self.pas.send_keys(Keys.TAB+Keys.TAB+Keys.TAB+Keys.ENTER)
        time.sleep(8)
        self.tweet=self.driver.find_element(By.XPATH,"//div[contains(@aria-label, 'Tweet text')]")
        self.tweet.send_keys(f'Hey Internet Operator. My down speed is {self.down.text} and up is {self.up.text} instead of {PROMISED_DOWN} down & {PROMISED_UP} up.')
        self.button=self.driver.find_element(By.XPATH,'//div[@data-testid="tweetButtonInline"]').click()

        self.driver.quit()
        

bot = InternetSpeedTwitterBot(CHROME_DRIVE_PATH)
bot.get_internet_speed()
bot.tweet_at_providers()


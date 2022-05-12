from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from yt_dlp import YoutubeDL
import getpass, time

class User:
    def __init__(self, u, p):
        self.user = u
        self.passwd = p
    
    def run(self):
        browser = webdriver.Chrome()
        browser.get('https://www.hockeytv.com/login')
        email_input = browser.find_element(By.XPATH, '//*[@id="emailInput"]')
        passwd_input = browser.find_element(By.XPATH, '//*[@id="passwordInput"]')
        email_input.send_keys(self.user)
        passwd_input.send_keys(self.passwd)
        time.sleep(10)
        browser.quit()
        ## implement webdriver wait on search bar

my_user = User(input("Enter username: "), getpass.getpass("Enter password: "))
my_user.run()

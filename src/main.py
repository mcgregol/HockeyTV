from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from yt_dlp import YoutubeDL
import getpass, time

class User:
    def __init__(self, u, p):
        self.user = u
        self.passwd = p
    
    def get_link(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

        browser = webdriver.Firefox(firefox_profile=firefox_profile)
        browser.scopes = ['.*akamaized.*']

        browser.get('https://www.hockeytv.com/login')

        email_input = browser.find_element(By.XPATH, '//*[@id="emailInput"]')
        passwd_input = browser.find_element(By.XPATH, '//*[@id="passwordInput"]')
        sign_in = browser.find_element(By.XPATH, '/html/body/app-root/section/div/div[2]/app-login/div/div/form/button')

        email_input.send_keys(self.user)
        passwd_input.send_keys(self.passwd)
        sign_in.click()

        try:
            print("Navigate to desired game video...")
            vod_link = browser.wait_for_request('/main.m3u8', timeout=500)
            
            browser.quit()
            return vod_link
        except:
            print("incorrect credentials or bad connection...")
            browser.quit()

my_user = User(input("Enter HockeyTV email: "), getpass.getpass("Enter HockeyTV password(hidden): "))
my_user.get_link()
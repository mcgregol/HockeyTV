from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yt_dlp import YoutubeDL
import getpass, time

class User:
    def __init__(self, u, p):
        self.user = u
        self.passwd = p
    
    def run(self):
        browser = webdriver.Firefox()
        browser.get('https://www.hockeytv.com/login')

        email_input = browser.find_element(By.XPATH, '//*[@id="emailInput"]')
        passwd_input = browser.find_element(By.XPATH, '//*[@id="passwordInput"]')
        sign_in = browser.find_element(By.XPATH, '/html/body/app-root/section/div/div[2]/app-login/div/div/form/button')

        email_input.send_keys(self.user)
        passwd_input.send_keys(self.passwd)
        sign_in.click()

        try:
            search_wait = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="term"]')))
            print("Navigate to desired game video...")

            vid_wait = WebDriverWait(browser, 120).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="contentArea"]/app-game/div/div[2]/div/app-game-summary/div/div[1]/div[2]/div')))
            print("nice!")

            browser.quit()
        except:
            print("incorrect credentials or bad connection...")
            browser.quit()

my_user = User(input("Enter HockeyTV email: "), getpass.getpass("Enter HockeyTV password: "))
my_user.run()

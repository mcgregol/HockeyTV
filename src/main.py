from http.server import executable
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from yt_dlp import YoutubeDL
import getpass, time
import yt_dlp

class MyLogger:
    def debug(self, msg):
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')

class User:
    def __init__(self, u, p):
        self.user = u
        self.passwd = p
    
    def get_link(self):
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

        browser = webdriver.Firefox(
            firefox_profile=firefox_profile,
            executable_path='bin\geckodriver.exe')
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
            vod_link = str(browser.wait_for_request('/main.m3u8', timeout=500))
            print("Grabbed video location!\nDownloading, please be patient...")
            
            browser.quit()
            return vod_link
        except:
            print("incorrect credentials or bad connection...")
            browser.quit()

my_user = User(input("Enter HockeyTV email: "), getpass.getpass("Enter HockeyTV password(hidden): "))
url = my_user.get_link()

ydl_opts = {
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
print("All done!")

## TODO: add filedialog to select path for final product
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from yt_dlp import YoutubeDL
from appJar import gui
import getpass, time
import yt_dlp

class MyLogger:
    def debug(self, msg):
        if msg.startswith('[debug] '):
            print(msg)
        else:
            self.info(msg)

    def info(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

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
            firefox_profile=firefox_profile)
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
            print("Grabbed video location!")
            
            browser.quit()
            return vod_link
        except:
            print("incorrect credentials or bad connection...")
            browser.quit()

app = gui()

def press_login(button):
    if button == "Run":
        global url
        my_user = User(app.getEntry("HockeyTV Email:"), app.getEntry("HockeyTV Password:"))
        app.stop()
        url = my_user.get_link()
    else:
        app.stop()
        exit()

app.addLabel("htv-grabber", "htv-grabber by Liam McGregor")
app.setLabelBg("htv-grabber", "green")

app.addLabelEntry("HockeyTV Email:")
app.addLabelSecretEntry("HockeyTV Password:")

app.addSaveEntry("Video location")
save_as = app.getEntry("Video location") + ".mp4"

app.addButtons(["Run", "Exit"], press_login)

app.go()

ydl_opts = {
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'outtmpl': save_as
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print("Beginning download!\nPress CTRL + C at any time to abort...")
    time.sleep(5)
    ydl.download(url)

print("All done!\nVideo saved as \"" + save_as + "\"")

## IMPLEMENT MULTIPLE VIDEO DOWNLOAD
from seleniumwire import webdriver
from yt_dlp import YoutubeDL
import time, getpass

class User:
    def __init__(self, u, p):
        self.user = u
        self.passwd = p
    
    def run(self):
        browser = webdriver.Firefox()
        browser.get('https://1.1.1.1')

my_user = User(input("Enter username: "), getpass.getpass("Enter password: "))
my_user.run()
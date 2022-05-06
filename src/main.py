from seleniumwire import webdriver
from yt_dlp import YoutubeDL
import time, getpass

driver = webdriver.Firefox(executable_path='geckodriver.exe')

driver.get('https://google.com')

class Vod:
    def __init__(self, url):
        self.url = url
    
    def getVod()
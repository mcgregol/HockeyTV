from seleniumwire import webdriver
from yt_dlp import YoutubeDL
import time, getpass

class User:
    def __init__(self, u, p):
        self.user = u
        self.passwd = p

myUser = User(input("Enter username: "), getpass.getpass("Enter password: "))

print(myUser.user)
print(myUser.passwd)
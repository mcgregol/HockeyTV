from seleniumwire import webdriver
from yt_dlp import YoutubeDL
import time, getpass

class User:
    def __init__(self, u, p):
        self.user = u
        self.passwd = p

my_user = User(input("Enter username: "), getpass.getpass("Enter password: "))

print(my_user.user)
print(my_user.passwd)
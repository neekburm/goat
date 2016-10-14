import os
from selenium import webdriver
chromedriver = "Users"

chromedriver = "/home/neekburm/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

browser.get('http://localhost:8000')

assert 'Django' in browser.title


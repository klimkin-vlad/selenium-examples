from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
import time
import random
import sys

options = Options()
options.add_argument("-profile")
options.add_argument("./profile")
service = Service(executable_path='./geckodriver')

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Firefox(service = service, options = options)
    browser.get(link)
    browser.find_element(By.ID, "button") 

finally:
    time.sleep(10)
    browser.quit()


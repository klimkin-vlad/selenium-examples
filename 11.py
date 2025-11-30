from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
import time
import random
import os

options = Options()
options.add_argument("-profile")
options.add_argument("./profile")
service = Service(executable_path='./geckodriver')

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox(service = service, options = options)
    browser.get(link)

    element1 = browser.find_element(By.XPATH, "//input[@name='firstname']")
    element2 = browser.find_element(By.XPATH, "//input[@name='lastname']")
    element3 = browser.find_element(By.XPATH, "//input[@name='email']")
    element4 = browser.find_element(By.ID, "file")
    element1.send_keys("Vlad")
    element2.send_keys("Klimkin")
    element3.send_keys("example@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt')
    element4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


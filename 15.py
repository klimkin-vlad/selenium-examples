from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math
import random
import sys

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

options = Options()
options.add_argument("-profile")
options.add_argument("./profile")
service = Service(executable_path='./geckodriver')

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Firefox(service = service, options = options)
    browser.implicitly_wait(12)
    browser.get(link)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    textField = browser.find_element(By.ID, "answer")
    textField.send_keys(y)
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()

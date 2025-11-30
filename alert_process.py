from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

options = Options()
options.add_argument("-profile")
options.add_argument("./profile")
service = Service(executable_path='./geckodriver')

try:
    browser = webdriver.Firefox(service = service, options = options)
    browser.get("https://suninjuly.github.io/alert_accept.html")
    button1 = browser.find_element(By.CSS_SELECTOR, "button")
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(0.1)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    textField = browser.find_element(By.CSS_SELECTOR, "#answer")
    textField.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "button")
    button2.click()

finally:
    time.sleep(30)
    browser.quit()

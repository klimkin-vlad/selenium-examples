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
    browser.get("https://SunInJuly.github.io/execute_script.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    textField = browser.find_element(By.CSS_SELECTOR, "#answer")
    textField.send_keys(y)
    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check.click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(30)
    browser.quit()

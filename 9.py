from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math


options = Options()
options.add_argument("-profile")
options.add_argument("./profile")
service = Service(executable_path='./geckodriver')

try:
    browser = webdriver.Firefox(service = service, options = options)
    browser.get("https://suninjuly.github.io/selects1.html")
    num1_elem = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2_elem = browser.find_element(By.CSS_SELECTOR, "#num2")
    num1 = int(num1_elem.text)
    num2 = int(num2_elem.text)
    y = num1 + num2
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

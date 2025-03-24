from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link='https://suninjuly.github.io/math.html'
try:
    browser=webdriver.Chrome()
    browser.get(link)
    x=browser.find_element(By.CSS_SELECTOR,'#input_value')
    x=int(x.text)
    x=math.log(abs(12*math.sin(x)))
    
    input1=browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(x)
    checkbox=browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()
    robots=browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robots.click()
    button=browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
    28.9306768267285
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link='https://suninjuly.github.io/alert_accept.html'
try:
    browser=webdriver.Chrome()
    browser.get(link)
    button1=browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click() 
    browser.switch_to.alert.accept()
    x=int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    x=math.log(abs(12*math.sin(x)))
    input1=browser.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys(x)
    button2=browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]' ).click()

    
finally:
    time.sleep(5)
    browser.quit()

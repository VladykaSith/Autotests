from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link='https://suninjuly.github.io/wait1.html'
try:
    browser=webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    
    btn_verify=browser.find_element(By.CSS_SELECTOR, '#verify').click()
    message1='Verification was successful!'
    message2=browser.find_element(By.CSS_SELECTOR, '#verify_message').text
    if message1==message2:
        print('Success!')
    else:
        print('Сообщения не совпадают')

finally:
    time.sleep(3)
    browser.quit()
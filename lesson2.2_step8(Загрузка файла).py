from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
link='https://suninjuly.github.io/file_input.html'
try:
    browser=webdriver.Chrome()
    browser.get(link)
    name1=browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Vlad')
    name2=browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Naumov')
    email=browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('Naumov_Vladyka@mail.ru')
    current_dir=os.path.abspath(os.path.dirname(__file__))
    file_path=os.path.join(current_dir,'HelloWorld.txt')
    button=browser.find_element(By.CSS_SELECTOR,'#file').send_keys(file_path)
    btn=browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    
finally:
    time.sleep(30)
    browser.quit()
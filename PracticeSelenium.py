from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link='http://suninjuly.github.io/simple_form_find_task.html'
try:
    browser=webdriver.Chrome()
    browser.get(link)
    input1=browser.find_element(By.CSS_SELECTOR, '[name="first_name"]')
    input1.send_keys('Vlad')
    input2=browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    input2.send_keys('Naumov')
    button=browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
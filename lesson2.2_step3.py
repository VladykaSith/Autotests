from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
link='https://suninjuly.github.io/selects2.html'
try:
    browser=webdriver.Chrome()
    browser.get(link)
    x1=int(browser.find_element(By.CSS_SELECTOR,'#num1').text)
    x2=int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
    x=str(x1+x2)
    select=Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(x)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()
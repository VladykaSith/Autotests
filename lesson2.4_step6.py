from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link='http://suninjuly.github.io/cats.html'
try:
    browser=webdriver.Chrome()
    browser.get(link)
    btn=browser.find_element(By.ID, "button").click()

finally:
    time.sleep(3)
    browser.quit()
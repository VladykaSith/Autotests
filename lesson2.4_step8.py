from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link='https://suninjuly.github.io/explicit_wait2.html'
try:
    browser=webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '100'))
    btn=browser.find_element(By.CSS_SELECTOR, "#book").click()
    x=int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    x= math.log(abs(12*math.sin(x)))
    input1=browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(x)
    submit=browser.find_element(By.CSS_SELECTOR, '#solve').click()
finally:
    time.sleep(7)
    browser.quit()
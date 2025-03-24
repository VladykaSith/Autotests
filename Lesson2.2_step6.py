from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link='https://SunInJuly.github.io/execute_script.html'
try:
    browser=webdriver.Chrome()
    browser.get(link)
    x=int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    x=str(math.log(abs(12*math.sin(x))))
    input1=browser.find_element(By.CSS_SELECTOR,'#answer')
    print(x)
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(x)
    robot=browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot)
    robot.click()
    robot2=browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true)', robot2)
    robot2.click()
    btn=browser.find_element(By.CSS_SELECTOR,'.btn')
    browser.execute_script('return arguments[0].scrollIntoView(true)', btn)
    btn.click()
finally:
    time.sleep(30)
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link="https://www.saucedemo.com/"
try:
    browser=webdriver.Chrome()
    browser.get(link)
    input1=browser.find_element(By.CSS_SELECTOR, '[name="user-name"]')
    input1.send_keys('standard_user')
    input2=browser.find_element(By.CSS_SELECTOR, '#password')
    input2.send_keys('secret_sauce')
    button=browser.find_element(By.CSS_SELECTOR, 'input[name="login-button"]')
    button.click()
    time.sleep(2)
    button2=browser.find_element(By.CSS_SELECTOR, 'button.btn[name="add-to-cart-sauce-labs-backpack"]')
    button2.click()
    time.sleep(2)
    check='1'
    check1=browser.find_element(By.CSS_SELECTOR,'.shopping_cart_badge[data-test="shopping-cart-badge"]')
    print(check1.text)
    if check1.text==check:
        print('HHOOORAY')
    else:
        print('Failed')
finally:
    time.sleep(5)
    browser.quit()
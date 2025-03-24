from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link='https://anketolog.ru/'
try:
    browser=webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    cookie=browser.find_element(By.CSS_SELECTOR,'#cookie-alert__btn')
    cookie.click()
    button=browser.find_element(By.CSS_SELECTOR,'button[data-target="#header-login-modal"]:nth-of-type(1)')
    button.click()
    time.sleep(2)
    email=browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Эл. почта"]')
    email.send_keys('v.naumov@anketolog.ru')
    password=browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Пароль"]')
    password.send_keys('uq)ah~o9n@TpJ&C4P(#m')
    time.sleep(2)
    captcha=browser.find_element(By.CSS_SELECTOR, 'input[name="smart-token"]')
    captcha.click()
    captcha()
    time.sleep(2)
    enter=browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    enter.click()
finally:
    time.sleep(7)
    browser.quit()
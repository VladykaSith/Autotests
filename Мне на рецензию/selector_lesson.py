from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    _block1 = browser.find_element(By.CLASS_NAME, "first_block")
    _block2 = browser.find_element(By.CLASS_NAME, "second_block")

    input1 = _block1.find_element(By.CLASS_NAME, "form-control.first")
    input1.send_keys("Murad")
    input2 = _block1.find_element(By.CLASS_NAME, "form-control.second")
    input2.send_keys("Legend")
    input3 = _block1.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("lol_kek@mmm.ru")
    input4 = _block2.find_element(By.CLASS_NAME, "form-control.first")
    input4.send_keys("9999999999")
    input5 = _block2.find_element(By.CLASS_NAME, "form-control.second")
    input5.send_keys("Puskin street, Kolotuskin`s house")
    time.sleep(5)
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
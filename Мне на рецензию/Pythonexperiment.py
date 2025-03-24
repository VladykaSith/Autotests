from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def reg_form(browser):
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(1) input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(2) input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block div:nth-child(3) input")
    input3.send_keys("email@mail.ru")
    input4 = browser.find_element(By.CSS_SELECTOR, ".second_block div:nth-child(1) input")
    input4.send_keys("+79168887755")
    input5 = browser.find_element(By.CSS_SELECTOR, ".second_block div:nth-child(2) input")
    input5.send_keys("Russia, Moscow")
    time.sleep(5)

def check_form(browser, link):
    # Открываем url
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    reg_form(browser)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    print("Success")

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()

    print(f"test1 link={link1}")
    check_form(browser, link1)

    print(f"test2 link={link2}")
    check_form(browser, link2)
    time.sleep(10)
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()


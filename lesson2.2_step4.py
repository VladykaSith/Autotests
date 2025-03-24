from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
#browser.get(link)
#browser.execute_script("document.title='Script executing';")
#time.sleep(5)
#browser.execute_script("alert('Привет! Как дела?');")
#time.sleep(5)
browser.execute_script("document.title='Halloween';alert('Whats up');")
time.sleep(3)
browser.quit()

#ловилось исключение и выполнение кода зависало:
#получилось исправить с помощью добавления в код:

alert = browser.switch_to.alert
alert.accept()
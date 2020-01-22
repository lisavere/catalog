import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://yandex.ru/")
time.sleep(5)

textinput = driver.find_element_by_css_selector(".input__input")

textinput.send_keys("Алтайский государственный университет")
time.sleep(5)

submit_button = driver.find_element_by_css_selector(".suggest2-form__button")

submit_button.click()
time.sleep(15)

driver.quit()
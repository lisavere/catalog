import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://google.ru/")
time.sleep(5)

textinput = driver.find_element_by_css_selector(".gLFyf")

textinput.send_keys("АГУ")
time.sleep(3)
 
submit_button = driver.find_element_by_css_selector(".gNO89b")

submit_button.click()
time.sleep(10)

driver.quit()
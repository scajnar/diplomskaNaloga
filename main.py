import time

from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://selenium.dev")
time.sleep(5)
driver.quit()
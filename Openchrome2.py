from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://google.com")
driver.get("https://facebook.com")
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()

time.sleep(5)

driver.refresh()


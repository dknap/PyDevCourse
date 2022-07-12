from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://www.python.org')

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.ENTER)
time.sleep(5)

driver.close()
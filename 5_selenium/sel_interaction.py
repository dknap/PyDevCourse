from pydoc import classname
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://www.flashscore.com/')

log_button = driver.find_element(By.ID, 'user-menu')
log_button.click() # click the button = clean elemen 

time.sleep(3)

mail = driver.find_element(By.ID, 'email')
mail.clear()
mail.send_keys('example@yourmail.com')
pw = driver.find_element(By.ID, 'passwd')
pw.clear()
pw.send_keys('password')

entry_button = driver.find_element(By.CLASS_NAME, 'loginWindow__button--login')
entry_button.click()

time.sleep(5)
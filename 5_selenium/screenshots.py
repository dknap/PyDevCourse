from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://facebook.com')

driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file('./Facebook.png')

driver.find_element(By.ID, 'email').send_keys('mail@yourmail.com')
driver.find_element(By.NAME, 'pass').send_keys('password')
driver.find_element(By.ID, 'loginbutton').click()
driver.get_screenshot_as_file('./Facebook1.png')

driver.quit()
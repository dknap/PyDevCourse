from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://python.org')

# search_form = driver.find_element(By.ID, 'id-search-field')
# search_form = driver.find_element(By.XPATH, 'html/body/div/header/div/div/div/form/fieldset/input')
# search_form = driver.find_element(By.NAME, 'q')
search_form = driver.find_element(By.CLASS_NAME, 'search-field')

print('My search form element is: ')
print(search_form)

search_form.clear()
search_form.send_keys('Linux')
search_form.send_keys(Keys.RETURN)
time.sleep(5)

driver.close()
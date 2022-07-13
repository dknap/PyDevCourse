from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://jqueryui.com/droppable')
driver.switch_to.frame(0)

action_chains = ActionChains(driver)
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
time.sleep(2)

action_chains.drag_and_drop_by_offset(source, 0, 0).perform()
time.sleep(2)

action_chains.drag_and_drop(source, target).perform()
time.sleep(2)

driver.close()
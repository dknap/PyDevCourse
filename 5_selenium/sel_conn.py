from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.soccerstats.com')
# browser.set_window_size(400, 800)
browser.maximize_window()
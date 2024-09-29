from selenium import webdriver
driver = webdriver.Edge()
driver.get('https://www.google.com')
driver.close()                 #It closes the current tab
#driver.quit()                 It closes the entire browser
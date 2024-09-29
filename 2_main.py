from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("http://www.python.org")
assert "Python" in driver.title             # We are checking that does python is present in title or not. It not then assertion will fail and program will stop
elem = driver.find_element(By.NAME, "q")    #Finding elements by name
elem.clear()
elem.send_keys("pycon")                     # Entering the key in search bar
elem.send_keys(Keys.RETURN)                 # Pressing enter key
assert "No results found." not in driver.page_source   #We are expecting that is hould give the result if result is not present it will raise an error
time.sleep(6)
driver.close()
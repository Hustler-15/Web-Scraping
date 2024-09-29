from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

query = "laptop"
driver = webdriver.Edge()
driver.get(f"https://www.amazon.com/s?k={query}&ref=nb_sb_noss")  
element = driver.find_element(By.CLASS_NAME, "puis-card-container")
print(element.text)         #To print the actual details
print(element.get_attribute("outerHTML"))   #To get the html details
time.sleep(5)
driver.close()
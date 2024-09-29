from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

query = "laptop"
driver = webdriver.Edge()
for i in range(1, 21):
    driver.get(f"https://www.amazon.com/s?k={query}&page={i}&ref=nb_sb_noss")   #collecting data from page 1 to 20
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} item found")
    print(elems)
    for elem in elems:
        print(elem.text)         #To print the actual details
time.sleep(5)
driver.close()
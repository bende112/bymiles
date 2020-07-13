import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/fixterall/Downloads/chromedriver-2")
driver.implicitly_wait(5)
driver.get("https://www.bymiles.co.uk/")
print(driver.title)

time.sleep(2)
driver.quit()



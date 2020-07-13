from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time

browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.safari
else:
    print('Please pass correct browser name :' + browserName)
    raise Exception('driver not found')

driver.implicitly_wait(5)
driver.get("https://www.bymiles.co.uk/")
driver.fullscreen_window()
print(driver.title)

getQuote_Link = driver.find_element(By.LINK_TEXT, 'GET A QUOTE')
getQuote_Link.click()

assert "Get a quote, quickly." in driver.page_source

inputBoxes = []
inputBoxes = driver.find_elements_by_css_selector("input[class='text']")

enterYourRegNumber = driver.find_element_by_xpath('.//*[@datacy="formbox-input"]')
enterYourRegNumber.send_keys("BD17 UNX")
getA_QuickQuote = driver.find_element_by_xpath('.//*[@datacy="qq-main"]')
getA_QuickQuote.click()

heading = driver.find_element(By.TAG_NAME, 'h5')
print(heading.text, 'NISSAN JUKE N-CONNECTA')

yesContinue_link = driver.find_element_by_xpath(".//*[@datacy='quick-quote-mileage-continue']")
yesContinue_link.click()

time.sleep(2)


yearClaim = driver.find_elements_by_css_selector('.Select-control')[0].click()
select = Select(yearClaim)
select.select_by_value('0')

time.sleep(5)

age = driver.find_element(By.XPATH, '//*[@id="age"]/input')
age.send_keys(40)

postCode = driver.find_element(By.XPATH, '//*[@id="postcode"]/input')
postCode.send_keys('NR9 3AH')

insuranceRenew = driver.find_element(By.XPATH, '//*[@name="renewal_month"]/input')
insuranceRenew.send_keys("March")


# for element in insuranceRenew:
#     print(element.text)
#     if element.text == 'January':
#         element.click()
#         break

time.sleep(5)
driver.quit()

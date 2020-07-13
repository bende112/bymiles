from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher('re')


@given('a user is on the  homepage')
def step_impl(context):

    browser = webdriver.Chrome(executable_path="/Users/fixterall/Downloads/chromedriver-2")
    browser.implicitly_wait(5)
    browser.get("https://www.bymiles.co.uk/")
    print(browser.title)

    browser.quit()

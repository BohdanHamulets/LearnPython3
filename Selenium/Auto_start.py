import os
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#driver = webdriver.Firefox()
url = "https://10.76.71.58/mail_policies/email_security_manager/incoming_mail_policies"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()



elem = driver.find_element_by_name("username")
elem.clear()
elem.send_keys("admin")

elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys("Cisco123$")

time.sleep(5)
elem = driver.find_element_by_name("action:Login")
elem.send_keys(Keys.RETURN)

time.sleep(5)
# assert 'Dictionaries' in driver.title

for x in range(1, 101):
    driver.get(url)
    add_enrty = driver.find_element_by_xpath('//*[@id="content"]/form/dl/dd[2]/div/input')
    add_enrty.click()

    elem = driver.find_element_by_name("rpolicyName")
    elem.send_keys(x)

    elem = driver.find_element_by_class_name("button-secondary")
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element_by_class_name("submit")
    elem.send_keys(Keys.RETURN)

    my_bla = driver.getElementsByClassName("submit")
    my_bla.click()

"""for x in range(1, 101):
    elem = driver.find_element_by_xpath("//input[@value='Add Dictionary...']")
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element_by_name("id")
    elem.send_keys(x)
    elem = driver.find_element_by_name("add_list")
    elem.send_keys('test')
    elem = driver.find_element_by_xpath("//input[@value='Add'][@type='button']")
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element_by_xpath("//input[@value='Submit'][@type='button']")
    elem.send_keys(Keys.RETURN)
    time.sleep(5)

    elem = driver.find_element_by_id("action-results-title")
    assert 'Success' in elem.text"""



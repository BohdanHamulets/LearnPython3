import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



#webdriver.ChromeOptions.binary_location = ur"/home/bgam/Downloads/chromedriver" 

#self.webdriver = webdriver.Chrome()

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='/home/bgam/Downloads/chromedriver')
driver.get('https://vm30esa0026.ibqa.sgg.cisco.com/mail_policies/dictionaries')

elem = driver.find_element_by_name("username")
elem.clear()
elem.send_keys("admin")

elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys("Cisco123~")

elem = driver.find_element_by_name("action:Login")
elem.send_keys(Keys.RETURN)

time.sleep(5)
# assert 'Dictionaries' in driver.title

for x in range(1, 101):
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
    assert 'Success' in elem.text

import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver


url = 'http://tokyo.uk'

#url_r = requests.get(url)
#url_soup = BeautifulSoup(url_r.text, 'html.parser')

#print(url_soup.findAll('img'))

driver = webdriver.Firefox()
driver.get(url)


html_ = driver.execute_script("return document.documentElement.outerHTML")
selenium_soup = BeautifulSoup(html_, 'html.parser')
print(selenium_soup.findAll('img'))

list_of_images = []
for single_image in selenium_soup.findAll('img'):
    #print (single_image)
    list_of_images.append(single_image)

number = len(list_of_images)
print (list_of_images) 
print("number of images in this list is {number}".format(number=number))





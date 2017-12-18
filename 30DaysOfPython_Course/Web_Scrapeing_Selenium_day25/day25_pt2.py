import os
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import shutil
import time

#url = 'http://tokyo.uk'
url = 'http://www.chrisburkard.com/Stills/Landscape/'
#url_r = requests.get(url)
#url_soup = BeautifulSoup(url_r.text, 'html.parser')

#print(url_soup.findAll('img'))

driver = webdriver.Firefox()
driver.get(url)




list_of_images = []
for i in selenium_soup.findAll('img'):
    src = i["src"]
    list_of_images.append(src)

#number = len(list_of_images)
 

current_path = os.getcwd()
iterations = 0

while iterations < 10:
    html_ = driver.execute_script("return document.documentElement.outerHTML")
    selenium_soup = BeautifulSoup(html_, 'html.parser')
    #print(selenium_soup.findAll('img'))
    print (list_of_images)
    for img in list_of_images:
        try:
            file_name = os.path.basename(img)
            img_r = requests.get(img, stream=True)
            new_path = os.path.join(current_path, "dir_4_images", file_name)
            with open (new_path, "wb") as output_file:
                shutil.copyfileobj(img_r.raw, output_file)
            del img_r
        except:
            pass
    iterations +=1
    time.sleep(5)







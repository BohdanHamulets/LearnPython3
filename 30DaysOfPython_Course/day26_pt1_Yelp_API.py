import os
import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
import shutil
import time


Client_ID = "0p3nQve_S9RGarSa61LZgw"
Client_Secret= "5kDllAvYay4AEoDr02dHXf7TXapNEt8JqL2nR9KBlFP03HRNjgpVp4wmHFWp0uVM"


https://api.yelp.com/oauth2/token


url = "https://api.yelp.com/v3/businesses/search"
r = requests.get(url)
print(r.status_code)

print(r.text)
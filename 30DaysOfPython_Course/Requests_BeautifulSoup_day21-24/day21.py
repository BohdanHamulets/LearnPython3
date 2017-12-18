import requests
from bs3 import BeautifulSoup

url = "https://www.yelp.com/sf"

yelp_r = requests.get(url)

print(yelp_r.status_code) #should be 200

yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

print(yelp_soup.prettify())

print(yelp_soup.findAll('a'))


for link in yelp_soup.findAll('a'):
    print(link)
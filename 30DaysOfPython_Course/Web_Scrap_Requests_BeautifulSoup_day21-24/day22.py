import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_loc="
loc = 'Newport Beach, CA'
page = 10


url= base_url + loc + "&start=" + str(page)

yelp_r = requests.get(url)

print(yelp_soup.findAll('li',{'class': 'regular-search-result'}))

print(yelp_soup.findAll('a',{'class': 'biz-name'}))

for name in yelp_soup.findAll('a',{'class': 'biz-name'}):
    print(name.text)








print(yelp_r.status_code) #should be 200

yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

print(yelp_soup.prettify())

print(yelp_soup.findAll('a', {'class':}))


for link in yelp_soup.findAll('a'):
    print(link)



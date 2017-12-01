import requests
from bs4 import BeautifulSoup
import os

base_url = "https://www.yelp.com/search?find_loc="
loc = 'London'
current_page = 0

while current_page < 201:
    print(current_page)
    url= base_url + loc + "&start=" + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
    file_path = 'yelp2-{loc}.txt'.format(loc=loc)
    businesses = yelp_soup.findAll('div',{'class': 'biz-listing-large'})
    with open(file_path, 'a') as textfile:
        businesses = yelp_soup.findAll('div',{'class': 'biz-listing-large'})
            for biz in businesses:
            title = biz.findAll('a', {'class': 'biz-name'})[0].text
            print(title)
            try:
                address = biz.findAll('address')[0]
            except:
                address = None
            print(address)
            try:
                phone = biz.findAll('span', {'class': 'biz-phone'})[0].text
            except:
                phone= None
            print(phone)
            page_line = "{title}\n{address}\n{phone}\n".format(
                title = title,
                address = address,
                phone = phone
                )
            textfile.write(page_line)
    current_page +=10






























print(yelp_soup.findAll('li',{'class': 'regular-search-result'}))

print(yelp_soup.findAll('a',{'class': 'biz-name'}))

for name in yelp_soup.findAll('a',{'class': 'biz-name'}):
    print(name.text)













print(yelp_r.status_code) #should be 200



print(yelp_soup.prettify())

print(yelp_soup.findAll('a', {'class':}))


for link in yelp_soup.findAll('a'):
    print(link)



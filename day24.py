import requests
from bs4 import BeautifulSoup
import os


loc = 'London,+United%20Kingdom'
#change this var for other place if you want to scrap other location
pages_number= 200
#change this var to alter number of pages you want to scrap

def lookup_be_location(loc, pages_number):
    base_url = "https://www.yelp.com/search?find_loc="
    current_page = 0
    #defining url that we'll parse and var current page with step += 10
    while current_page < pages_number:
        print(current_page)
        url= base_url + loc + "&start=" + str(current_page)
        #putting url together
        yelp_r = requests.get(url)
        #making a request with this URL using requests lib
        yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
        #using bs4 to parce page that was returned
        file_path = 'yelp2-{loc}.txt'.format(loc=loc)
        #defining file path and name that we're going to store this info
        businesses = yelp_soup.findAll('div',{'class': 'biz-listing-large'})
        #will go through selected businesses
        with open(file_path, 'a') as textfile:
            businesses = yelp_soup.findAll('div',{'class': 'biz-listing-large'})
            for biz in businesses:
                #going through every business
                title = biz.findAll('a', {'class': 'biz-name'})[0].text
                print(title)
                address = biz.findAll('address')[0].contents
                second_line= ""
                first_line = ""
                #this try block neede because not all addresses consist from one part
                try:
                    for item in address:
                        if "br" in str(item):
                            #print(item.getText())
                            second_line += item.getText().strip(" \n\t\r")
                        else:
                            print(item.strip(" \n\t\r"))
                            first_line += item.strip(" \n\t\r")
                    print(first_line)
                    print(second_line)
                except:
                    pass
                print("\n")
                try:
                    phone = biz.findAll('span', {'class': 'biz-phone'})[0].getText().strip(" \n\t\r")
                except:
                    phone= None
                print(phone)
                #defining var to select what we're going to write into our file
                page_line = "{title}\n{address1}\n{address2}\n{phone}\n".format(
                    title = title,
                    address1 = first_line,
                    address2 = second_line,
                    phone = phone
                    )
                #writting to a file
                textfile.write(page_line)
        #going to the next page
        current_page +=10

lookup_be_location(loc, pages_number)

'''
you can also call this function with needed location by passing argument
as a string, like lookup_be_location('Newport+Beach,+CA,+United+States')
'''


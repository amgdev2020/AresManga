#!/usr/bin/python3

import requests
import json
import argparse
from bs4 import BeautifulSoup


# Making a GET request
parser = argparse.ArgumentParser()
parser.add_argument("-u", dest="url")

args = parser.parse_args()
page_num = args.url if args.url else None
url = 'https://fl-ares.com/page/'+page_num

r = requests.get(url)
home_list = []
soup = BeautifulSoup(r.content, 'html.parser')

items = soup.find('div')
ratings = soup.find('div', class_='numscore')

    


result_items = []

for a in items.find_all(class_='bsx'):
    
    try:
       title = a.a['title']
    except:
       title = 'Not found'
    try:
       link = a.a['href']
    except:
       link = 'Not found'
    try:
       image = a.div.img['src']
    except:
       image = 'Not found'
    try:
       rating = a.find('div', class_='numscore').text
    except:
       rating = 'Not found'
    
    result_items.append({"title":title, "link":link, "image":image, "rating":rating})
    

results = json.dumps(result_items)
#with open("home_page_"+page_num+".json", "w") as outfile:
#    outfile.write(results)
print(results)


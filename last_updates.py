#!/usr/bin/python3

import requests
import json

from bs4 import BeautifulSoup


# Making a GET request

url = 'https://fl-ares.com/series/?order=update'

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
#with open("last_updates.json", "w") as outfile:
#    outfile.write(results)
print(results)


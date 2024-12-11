#!/usr/bin/python3

import requests
import json
import argparse
from bs4 import BeautifulSoup


# Making a GET request
parser = argparse.ArgumentParser()
parser.add_argument("-u", dest="url")

args = parser.parse_args()
url = args.url if args.url else None
r = requests.get(url)
cat_list = []
soup = BeautifulSoup(r.content, 'html.parser')

s_title = soup.find('h1', class_='entry-title')
s_title2 = soup.find('span', class_='alternative')
s_category = soup.find('div', class_='wd-full')
s_desc = soup.find('div', class_='entry-content entry-content-single')
s_img = soup.find('img', class_='attachment- size- wp-post-image')
s_rating = soup.find('div', class_='num')
s_followers = soup.find('div', class_='bmc')
s_state = soup.find_all('div', class_='imptdt')
s_shapters = soup.find('div', class_='eplister')

try:
  title = s_title.text
except:
  title = 'Not found'

try:
  title2 = s_title2.text
except:
  title2 = 'Not found'

try:
  image = s_img['src']
except:
  image = 'Not found'
try:
  description = s_desc.text
except:
  description = 'Not found'
try:
  rating = s_rating.text
except:
  rating = 'Not found'
try:
  followers = s_followers.text
except:
  followers = 'Not found'
try:
  state = s_state[0].i.text
except:
  state = 'Not found'
try:
  typee = s_state[1].a.text
except:
  typee = 'Not found'

try:
  author = s_state[2].i.text
except:
  author = 'Not found'

try:
  painter = s_state[3].i.text
except:
  painter = 'Not found'
shapters_list = []
for b in s_shapters.ul.find_all('li'):
    
    try:
      soort = b['data-num']
    except:
      soort = 'Not found'
    try:
      name = b.find('span', class_='chapternum').text
    except:
      name = 'Not found'
    try:
      date = b.find('span', class_='chapterdate').text
    except:
      date = 'Not found'
    try:
      link = b.a['href']
    except:
      link = 'Not found'
    
    chapter_url = link
    chapter_tmp_1 = 'https://fl-ares.com/wp-content/uploads/series/data/'
    old_string = chapter_url.replace('-chapter', '')
    k = old_string.rfind("-")
    new_string = old_string[:k] + "/" + old_string[k+1:]
    chapter_tmp_2 = new_string.replace('https://fl-ares.com/', chapter_tmp_1)


    chapter_1 = chapter_tmp_2+'1.jpg'
    chapter_2 = chapter_tmp_2+'2.jpg'
    chapter_3 = chapter_tmp_2+'3.jpg'
    shapter = {"sort":soort,"name":name,"date":date,"link":link, "ch1":chapter_1, "ch2":chapter_2, "ch3":chapter_3}
    shapters_list.append(shapter)
    
for a in s_category.find_all('a', href=True):
    
    try:
      cat_list.append(a.text)
    except:
      cat_list.append('Not found')

category = json.dumps(cat_list)
shapters = json.dumps(shapters_list)

#print(title)
#print(title2)
#print(image)
#print(category)
#print(description)
#print(rating)
#print(followers)
#print(typee)
#print(author)
#print(painter)
#print(shapters)

info_json = {"title":title,"title2":title2,"image":image,"category":category,"desc":description,"rating":rating,"followers":followers,"type":typee,"author":author,"painter":painter, "chapters":shapters}
info = json.dumps(info_json)

#with open("info.json", "w") as outfile:
#    outfile.write(info)
print(info)

    
    


#!/usr/bin/python3

import requests
import json
import argparse
from bs4 import BeautifulSoup


# Making a GET request
"""
#url = input('URL:')
url = 'https://fl-ares.com/martial-god-asura-chapter-800/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')


shapter = soup.find('img', class_='ts-main-image curdown')
print(shapter)



#shapters = shapter.img
    
#for a in shapters:
#    print(a['src'])
    
    
    
    
"""
parser = argparse.ArgumentParser()
parser.add_argument("-u", dest="url")

args = parser.parse_args()
chapter_url = args.url if args.url else None

chapter_tmp_1 = 'https://fl-ares.com/wp-content/uploads/series/data/'
old_string = chapter_url.replace('-chapter', '')
k = old_string.rfind("-")
new_string = old_string[:k] + "/" + old_string[k+1:]
chapter_tmp_2 = new_string.replace('https://fl-ares.com/', chapter_tmp_1)


chapter_1 = chapter_tmp_2+'1.jpg'
chapter_2 = chapter_tmp_2+'2.jpg'
chapter_3 = chapter_tmp_2+'3.jpg'
chapters = []
chapters.append(chapter_1)
chapters.append(chapter_2)
chapters.append(chapter_3)
chapters_file = json.dumps(chapters)
with open("chapters.json", "w") as outfile:
    outfile.write(chapters_file)
print('done')


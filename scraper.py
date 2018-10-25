# import libraries
import urllib2
from bs4 import BeautifulSoup

random_kym = "https://www.knowyourmeme.com/random" # not sure if this will work without some kinda redirect flag

random_meme_page = urllib2.urlopen(random_kym)

random_meme_page_parsed = BeautifulSoup(random_meme_page, 'html.parser')

title = random_meme_page_parsed.find("meta", property="og:title")["content"]
image_link = random_meme_page_parsed.find("meta", property="og:image")["content"]
description = random_meme_page_parsed.find("meta", property="og:description")["content"]

print(title)
print(image_link)
print(description)

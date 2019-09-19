#!/usr/bin/env python
# coding: utf-8

# In[31]:
#This code lists out the GPU names from newegg website

import requests
from bs4 import BeautifulSoup 

url = "https://www.newegg.com/global/in-en/p/pl?d=graphics+card"

#grabs the webpage
page = requests.get(url, timeout = 5)

#parsing html
soup = BeautifulSoup(page.content, "html.parser")

#finds all of the relative tags and sets ground for looping
container = soup.findAll("div",{"class":"item-info"})

#loop to grab names
for contains in container:
    x = contains.findAll("a", {"class":"item-title"})
    product_name = x[0].text
    print(product_name+ "\n")


#!/usr/bin/env python
# coding: utf-8

# In[31]:


import requests
from bs4 import BeautifulSoup 

url = "https://www.newegg.com/global/in-en/p/pl?d=graphics+card"

page = requests.get(url, timeout = 5)

soup = BeautifulSoup(page.content, "html.parser")

container = soup.findAll("div",{"class":"item-info"})

for contains in container:
    x = contains.findAll("a", {"class":"item-title"})
    product_name = x[0].text
    print(product_name+ "\n")

